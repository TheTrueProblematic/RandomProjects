function check(){
  var height = window.innerHeight;
  var width = window.innerWidth;
  if (width<height){
    location.replace("mobile.html");
  }
}

function check2(){
  var height = window.innerHeight;
  var width = window.innerWidth;
  if (width>height){
    location.replace("index.html");
  }
}
