var slidesPerView = 2

if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Opera Mini/i.test(navigator.userAgent)) {
    // Take the user to a different screen here.
    slidesPerView = 1.05

}



  var swiper = new Swiper('.mySwiper', {
    loop: true,
    slidesPerView: slidesPerView,
    spaceBetween: 10,
    scrollbar: {
      el: '.swiper-scrollbar',
      draggable: true,
    },

  });




    const container = document.querySelector('#lightgallery');
    window.lightGallery(container, {
        selector: 'a',
        hideScrollbar: true,
        plugins: [
            lgZoom
        ],
    });