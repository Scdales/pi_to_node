# socketIO-client
# https://pypi.org/project/socketIO-client/
# https://github.com/miguelgrinberg/python-socketio/blob/master/examples/client/asyncio/latency_client.py

import logging
from socketIO_client import SocketIO, LoggingNamespace

logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()

with SocketIO('localhost', 8090, LoggingNamespace) as socketIO:
    socketIO.emit('aaa')
    socketIO.wait(seconds=1)