from bottle import *  
import sqlite3 
import os 



db = sqlite3.connect("testdb.db")

cur = db.cursor()


@route('/play')
def get_music():
    return '''
     <form action="/play" method="post">
            Music: <input name="music_name" type="text" />
            <input value="Login" type="submit" />
        </form>
        <iframe src="http://localhost:8000/list"  height="500px" width="600px"></iframe>
'''
    
@route('/play',method='POST')
def play_music():
    os.chdir('/home/parsa/projects/test/music')
    wp_music = request.forms.get('music_name')
    mixer.music.load(wp_music)
    mixer.music.play()

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
@route('/volume')
def play_volume():
    volume = mixer.music.get_volume()
    return f"mixer volume is {volume}"
    
debug(True)
reloader(True)
run(host='localhost',port=8000)


