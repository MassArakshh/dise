import sqlite3 as sl
from sqlite3 import DatabaseError
# from sqlite3 import DatabaseError
# from typing import Any

tbl = sl.connect('playersdata.db')

def create_table():
    # CREATE TABLE IF NOT EXISTS PLAYERSTBL - проверить что работает
    tbl.execute("""
          CREATE TABLE PLAYERSTBL (
              player_id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              player_name TEXT,
              assets_all  INTEGER,
              current_bet INTEGER,
              bet_on      INTEGER
          );
      """)

def create_table_new():
    # CREATE TABLE IF NOT EXISTS PLAYERSTBL - проверить что работает
    tbl.execute("""
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

def insert_player_short(entities: [int, str , int, int, int]):
    sqlstr = 'INSERT INTO PLAYERSDATA (player_id, player_name, assets_all, plays_all, plays_on) values(?, ?, ?, ?, ?)'
    try:
        tbl.execute(sqlstr, entities)
        tbl.commit()
        res = True
    except DatabaseError:
        # print('error no user !!')
        res = False
    return res

# ! доделать!!!
def insert_player_full(entities: [int, str , int, int, int, int, int, int, int, str , str ]):
    sqlstr = 'INSERT INTO PLAYERSDATA (player_id, player_name, assets_all, plays_all, plays_on, bet_current, field1, field2, field3, field4, field5) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    try:
        tbl.execute(sqlstr, entities)
        tbl.commit()
        res = True
    except DatabaseError:
        res = False
        # print('error no user !!')
    return res

def select_player_assets_by_id(player_id):
    sqlstr = 'SELECT assets_all FROM PLAYERSDATA WHERE player_id = ' + str(player_id)
    data = tbl.execute(sqlstr)
    assets = data.fetchone()
    # преобразуем кортеж в строку и потом в число чтобы вернуть число
    res = ""
    for i in assets:
        res += str(i)
        res = int(res)
    return res
    # for row in data:
    #     print(row)

def select_player_assets_plays_by_id(player_id):
    sqlstr_assets = 'SELECT assets_all FROM PLAYERSDATA WHERE player_id = ' + str(player_id)
    sqlstr_plays = 'SELECT plays_all FROM PLAYERSDATA WHERE player_id = ' + str(player_id)
    sqlstr_wins = 'SELECT plays_on FROM PLAYERSDATA WHERE player_id = ' + str(player_id)
    sqlstr_win_assets = 'SELECT field1 FROM PLAYERSDATA WHERE player_id = ' + str(player_id)
    sqlstr_loss_assets = 'SELECT field2 FROM PLAYERSDATA WHERE player_id = ' + str(player_id)

    # деньги
    data_assets = tbl.execute(sqlstr_assets)
    assets = data_assets.fetchone()
    # игры
    data_plays = tbl.execute(sqlstr_plays)
    plays = data_plays.fetchone()
    #победы
    data_wins = tbl.execute(sqlstr_wins)
    wins = data_wins.fetchone()

    # выигранные деньги
    data_win_assets = tbl.execute(sqlstr_win_assets)
    win_assets = data_win_assets.fetchone()
    # проигранные деньги
    data_loss_assets = tbl.execute(sqlstr_loss_assets)
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


def select_players():
    sqlstr = 'SELECT * FROM PLAYERSDATA'
    data = tbl.execute(sqlstr)
    rows = data.fetchall()
    # кол-во выбранных строк
    print(len(rows))
    print(rows)

def update_player_assets_abs_by_id(player_id, val):
    sqlstr = 'UPDATE PLAYERSDATA set assets_all =' + str(val) + ' WHERE player_id = ' + str(player_id)
    data = tbl.execute(sqlstr)
    assets = data.fetchone()
    # return assets
    # for row in data:
    #     print(row)


def update_player_assets_by_id_up(player_id, val):
    assets = select_player_assets_by_id(player_id)
    assets = assets + val
    sqlstr = 'UPDATE PLAYERSDATA set assets_all =' + str(assets) + ' WHERE player_id = ' + str(player_id)
    data = tbl.execute(sqlstr)
    assets = data.fetchone()
    tbl.commit()
    # return assets
    # for row in data:
    #     print(row)

def update_player_assets_plays_by_id_up(player_id, val):
    data = select_player_assets_plays_by_id(player_id)
    assets = data['assets'] + val
    plays = data['plays'] + 1
    wins = data['wins'] + 1
    win_assets = data['win_assets'] + val
    sqlstr = 'UPDATE PLAYERSDATA set assets_all=' + str(assets) +', plays_all=' + str(plays)+', plays_on=' + str(wins) +', field1=' + str(win_assets) +' WHERE player_id = ' + str(player_id)
    tbl.execute(sqlstr)
    tbl.commit()


def update_player_assets_by_id_down(player_id, val):
    assets = select_player_assets_by_id(player_id)
    assets = assets - val
    sqlstr = 'UPDATE PLAYERSDATA set assets_all =' + str(assets) + ' WHERE player_id = ' + str(player_id)
    data = tbl.execute(sqlstr)
    assets = data.fetchone()
    tbl.commit()
    # return assets
    # for row in data:
    #     print(row)

def update_player_assets_plays_by_id_down(player_id, val):
    data = select_player_assets_plays_by_id(player_id)
    assets = data['assets'] - val
    # print(str(data['plays']))
    plays = data['plays'] + 1
    # print(str(plays))
    loss_assets = data['loss_assets'] + val
    sqlstr = 'UPDATE PLAYERSDATA set assets_all =' + str(assets) +', plays_all =' + str(plays)+', field2=' + str(loss_assets) +' WHERE player_id = ' + str(player_id)
    tbl.execute(sqlstr)
    tbl.commit()

def update_player_data(player_id, val):
    assets = select_player_assets_by_id(player_id)
    assets = assets - val
    sqlstr = 'UPDATE PLAYERSDATA set assets_all =' + str(assets) + ' WHERE player_id = ' + str(player_id)
    data = tbl.execute(sqlstr)
    assets = data.fetchone()
    tbl.commit()
    # return assets
    # for row in data:
    #     print(row)

# if __name__ == '__main__':
#        tbl.execute("DROP TABLE IF EXISTS PLAYERSDATA")
#        create_table_new()

#     entities_full: [int, str , int, int, int, int, int, int, int, str , str ] = (1111, "Test", 0, 0, 0, 0, 0, 0, 0, " ", " ")
#     entities_short: [int, str , int, int, int] = (1111, "Test", 0, 0, 0)
#
#     insert_player_short(entities_short)
    # insert_player_full(entities_full)

    # select_players()
#     update_player_assets_by_id(tbl, 1, 50)
#     assets = select_player_assets_by_id(tbl, 2)
#     print(assets)
#     entities = (3, 'Den', 30, 0, 0)
#     insert_player(tbl, entities)
# select_players(tbl)
# insert_player(tbl, entities)
