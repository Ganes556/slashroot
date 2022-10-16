import mongoose from "mongoose";
mongoose.pluralize(null);

export default (() => {    
    return mongoose.createConnection( 
        "mongodb://root:8c18e23138bc5240468600b2a646bda2958303d7c69bdfed94@mongo:27018/app?connectTimeoutMS=1000&authSource=admin",
        (err) => (!err) ? console.log("sukses") : console.log('error',err))
})()