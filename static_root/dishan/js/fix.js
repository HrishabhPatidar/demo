window.onload=function(){

    var scrollTop = 0;
    $(window).scroll(function(){
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
    var carousel = $("#carousel").waterwheelCarousel({
        flankingItems: 3,
        movingToCenter: function ($item) {
            $('#callback-output').prepend('movingToCenter: ' + $item.attr('id') + '<br/>');
        },
        movedToCenter: function ($item) {
            $('#callback-output').prepend('movedToCenter: ' + $item.attr('id') + '<br/>');
        },
        movingFromCenter: function ($item) {
            $('#callback-output').prepend('movingFromCenter: ' + $item.attr('id') + '<br/>');
        },
        movedFromCenter: function ($item) {
            $('#callback-output').prepend('movedFromCenter: ' + $item.attr('id') + '<br/>');
        },
        clickedCenter: function ($item) {
            $('#callback-output').prepend('clickedCenter: ' + $item.attr('id') + '<br/>');
        }
    });

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