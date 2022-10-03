// function test() {
//     const x = 2, y = 4;
//     // Direct call, uses local scope    
//     console.log(eval('x + y')); // Result is 6
//     console.log(eval?.('x1 + y1')); // Uses global scope, throws because x is undefined
// }
// let a = 1; 
// global['a'] = 10;
// global.clearImmediate();
// let c = eval?.("({a:(4-1), b:function(){}, c:new Date()})");

// console.log(c);

const security = (cc) => cc.match(/^.*(global|process|eval|object|charAt|-|_|{|}|function).*$/i) || cc.length > 100
console.log(security("<% x='child\x95proce' %>"))