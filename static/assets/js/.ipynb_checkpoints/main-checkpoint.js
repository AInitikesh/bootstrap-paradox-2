
$("#start-button").click(function(){
  $("#main-image").attr("src", "/stream_data");
});

$("#stop-button").click(function(){
  $("#main-image").attr("src", "assets/img/icon.png");
});

$('#file-upload').on('submit', function(e){
    // validation code here
    if(!valid) {
      e.preventDefault();
    }
  });