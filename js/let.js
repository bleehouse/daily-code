function es5() {
  var i;
  for (i = 0; i < 10; i += 1) {
    (function () {
      var i = 10;
      var i = i + 1;
      console.log(i);
    })();
  }
}

es5();

// function es6() {
//   for (let i = 0; i < 10; i += 1) {    
//     (function () {
//       let i = 10;
//       let i = i + 1; // syntax error because of redeclaration of i
//       console.log(i);
//     })();
//   }
// }

// es6();

//       let i = i + 1; // syntax error because of redeclaration of i
//                   ^
// SyntaxError: Identifier 'i' has already been declared
//     at Object.exports.runInThisContext (vm.js:78:16)
//     at Module._compile (module.js:545:28)
//     at Object.Module._extensions..js (module.js:582:10)
//     at Module.load (module.js:490:32)
//     at tryModuleLoad (module.js:449:12)
//     at Function.Module._load (module.js:441:3)
//     at Module.runMain (module.js:607:10)
//     at run (bootstrap_node.js:420:7)
//     at startup (bootstrap_node.js:139:9)
//     at bootstrap_node.js:535:3