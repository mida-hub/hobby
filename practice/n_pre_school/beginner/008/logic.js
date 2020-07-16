// var age = 20;
// var result = null;
// if (age >= 20){
//     result = '成年';
// } else {
//     result = '未成年';
// }
// document.write(result);

var age = 65;
var isMember = true;
var result = null;
if (age >= 60 && isMember) {
    result = 'シニア会員割引の対象です';
} else {
    result = 'シニア会員割引の対象ではありません';
}
document.write(result);
