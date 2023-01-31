# не получаетс использовать класс
# т.к. sql не может поддерживать многопоточность и блокируется поэтому используем курсор и оператор with


import sqlite3 as sl
from sqlite3 import DatabaseError
# from typing import Any


class DataBase:
    def __init__(self):
        self.tbl = sl.connect('playersdata.db')
        self.cursor = self.tbl.cursor()

    def create_table(self):
        # CREATE TABLE IF NOT EXISTS PLAYERSTBL - проверить что работает
        self.tbl.execute("""
              CREATE TABLE PLAYERSTBL (
                  player_id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  player_name TEXT,
                  assets_all  INTEGER,
                  current_bet INTEGER,
                  bet_on      INTEGER
              );
          """)

    def create_table_new(self):
        # CREATE TABLE IF NOT EXISTS PLAYERSTBL - проверить что работает
        self.tbl.execute("""
              CREATE TABLE PLAYERSDATA (
                  player_id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  player_name TEXT,
                  assets_all  INTEGER,
                  plays_all INTEGER,
                  plays_on  INTEGER,
                  bet_current INTEGER,
                  field1 INTEGER,
                  field2 INTEGER,
                  field3 INTEGER,
                  field4 TEXT,
                  field5 TEXT
              );
          """)

        # def insert_player (tbl ,entities):

    def insert_player_short(self, entities: [int, str , int, int, int]):
        with self.tbl:
            sqlstr = 'INSERT INTO PLAYERSDATA (player_id, player_name, assets_all, plays_all, plays_on) values(?, ?, ?, ?, ?)'
            try:
                self.cursor.execute(sqlstr, entities)
                # self.cursor.commit()
                res = True
            except DatabaseError:
                # print('error no user !!')
                res = False
            return res

    def insert_player_full(self,
                           entities: [int, str , int, int, int, int, int, int, int, str , str ]):
        with self.tbl:
            sqlstr = 'INSERT INTO PLAYERSDATA (player_id, player_name, assets_all, plays_all, plays_on, bet_current, field1, field2, field3, field4, field5) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            try:
                self.cursor.execute(sqlstr, entities)
                # self.cursor.commit()
                res = True
            except DatabaseError:
                res = False
                # print('error no user !!')
            return res

    def select_player_assets_by_id(self, player_id):
        with self.tbl:
            sqlstr = 'SELECT assets_all FROM PLAYERSDATA WHERE player_id = ' + str(player_id)
            data = self.cursor.execute(sqlstr)
            assets = data.fetchone()
        # преобразуем кортеж в строку и потом в число чтобы вернуть число
        res = ""
        for i in assets:
            res += str(i)
            res = int(res)
        return res
        # for row in data:
        #     print(row)

    def select_player_assets_plays_by_id(self, player_id):
        with self.tbl:
            sqlstr_assets = 'SELECT assets_all FROM PLAYERSDATA WHERE player_id = ' + str(player_id)
            sqlstr_plays = 'SELECT plays_all FROM PLAYERSDATA WHERE player_id = ' + str(player_id)
            sqlstr_wins = 'SELECT plays_on FROM PLAYERSDATA WHERE player_id = ' + str(player_id)
            sqlstr_win_assets = 'SELECT field1 FROM PLAYERSDATA WHERE player_id = ' + str(player_id)
            sqlstr_loss_assets = 'SELECT field2 FROM PLAYERSDATA WHERE player_id = ' + str(player_id)

            # деньги
            data_assets = self.cursor.execute(sqlstr_assets)
            assets = data_assets.fetchone()
            # игры
            data_plays = self.cursor.execute(sqlstr_plays)
            plays = data_plays.fetchone()
            # победы
            data_wins = self.cursor.execute(sqlstr_wins)
            wins = data_wins.fetchone()

            # выигранные деньги
            data_win_assets = self.cursor.execute(sqlstr_win_assets)
            win_assets = data_win_assets.fetchone()
            # проигранные деньги
            data_loss_assets = self.cursor.execute(sqlstr_loss_assets)
            loss_assets = data_loss_assets.fetchone()

        # преобразуем кортеж в строку и потом в число чтобы вернуть число
        res = ""
        res_dict = dict()

        for i in assets:
            res += str(i)
            res = int(res)
        res_dict['assets'] = res

        res = ""
        for i in plays:
            res += str(i)
            res = int(res)
        res_dict['plays'] = res

        res = ""
        for i in wins:
            res += str(i)
            res = int(res)
        res_dict['wins'] = res

        res = ""
        for i in win_assets:
            res += str(i)
            res = int(res)
        res_dict['win_assets'] = res

        res = ""
        for i in loss_assets:
            res += str(i)
            res = int(res)
        res_dict['loss_assets'] = res

        return res_dict
        # for row in data:
        #     print(row)

    def select_players(self):
        with self.tbl:
            sqlstr = 'SELECT * FROM PLAYERSDATA'
            data = self.cursor.execute(sqlstr)
            rows = data.fetchall()
            # кол-во выбранных строк
            print(len(rows))
            print(rows)

    def update_player_assets_abs_by_id(self, player_id, val):
        with self.tbl:
            sqlstr = 'UPDATE PLAYERSDATA set assets_all =' + str(val) + ' WHERE player_id = ' + str(player_id)
            self.cursor.execute(sqlstr)

    def update_player_assets_by_id_up(self, player_id, val):
        with self.tbl:
            assets = self.select_player_assets_by_id(player_id)
            assets = assets + val
            sqlstr = 'UPDATE PLAYERSDATA set assets_all =' + str(assets) + ' WHERE player_id = ' + str(player_id)
            self.cursor.execute(sqlstr)
            # self.cursor.commit()

    def update_player_assets_plays_by_id_up(self, player_id, val):
        with self.tbl:
            data = self.select_player_assets_plays_by_id(player_id)
            assets = data['assets'] + val
            plays = data['plays'] + 1
            wins = data['wins'] + 1
            win_assets = data['win_assets'] + val
            sqlstr = 'UPDATE PLAYERSDATA set assets_all=' + str(assets) + ', plays_all=' + str(plays) + ', plays_on=' + str(
                wins) + ', field1=' + str(win_assets) + ' WHERE player_id = ' + str(player_id)
            self.cursor.execute(sqlstr)
            # self.cursor.commit()

    def update_player_assets_by_id_down(self, player_id, val):
        with self.tbl:
            assets = self.select_player_assets_by_id(player_id)
            assets = assets - val
            sqlstr = 'UPDATE PLAYERSDATA set assets_all =' + str(assets) + ' WHERE player_id = ' + str(player_id)
            self.cursor.execute(sqlstr)
            # self.cursor.commit()

    def update_player_assets_plays_by_id_down(self, player_id, assets, plays, loss_assets):
        with self.tbl:
            sqlstr = 'UPDATE PLAYERSDATA set assets_all =' + str(assets) + ', plays_all =' + str(plays) + ', field2=' + str(
                loss_assets) + ' WHERE player_id = ' + str(player_id)
            self.cursor.execute(sqlstr)
            # self.cursor.commit()

    def update_player_data(self, player_id, val):
        with self.tbl:
            assets = self.select_player_assets_by_id(player_id)
            assets = assets - val
            sqlstr = 'UPDATE PLAYERSDATA set assets_all =' + str(assets) + ' WHERE player_id = ' + str(player_id)
            self.cursor.execute(sqlstr)
            # self.cursor.commit()

