// 2000年1月1日0時0分 月のみ0からスタート
var myBirthTime = new Date(2000, 0, 1, 0, 0);
function updateParagraph(){
    var now = new Date();
    var seconds = (now.getTime() - myBirthTime.getTime()) / 1000;
    document.getElementById('birth-time').innerHTML =
        '生まれてから' + seconds + '秒経過。';
}

setInterval(updateParagraph, 1000);