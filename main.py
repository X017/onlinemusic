from bottle import *  
import sqlite3 
import os 



db = sqlite3.connect("testdb.db")

cur = db.cursor()


@route('/play')
def get_music():
    return template('play.tpl')

@route('/play',method='POST')
def play_music():
    pass

@route('/list')
def music_list():
    db_list = cur.execute('SELECT * FROM music')
    return template('music_list',music=db_list.fetchall())
@route('/update')
def list_update():
    cur.execute('DELETE FROM music;')
    for m in os.listdir('music'):
        if '.mp3' in m:
            cur.execute(f'INSERT INTO music(name) VALUES ("{m}")')
    db.commit()
debug(True)
run(host='localhost',port=8000)


