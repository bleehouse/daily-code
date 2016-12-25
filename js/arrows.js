// http://seokjun.kr/ecmascript-6-features/#arrows

var evens = [2, 4, 6, 8, 10, 12];

console.log("evens : " + evens);

// Expression bodies
var odds = evens.map(v => v + 1);

console.log("odds : " + odds);

var nums = evens.map((v, i) => v + i);  

console.log("nums : " + nums);

var pairs = evens.map(v => ({even: v, odd: v + 1}));

console.log("---- pairs ----");
console.log(pairs);

var fives = [];

// Statement bodies
nums.forEach(v => {  
  if (v % 5 === 0)
    fives.push(v);
});

console.log("fives : " + fives);

// Lexical this
var bob = {  
  _name: "Bob",
  _friends: [],
  printFriends() {
    this._friends.forEach(f =>
      console.log(this._name + " knows " + f));
  }
}

console.log(bob);

bob._friends.push("tom");
bob._friends.push("jane");

bob.printFriends();


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