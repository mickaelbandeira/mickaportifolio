<template>
  <div class="edrea_tm_section" id="about">
    <div class="section_inner">
      <div class="edrea_tm_about">
        <div class="left">
          <div class="image">
            <img src="img/thumbs/1-1.jpg" alt="" />
            <div
              class="main"
              :style="{ backgroundImage: 'url(img/about/micka.png)' }"
            ></div>
          </div>
        </div>
        <div class="right">
          <div class="short">
            <h3 class="name">Micka <span class="coloring">Bandeira</span></h3>
            <h3 class="job">
              <AnimationText />
            </h3>
          </div>
          <div class="text">
            <p>
              Unindo 9 anos de experiência em Design à Engenharia de IA. Desenvolvo automações inteligentes e interfaces que conectam estética, funcionalidade e tecnologia de ponta.
            </p>
          </div>
          <div class="edrea_tm_button" id="aboutPopup">
            <a href="#">Saiba Mais</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AnimationText from "./AnimationText.vue";
export default {
  name: `AboutComponent`,
  data() {
    return {
      open: false,
    };
  },
  components: {
    AnimationText,
  },
};
</script>

<style scoped>
.edrea_tm_modalbox {
  top: -90px;
}
</style>
