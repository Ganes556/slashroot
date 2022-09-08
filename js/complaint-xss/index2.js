import express, { request } from "express";
import cookieParser from "cookie-parser";

const app = express()

app.use(cookieParser())
app.use(express.json())

app.get("/",(req,res) => {        
    console.log(req.query);
    res.send(req.query);
})
app.listen(4000,() => console.log("listen 4000"))