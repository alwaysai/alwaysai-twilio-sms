var express = require('express');
var bodyParser = require('body-parser')
var app = express();
var server = require('http').Server(app);
var io = require('socket.io')(server);

app.use(express.static(__dirname));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}))

const accountSid = '';
const authToken = '';
const client = require('twilio')(accountSid, authToken);

let trigger = true

const timeout = () => {
  setTimeout(() => {
    trigger = true
  }, 20000)
}
 
io.on('connection', function (socket) {
  socket.on('labels', function (data) {
    
    console.log(data)
    
    // the twilio text only gets sent if the trigger variable is set to true
    if (trigger){
      client.messages.create({
        body: 'You see a chair',
        from: '+12000000000',
        to: '+12000000000'
      }).then(message => console.log(message.sid));

      trigger = false

      // this timeout method is defined previously. It will redefine the trigger variable as true when 20 seconds pass 
      timeout()
    }

  });
});

io.on('connection', () =>{
  console.log('a user is connected')
})

var server = server.listen(3001, () => {
  console.log('server is running on port', server.address().port);
});