<template>
  <MobileHeaderComponent />
  <!-- Header -->
  <div class="edrea_tm_header">
    <div class="header_inner">
      <div class="logo">
        <a href="#" @click="navFuntions.activeSection('home')" style="text-decoration: none;">
          <h3 style="color: #a2a2a2; font-size: 25px; font-weight: 600; font-family: 'Poppins'; margin-bottom: 0;">Micka <span style="color: #fff; font-weight: 700;">Bandeira</span></h3>
        </a>
      </div>
      <div class="menu">
        <Menu />
      </div>
    </div>
  </div>
</template>

<script>
import { navFuntions } from "@/navFuntions";
import Menu from "./Menu.vue";
import MobileHeaderComponent from "./MobileHeaderComponent.vue";
export default {
  name: `HeaderComponent`,
  components: { MobileHeaderComponent, Menu },
  data() {
    return {
      navFuntions,
    };
  },
};
</script>
