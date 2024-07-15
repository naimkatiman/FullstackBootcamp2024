const express = require('express')
const app = express()
const port = 8080

app.get('/',(req,res) => {
    res.send('This is a Node app for CICD')
})

app.listen(port, () =>{
    console.log(`App is listening at http://localhost:${port}`)

})
