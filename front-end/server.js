const express = require('express')
const app = express()

app.use(express.static(__dirname + '/dist/'))

app.get('/', function(req, res) {
    res.sendfile(__dirname + '/dist/index.html')
})

app.listen(3000, function() {
    console.log('Servidor Web rodando')
})