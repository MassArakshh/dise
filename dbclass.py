# не получаетс использовать класс
# т.к. sql не может поддерживать многопоточность и блокируется


import sqlite3 as sl
from sqlite3 import DatabaseError
# from sqlite3 import DatabaseError
from typing import Any


class DataBase:

    def __int__(self, tbl):
        # (self, tbl, entities, player_id, val):
        self.tbl = sl.connect('players.db')
        # self.insert_player(entities)
        # self.select_players(tbl)
        # self.select_player_assets_by_id(player_id)
        # self.update_player_assets_by_id_up(player_id, val)
        # self.update_player_assets_by_id_down(player_id, val)
        # self.update_player_assets_abs_by_id(player_id, val)

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

    # def insert_player (tbl ,entities):
    def insert_player(self, entities: tuple[Any, str | Any, int, int, int]):
        tbl = sl.connect('players.db')
        sqlstr = 'INSERT INTO PLAYERSTBL (player_id, player_name, assets_all, current_bet, bet_on) values(?, ?, ?, ?, ?)'
        try:
            tbl.execute(sqlstr, entities)
            tbl.commit()
        except DatabaseError:
            print('error no user !!')

    def select_player_assets_by_id(self, player_id):
        sqlstr = 'SELECT assets_all FROM PLAYERSTBL WHERE player_id = ' + str(player_id)
        data = self.tbl.execute(sqlstr)
        assets = data.fetchone()
        # преобразуем кортеж в строку и потом в число чтобы вернуть число
        res = ""
        for i in assets:
            res += str(i)
            res = int(res)
        return res
        # for row in data:
        #     print(row)

    def select_players(self, tbl):
        sqlstr = 'SELECT * FROM PLAYERSTBL'
        data = tbl.execute(sqlstr)
        rows = data.fetchall()
        print(rows)
        # кол-во выбранных строк
        # print(len(rows))

    def update_player_assets_abs_by_id(self, player_id, val):
        tbl = sl.connect('players.db')
        sqlstr = 'UPDATE PLAYERSTBL set assets_all =' + str(val) + ' WHERE player_id = ' + str(player_id)
        data = tbl.execute(sqlstr)
        assets = data.fetchone()
        # return assets
        # for row in data:
        #     print(row)

    def update_player_assets_by_id_up(self, player_id, val):
        assets = self.select_player_assets_by_id(player_id)
        assets = assets + val
        sqlstr = 'UPDATE PLAYERSTBL set assets_all =' + str(assets) + ' WHERE player_id = ' + str(player_id)
        data = self.tbl.execute(sqlstr)
        assets = data.fetchone()
        self.tbl.commit()
        # return assets
        # for row in data:
        #     print(row)

    def update_player_assets_by_id_down(self, player_id, val):
        assets = self.select_player_assets_by_id(player_id)
        assets = assets - val
        sqlstr = 'UPDATE PLAYERSTBL set assets_all =' + str(assets) + ' WHERE player_id = ' + str(player_id)
        data = self.tbl.execute(sqlstr)
        assets = data.fetchone()
        self.tbl.commit()
        # return assets
        # for row in data:
        #     print(row)

    # if __name__ == '__main__':
    #     select_players(tbl)
    #     update_player_assets_by_id(tbl, 1, 50)
    #     assets = select_player_assets_by_id(tbl, 2)
    #     print(assets)
    #     entities = (3, 'Den', 30, 0, 0)
    #     insert_player(tbl, entities)
    # select_players(tbl)
    # insert_player(tbl, entities)
