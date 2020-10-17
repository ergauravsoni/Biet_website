(function ($) {
    "use strict";

    jQuery(document).ready(function ($) {


        $(".embed-responsive iframe").addClass("embed-responsive-item");
        $(".carousel-inner .item:first-child").addClass("active");

        $('[data-toggle="tooltip"]').tooltip();


        (function ($) {

            var allPanels = $('.single_faq > p').hide();

            $('.single_faq > h3 > i').click(function () {
                allPanels.slideUp();
                $(this).parent().next().slideDown();
                return false;
            });

        })(jQuery);

        //Owl carusel slider....
        $('.slider_bottom').owlCarousel({
            loop: true,
            autoplay: true,
            nav: true,
            navText: ['<i class="fa fa-angle-double-left"></i>', '<i class="fa fa-angle-double-right"></i>'],
            margin: 10,
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 3
                },
                1000: {
                    items: 6
                }
            }
        });

        //Responsive Mobile Menu....
        $('#mobile_menu').slicknav();

        jQuery('.tp-banner').revolution({
            delay: 9000,
            startwidth: 1170,
            startheight: 500,
            hideThumbs: 10
        });

    });
	
jQuery(window).load(function(){

    $("#preloader").fadeOut(500);
    
});	




}(jQuery));

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
  var i;
  var vid=document.getElementsByTagName("VIDEO");
  for (i = 0; i < vid.length; i++) {
      vid[i].pause();
  }
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
  var i;
  var vid=document.getElementsByTagName("VIDEO");
  for (i = 0; i < vid.length; i++) {
      vid[i].pause();
  }
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var autoSlides = document.getElementsByClassName("autoSlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  if(autoSlides.length>0){
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  if(slides.length>0){
    slides[slideIndex-1].style.display = "block";
    if(dots.length>0){
      dots[slideIndex-1].className += " active";
    }
  }
  if(autoSlides.length>0){
    setTimeout(showSlides, 5000);
  }
}
