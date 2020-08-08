$(function(){
  $("#btn").click(function() {
    $("h1").css("color", "#ff0000");
    $("body").css({
      "color": "red",
      "background": "#ffff00"});
  });
  $("#btn").mousedown(function() {
    $("h1").text("N高へようこそ！");
  });
  $("#btn").mouseup(function() {
    $("h1").text("Hello,World!");
  });
});