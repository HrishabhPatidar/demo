window.onload=function(){


    $(window).scroll(function(){
        var scrollTop = 0;
        scrollTop = $(window).scrollTop();


        if (scrollTop >= 100) {

            $('#top, #navbar').addClass('header-background-f').removeClass('header-background-i');
            $('#navbar').css({'border-color':'rgba(67 , 79, 83, 0)','background-color':'rgba(67 , 79, 83, .0)'});
            $('#top').css({'min-height':'70px'});
            $('#logo').addClass('logo_resize'); } else if (scrollTop < 100) {
            $('#top, #navbar').removeClass('header-background-f').addClass('header-background-i');
            $('#logo').removeClass('logo_resize');
        }


        $('#navbar').css({'border-color':'transparent'})
    });



    $('#photos').click(function(){
        $('#bigphoto').fadeIn();



    });


    /*
        $(' html , body').on('click',function(){
            $('#hidden_meu').css({'display':'none'});
        });
    $('#navbar').on('click', function(){
       $('#hidden_meu').css({'display':'block','visibility':'visible'})
    });

        $('#dot').on('mouseover' ,function()
        {
            //$('#dot_size').css({  'margin':'-22px 0px 0px 34px', 'transform':'rotate(90deg)'}).delay(4000);
            //$('#hidden_menu').slideDown('fast')
            $('#hidden_menu').css({'display':'block'});


            $('#hidden_menu').on('mouseover ' , function()
            {
                //$('#hidden_menu').slideDown('slow')
                $('#hidden_menu').css({'display':'block'});

                //$('#dot_size').delay(200).css({  'margin':'-15px 0px 0px 30px', 'transform':'rotate(90deg)'});


            });

        });
        /*
        $('#hidden_menu').on('mouseleave' , function()
        {
            $('#hidden_menu').css({'display':'none'});



            $('#dot').on('mouseleave' , function()
            {
                $('#hidden_menu').css({'display':'none'});


                // $('#dot_size').css({'transform':'rotate(0deg)','margin':'-30px 0px 0px 7px'});
            }); });


    */
    (function() {

  'use strict';

  // define variables
  var items = document.querySelectorAll(".timeline li");

  // check if an element is in viewport
  // http://stackoverflow.com/questions/123999/how-to-tell-if-a-dom-element-is-visible-in-the-current-viewport
  function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }

  function callbackFunc() {
    for (var i = 0; i < items.length; i++) {
      if (isElementInViewport(items[i])) {
        items[i].classList.add("in-view");
      }
    }
  }

  // listen for events
  window.addEventListener("load", callbackFunc);
  window.addEventListener("resize", callbackFunc);
  window.addEventListener("scroll", callbackFunc);

})();
    $('#media').carousel({
        pause: true,
        interval: false,
    });

    $('#donate , #mission, #volunteer, #work').on('mouseover', function(){
        $(this).css({'transform':'rotateY(180deg)'});

    });
    $('#donate , #mission, #volunteer, #work').on('mouseleave', function(){
        $(this).css({'transform':'rotateY(0deg)'});

    });

    $('#sponsor , #ngo_volunteer , #campus_volunteer , #rulesm , #campaign , #donation ,#books , #stationary , #raddi , #clothes ,#fund').css({'background':'rgb(Math.floor(Math.random() * 250),Math.floor(Math.random() * 250),Math.floor(Math.random() * 250)'})

    ;

    $('#prev').bind('click', function () {
        carousel.prev();
        return false
    });

    $('#next').bind('click', function () {
        carousel.next();
        return false;
    });

    $('#reload').bind('click', function () {
        newOptions = eval("(" + $('#newoptions').val() + ")");
        carousel.reload(newOptions);
        return false;
    });




};