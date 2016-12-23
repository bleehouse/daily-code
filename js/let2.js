function es6() {
    let i = 99999;
  for (let j = 0; j < 10; j += 1) {
      let i = 88888;
    (function () {
        let i = 77777;
      console.log(i); // 0 to 9
    //   {
    //     console.log(i); // syntax error
    //     let i = 10;
    //   }
    })();
  }
}

 es6();