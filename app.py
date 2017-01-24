#!/usr/bin/env python
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None


def background_thread():
    """Example of how to send server generated events to clients."""
    from datetime import timedelta
    while True:
		socketio.sleep(1)	
		with open('/proc/uptime', 'r') as f:
			uptime_seconds = float(f.readline().split()[0])
			uptime_string = str(timedelta(seconds = uptime_seconds))
			uptime_string = uptime_string.split('.')[0]
			socketio.emit('uptime',{'data': uptime_string},namespace='/test')

def up_time():
	socketio.sleep(1)
	emit('my_response', {'data': '01:02:03', 'count': 0})
	
		#uptime_string = '01:01:01'
		#socketio.emit('my_response',{'data':uptime_string},namespace='/test')
	

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/raspberry_pi')
def raspberry_pi():
    return render_template('raspberry_pi.html', async_mode=socketio.async_mode)

	
@socketio.on('my_event', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})


@socketio.on('my_ping', namespace='/test')
def ping_pong():
    emit('my_pong')


@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app, debug=False,host='0.0.0.0',port=80)
