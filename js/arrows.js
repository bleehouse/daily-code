// Expression bodies
var odds = evens.map(v => v + 1);  
var nums = evens.map((v, i) => v + i);  
var pairs = evens.map(v => ({even: v, odd: v + 1}));

// Statement bodies
nums.forEach(v => {  
  if (v % 5 === 0)
    fives.push(v);
});

// Lexical this
var bob = {  
  _name: "Bob",
  _friends: [],
  printFriends() {
    this._friends.forEach(f =>
      console.log(this._name + " knows " + f));
  }
}

// // Expression bodies
// var odds = evens.map(function (v) {  
//   return v + 1;
// });
// var nums = evens.map(function (v, i) {  
//   return v + i;
// });
// var pairs = evens.map(function (v) {  
//   return { even: v, odd: v + 1 };
// });

// // Statement bodies
// nums.forEach(function (v) {  
//   if (v % 5 === 0) fives.push(v);
// });

// // Lexical this
// var bob = {  
//   _name: "Bob",
//   _friends: [],
//   printFriends: function printFriends() {
//     var _this = this;

//     this._friends.forEach(function (f) {
//       return console.log(_this._name + " knows " + f);
//     });
//   }
// };