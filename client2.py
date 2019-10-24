import asyncio
import time
import socketio

loop = asyncio.get_event_loop()
sio = socketio.AsyncClient()
start_timer = None


async def send_ping():
    global start_timer
    start_timer = time.time()
    await sio.emit('ping_from_client', {"foo" : 'bar'})


@sio.event
async def connect():
    print('connected to server')
    print('my sid is', sio.sid)
    await send_ping()


@sio.event
async def pong_from_server(data):
    global start_timer
    latency = time.time() - start_timer
    print('latency is {0:.2f} ms'.format(latency * 1000))
    print('Received:', data)
    await sio.sleep(1)
    await send_ping()


async def start_server():
    await sio.connect('http://localhost:80')
    await sio.wait()


if __name__ == '__main__':
    loop.run_until_complete(start_server())