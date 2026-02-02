<template>
  <ul class="transition_link">
    <li :class="navFuntions.activeNavCls('home')">
      <a href="#home" @click="navFuntions.activeSection('home')">Início</a>
    </li>
    <li :class="navFuntions.activeNavCls('about')">
      <a href="#about" @click="navFuntions.activeSection('about')">Sobre</a>
    </li>
    <li :class="navFuntions.activeNavCls('portfolio')">
      <a href="#portfolio" @click="navFuntions.activeSection('portfolio')"
        >Portfólio</a
      >
    </li>
    <li :class="navFuntions.activeNavCls('news')">
      <a href="#news" @click="navFuntions.activeSection('news')">AeC</a>
    </li>
    <li :class="navFuntions.activeNavCls('contact')">
      <a href="#contact" @click="navFuntions.activeSection('contact')"
        >Contato</a
      >
    </li>
  </ul>
</template>

<script>
import { navFuntions } from "@/navFuntions";
export default {
  name: `Menu`,
  data() {
    return {
      navFuntions,
    };
  },
};
</script>
