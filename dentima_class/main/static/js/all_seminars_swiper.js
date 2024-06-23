var slidesPerView = 4
var rows = 2

if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Opera Mini/i.test(navigator.userAgent)) {
    // Take the user to a different screen here.
    slidesPerView = 1.3
    rows = 1

}


const allSeminarsSwiper = new Swiper('.allSeminarsSwiper',  {
     slidesPerView: slidesPerView,
          grid: {
            rows: rows,
            fill: 'row',
          },
          spaceBetween: 0,

          // And if we need scrollbar
        scrollbar: {
        el: '.swiper-scrollbar',
        },
    })





