$(document).ready(function(){
    $(window).bind("resize", resizeWindow);
        function resizeWindow(e){
            var newWindowWidth = $(window).width();
            // Если ширина меньше 600 px, используется таблица стилей для мобильного
            if(newWindowWidth < 600){
                $("link[rel=stylesheet]").attr({href : "/static/hrumshop/css/styles_mobile.css"});
            } else if(newWindowWidth > 600){
            // Если ширина больше 600 px, используется таблица стилей для десктопа
                $("link[rel=stylesheet]").attr({href : "/static/hrumshop/css/styles_desktop.css"});
            }
        }
});

