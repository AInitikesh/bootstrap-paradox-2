
$("#start-button").click(function(){
  $("#main-image").attr("src", "/stream_data");
});

$("#stop-button").click(function(){
  $("#main-image").attr("src", "");
});

$('#file-upload').on('submit', function(e){
    // validation code here
    if(!valid) {
      e.preventDefault();
    }
  });

$(".dropdown-menu a").click(function(){
  var selText = $(this).text();
  var model_number = 1
    if (selText == "Deep Lab"){
        model_number = 1
    }
    
    if (selText == "MobileNetV2"){
        model_number = 2
    }
    
    if (selText == "MobileNetV2 Lite"){
        model_number = 3
    }
        
  $.get( "change_model?model_number=" + model_number, function( data ) {});
  $(this).parents('.container').find('.dropdown-toggle').html(selText+' <span class="caret"></span>');
});