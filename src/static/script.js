$(document).ready(function(){

    var isMenuOpened = false;
    $(".menu-icon").click(function(){
        if(isMenuOpened){
            $(".menu-icon").removeClass("active")
            $("body").removeClass("open-menu")
        }
        else{
            $(".menu-icon").addClass("active")
            $("body").addClass("open-menu")
        }
        isMenuOpened = !isMenuOpened
    })

})

$(document).ready(function() {
    $(".menu-btn").click(function(e) {
      e.preventDefault();
      $(this).find("ul").slideToggle();
      $(this).toggleClass("salam")
    });
  });