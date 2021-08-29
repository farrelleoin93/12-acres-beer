$( document ).ready(function() {
    $("#details-button").click(function(){
        $("#details").css("display", "block");
        $("#orders").css("display", "none");
    });
    
    $("#orders-button").click(function(){
        $("#details").css("display", "none");
        $("#orders").css("display", "block");
  });
});