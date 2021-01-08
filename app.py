from flask import *
import requests
from flask_socketio import *
import json
import jiosaavn

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/getlink')
def getlink():
    return 'https://sklktcdnems06.cdnsrv.jio.com/jiosaavn.cdn.jio.com/872/a5ec9ece4f1f351ea48b6639313b7033_320.mp4'

@app.route('/test')
def test():
    return render_template('test.html')

@socketio.on('receiveplay')
def play():
    socketio.emit('play')

@socketio.on('receivepause')
def pause():
    socketio.emit('pause')

@socketio.on('receiveurl')
def url(data):
    print(type(data))
    print(data)
    socketio.emit('url', data)

@socketio.on('hostseeksync')
def seeksync(data):
    socketio.emit('clientseeksync', data)

@socketio.on('clientseekmove')
def seekmove(data):
    socketio.emit('hostseekmove', data)

@socketio.on('clientskipright')
def seekmove():
    socketio.emit('hostskipright')

@socketio.on('clientskipleft')
def seekmove():
    socketio.emit('hostskipleft')

@socketio.on('clientvolume')
def seekmove(data):
    socketio.emit('hostvloume', data)

@socketio.on('hostnamebroadcast')
def seekmove(data):
    socketio.emit('clientnamebroadcast', data)


@socketio.on('songsearch')
def seekmove(data):
    jsdir=jiosaavn.search_for_song(data['query'], False)
    js=[]
    for t in jsdir:
        tmp={
            'name':t['song'],
            'album':t['album'],
            'year':t['year'],
            'artist':t['primary_artists'],
            'image':t['image'],
            'url':t['media_url']
        }
        js.append(tmp)

    socketio.emit('songsearchresults', js)

@socketio.on('clientsonginfo')
def seekmove(data):
    socketio.emit('url', data['info'])
    
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80, debug=True)