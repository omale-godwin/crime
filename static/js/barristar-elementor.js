/*
Template Name: Barristar
Author: wpoceans
Version: 1.0
Email: support@wpocean.com
*/

(function($){
'use strict';

/*----- ELEMENTOR LOAD FUNTION CALL ---*/

$( window ).on( 'elementor/frontend/init', function() {

	var hero_slider = function(){

	  if ($(".hero-slider").length) {
            $(".hero-slider").not('.slick-initialized').slick({
                autoplay: true,
                autoplaySpeed: 8000,
                pauseOnHover: true,
                arrows: true,
                prevArrow: '<button type="button" class="slick-prev">Previous</button>',
                nextArrow: '<button type="button" class="slick-next">Next</button>',
                dots: true,
                fade: true,
                cssEase: 'linear',
            });
        }

	}; // end

    var sliderBgSetting = function(){

       if ($(".hero-slider .slide").length) {
            $(".hero-slider .slide").each(function() {
                var $this = $(this);
                var img = $this.find(".slider-bg").attr("src");

                $this.css({
                    backgroundImage: "url("+ img +")",
                    backgroundSize: "cover",
                    backgroundPosition: "center center"
                })
            });
        }

    }; // end

    var testimonial = function(){

        /*------------------------------------------
            = TESTIMONIALS SLIDER
        -------------------------------------------*/
        if($(".testimonial-slide".length)) {
            $(".testimonial-slide").owlCarousel({
                mouseDrag: false,
                smartSpeed: 1500,
                margin: 30,
                loop:true,
                items: 1
            });
        }


    }; // end

    var odometer = function(){

        /*------------------------------------------
            = FUNFACE
        -------------------------------------------*/
        if ($(".odometer").length) {
            $('.odometer').appear();
            $(document.body).on('appear', '.odometer', function(e) {
                var odo = $(".odometer");
                odo.each(function() {
                    var countNumber = $(this).attr("data-count");
                    $(this).html(countNumber);
                });
            });
        }



    }; // end

    var expert_active = function(){

        if ($(".expert-active").length) {
          var $carousel = $('.expert-active');
          var $items = ($carousel.data("items") !== undefined) ? $carousel.data("items") : 3;
        $(".expert-active").owlCarousel({
            smartSpeed: 500,
            margin: 5,
            loop:true,
            autoplayHoverPause:true,
            dots: false,
            items: $items,
            autoplay : ($carousel.data("autoplay") !== undefined) ? $carousel.data("autoplay") : false,
            nav:  ($carousel.data("nav") !== undefined) ? $carousel.data("nav") : true,
            navText: ['<i class="ti-angle-left"></i>','<i class="ti-angle-right"></i>'],
             responsive: {
                0 : {
                    items: 1
                },

                550 : {
                    items: 2
                },

                992 : {
                    items: $items,
                }
            }
        });
    }




    }; // end


	//Slider
	elementorFrontend.hooks.addAction( 'frontend/element_ready/wpo-barristar_slider.default', function($scope, $){
		hero_slider();
	} );

    //Slide BG
    elementorFrontend.hooks.addAction( 'frontend/element_ready/wpo-barristar_slider.default', function($scope, $){
        sliderBgSetting();
    } );

    //Testimonial
    elementorFrontend.hooks.addAction( 'frontend/element_ready/wpo-barristar_testimonial.default', function($scope, $){
        testimonial();
    } );

    //odometer
    elementorFrontend.hooks.addAction( 'frontend/element_ready/wpo-barristar_funfact.default', function($scope, $){
        odometer();
    } );
	
    //odometer
    elementorFrontend.hooks.addAction( 'frontend/element_ready/wpo-barristar_attorney.default', function($scope, $){
        expert_active();
    } );

    


	
	
	
} );


})(jQuery);  