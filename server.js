var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);

server.listen(80);
// WARNING: app.listen(80) will NOT work here!

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index2.html');
});

io.on('connection', function (socket) {
  console.log('Client connected');
  socket.emit('news', { hello: 'world' });

  socket.on('my other event', (data) => {
    console.log(data);
  });

  socket.on('ping_from_client', (data) => {
    console.log('Received:', data);
    socket.emit('pong_from_server', {data : 'something'});
  });
});

