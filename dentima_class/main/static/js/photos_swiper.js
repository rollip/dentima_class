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

  lightGallery(document.getElementById('lightgallery'), {
    selector: 'a',
    hideScrollbar: true,
    plugins: [lgZoom, lgThumbnail],
    speed: 500,
    thumbnail: true,
  });