
var slidesPerView = 5

if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Opera Mini/i.test(navigator.userAgent)) {
    // Take the user to a different screen here.
    slidesPerView = 1.5
}


const allLectorsSwiper = new Swiper('.allLectorsSwiper', {
  // Optional parameters
  direction: 'horizontal',
  loop: true,
  slidesPerView: slidesPerView,


  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  // And if we need scrollbar
  scrollbar: {
    el: '.swiper-scrollbar',
  },
});




