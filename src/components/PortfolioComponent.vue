<template>
  <div class="edrea_tm_section" id="portfolio">
    <div class="section_inner">
      <div class="edrea_tm_portfolio swiper-section">
        <div class="edrea_tm_main_title">
          <h3>Portfólio <span class="coloring">Criativo</span></h3>
        </div>
        <div class="portfolio_list gallery_zoom">
          <swiper
            :loop="false"
            :slidesPerView="1"
            :spaceBetween="0"
            :loopAdditionalSlides="1"
            :autoplay="{
              delay: 6000,
            }"
            :navigation="{
              nextEl: '.my_next',
              prevEl: '.my_prev',
            }"
            :pagination="pagination"
            :breakpoints="{
              700: {
                slidesPerView: 2,
                spaceBetween: 20,
              },
              1200: {
                slidesPerView: 3,
                spaceBetween: 30,
              },
            }"
            @slideChange="onSlideChange"
            :modules="modules"
            class="swiper-container"
          >
            <swiper-slide class="swiper-slide">
              <div class="list_inner">
                <div class="image">
                  <img src="img/thumbs/1-1.jpg" alt="" />
                  <div
                    class="main"
                    :style="{ backgroundImage: 'url(img/portfolio/consulttymed_final.png)', backgroundSize: 'contain', backgroundRepeat: 'no-repeat', backgroundColor: '#fff', backgroundPosition: 'center' }"
                  ></div>
                </div>
                <div class="details">
                  <h3>Consulttymed</h3>
                  <span>Ver Projeto</span>
                </div>
                <a
                  class="edrea_tm_full_link"
                  href="https://www.instagram.com/consulttymed/"
                  target="_blank"
                ></a>
              </div>
            </swiper-slide>
            <swiper-slide class="swiper-slide">
              <div class="list_inner">
                <div class="image">
                  <img src="img/thumbs/1-1.jpg" alt="" />
                  <div
                    class="main"
                    :style="{ backgroundImage: 'url(img/portfolio/new_logo_2.png)', backgroundSize: 'contain', backgroundRepeat: 'no-repeat', backgroundColor: '#fff', backgroundPosition: 'center' }"
                  ></div>
                </div>
                <div class="details">
                  <h3>Blog do Bina</h3>
                  <span>Ver Projeto</span>
                </div>
                <a
                  class="edrea_tm_full_link"
                  href="https://www.blogdobina.com"
                  target="_blank"
                ></a>
              </div>
            </swiper-slide>
            <swiper-slide class="swiper-slide">
              <div class="list_inner">
                <div class="image">
                  <img src="img/thumbs/1-1.jpg" alt="" />
                  <div
                    class="main"
                    :style="{ backgroundImage: 'url(img/portfolio/new_logo_1.png)', backgroundSize: 'contain', backgroundRepeat: 'no-repeat', backgroundColor: '#fff', backgroundPosition: 'center' }"
                  ></div>
                </div>
                <div class="details">
                  <h3>Tecla1</h3>
                  <span>Ver Projeto</span>
                </div>
                <a
                  class="edrea_tm_full_link"
                  href="https://www.tecla1.com.br"
                  target="_blank"
                ></a>
              </div>
            </swiper-slide>
             <swiper-slide class="swiper-slide">
              <div class="list_inner">
                <div class="image">
                  <img src="img/thumbs/1-1.jpg" alt="" />
                  <div
                    class="main"
                    :style="{ backgroundImage: 'url(img/portfolio/new_logo_3.png)', backgroundSize: 'contain', backgroundRepeat: 'no-repeat', backgroundColor: '#fff', backgroundPosition: 'center' }"
                  ></div>
                </div>
                <div class="details">
                  <h3>Arapiraca News</h3>
                  <span>Ver Projeto</span>
                </div>
                <a
                  class="edrea_tm_full_link"
                  href="https://www.arapiracanews.com.br"
                  target="_blank"
                ></a>
              </div>
            </swiper-slide>
             <swiper-slide class="swiper-slide">
              <div class="list_inner">
                <div class="image">
                  <img src="img/thumbs/1-1.jpg" alt="" />
                  <div
                    class="main"
                    :style="{ backgroundImage: 'url(img/portfolio/urbanisme_port.png)', backgroundSize: 'contain', backgroundRepeat: 'no-repeat', backgroundColor: '#fff', backgroundPosition: 'center' }"
                  ></div>
                </div>
                <div class="details">
                  <h3>Urbanisme</h3>
                  <span>Ver Projeto</span>
                </div>
                <a
                  class="edrea_tm_full_link"
                  href="https://www.instagram.com/construtoraurbanisme/"
                  target="_blank"
                ></a>
              </div>
            </swiper-slide>
            <div class="edrea_tm_swiper_progress fill">
              <div class="my_pagination_in">
                <span class="current">0</span>
                <span class="pagination_progress"
                  ><span class="all"
                    ><span
                      style="
                        transform: translate3d(0px, 0px, 0px) scaleX(0.75)
                          scaleY(1);
                      "
                    ></span></span
                ></span>
                <span class="total">04</span>
              </div>
              <div class="my_navigation">
                <ul>
                  <li>
                    <a class="my_prev" href="#"
                      ><i class="icon-left-open-1"></i
                    ></a>
                  </li>
                  <li>
                    <a class="my_next" href="#"
                      ><i class="icon-right-open-1"></i
                    ></a>
                  </li>
                </ul>
              </div>
            </div>
          </swiper>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import Swiper core and required modules

// Import Swiper Vue.js components
import { Navigation, Pagination } from "swiper";
import { Swiper, SwiperSlide } from "swiper/vue";
import { swiperSliderCustomSlider, dataImage } from "../utilits";

export default {
  name: `PortfolioComponent`,
  components: {
    Swiper,
    SwiperSlide,
  },
  methods: {
    onSlideChange(swiper) {
      this.activeSlider = swiper.activeIndex + 1;
    },
  },
  mounted() {
    dataImage();
  },
  setup() {
    return {
      modules: [Navigation, Pagination],
      pagination: {
        el: ".edrea_tm_swiper_progress",
        type: "custom", // progressbar
        renderCustom: function (swiper, current, total) {
          swiperSliderCustomSlider(current, total);
        },
      },
    };
  },
};
</script>
