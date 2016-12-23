//  only in ES5 through the help of object properties
//  and only in global context and not in a block scope
// Object.defineProperty(typeof global === "object" ? global : window, "PI", {
//     value:        3.141593,
//     enumerable:   true,
//     writable:     false,
//     configurable: false
// })

const PI = 3.141593

console.log(PI);