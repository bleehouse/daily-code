//matrix.js header

var matrix = [1,0,1,2,3,4,5,6,7,8,9,10,11,12];
var row = "";
for(var i=0; i<matrix.length; i++){
    for(var j=0; j<matrix.length; j++){
        if (i ==0 && j==0) {
            row = row +  " ";
        } else {
            row = row + matrix[i] * matrix[j] + " ";
        }
        
    }
    row = row + "\r\n";
    console.log(row);
    row = "";
}
