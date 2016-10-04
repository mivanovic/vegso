//jQuery to collapse the navbar on scroll
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
        $(".img-brand").addClass("img-brand-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
        $(".img-brand").removeClass("img-brand-collapse");
    }
});

//jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);

        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - 70
        }, 1500, 'easeInOutExpo');
        console.log($($anchor.attr('href')).offset().top);
        event.preventDefault();
    });
});
