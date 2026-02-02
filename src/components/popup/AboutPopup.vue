<template>
  <div class="edrea_tm_modalbox" :class="open ? 'opened' : ''">
    <div class="box_inner">
      <div class="close">
        <a href="#" @click="close"><i class="icon-cancel"></i></a>
      </div>
      <div class="description_wrap">
        <div class="about_popup_details">
          <div class="left">
            <div class="left_inner">
              <div class="author">
                <div class="avatar_image">
                  <img src="img/thumbs/1-1.jpg" alt="" />
                  <div
                    class="main"
                    :style="{ backgroundImage: 'url(img/about/popup_avatar.png)' }"
                  ></div>
                </div>
                <div class="short">
                  <h3 class="name">
                    {{ aboutData.firstName }}
                    <span class="coloring">{{ aboutData.lastName }}</span>
                  </h3>
                  <h3 class="job">
                    <AnimationText />
                  </h3>
                </div>
              </div>
              <div class="list">
                <ul>
                  <li>
                    <div class="list_inner">
                      <i class="icon-user"></i>
                      <span
                        >{{ aboutData.firstName }}
                        {{ aboutData.lastName }}</span
                      >
                    </div>
                  </li>
                  <li>
                    <div class="list_inner">
                      <i class="icon-calendar"></i>
                      <span>{{ aboutData.bithday }}</span>
                    </div>
                  </li>
                  <li>
                    <div class="list_inner">
                      <i class="icon-location"></i>
                      <span
                        ><a href="#" class="href_location">{{
                          aboutData.address
                        }}</a></span
                      >
                    </div>
                  </li>
                  <li>
                    <div class="list_inner">
                      <i class="icon-phone"></i>
                      <span
                        ><a href="#">{{ aboutData.phn }}</a></span
                      >
                    </div>
                  </li>
                  <li>
                    <div class="list_inner">
                      <i class="icon-mail-1"></i>
                      <span
                        ><a :href="`mailto:${aboutData.email}`">{{
                          aboutData.email
                        }}</a></span
                      >
                    </div>
                  </li>
                </ul>
              </div>
              <div class="edrea_tm_button full">
                <a href="https://wa.me/5582996004382" target="_blank">Fale comigo</a>
              </div>
            </div>
          </div>
          <div class="right">
            <div class="right_inner">
              <div class="biography">
                <div class="about_title">
                  <h3>
                    <span>Sobre <span class="coloring">Mim</span></span>
                  </h3>
                </div>
                <div class="text">
                  <p>
                    Meu nome é <span>Micka Bandeira</span> e minha jornada sempre foi sobre comunicar ideias. Começou com o Design Gráfico e a Diagramação, onde passei 9 anos refinando o olhar visual. Hoje, levo essa bagagem para o mundo da Programação e IA. Acredito que a tecnologia deve ser inteligente, mas também humana. Por isso, desenvolvo automações e sistemas focados em otimizar o tempo e potencializar resultados, sem nunca abrir mão da experiência do usuário.
                  </p>
                </div>
              </div>
              <div class="service">
                <div class="about_title">
                  <h3>
                    <span>Cursos e <span class="coloring">Tecnologias</span></span>
                  </h3>
                </div>
                <div class="list">
                  <ul>
                    <li v-for="(service, i) in aboutData.serviceLists" :key="i">
                      <i class="icon-right-dir"></i>{{ service }}
                    </li>
                  </ul>
                </div>
              </div>
              <div class="prog_skill">
                <div class="about_title">
                  <h3>
                    <span
                      >Habilidades de <span class="coloring">Programação</span></span
                    >
                  </h3>
                </div>
                <div class="programming_skills_list" style="margin-top: 20px;">
                  <div
                    class="skill_item"
                    v-for="(skill, i) in aboutData.skills.programming"
                    :key="i"
                    style="margin-bottom: 20px; padding-bottom: 10px; border-bottom: 1px dashed rgba(255,255,255,0.1);"
                  >
                    <h5 style="margin: 0; font-size: 16px; color: #fff; font-family: 'Poppins'; font-weight: 600;">{{ skill.name }}</h5>
                    <p style="margin: 5px 0 0 0; font-size: 15px; color: #a2a2a2; font-family: 'Mulish'; line-height: 1.5;">{{ skill.value }}</p>
                  </div>
                </div>
              </div>
              <div class="lang_skill">
                <div class="about_title">
                  <h3>
                    <span>Habilidades <span class="coloring">Linguísticas</span></span>
                  </h3>
                </div>
                <div class="circular_progress_bar">
                  <ul>
                    <li>
                      <div class="list_inner">
                        <div class="myCircle" data-value="1.0"></div>
                        <div class="title"><span>Português</span></div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
              <div class="timeline">
                <div class="about_title">
                  <h3>
                    <span
                      >Formação <span class="coloring">Acadêmica</span></span
                    >
                  </h3>
                </div>
                <div class="list">
                  <ul>
                    <li v-for="(edu, i) in aboutData.education" :key="i">
                      <div class="list_inner">
                        <div class="time">
                          <span>{{ edu.year }}</span>
                        </div>
                        <div class="place">
                          <h3>{{ edu.unv }}</h3>
                          <span>{{ edu.degree }}</span>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
              <div class="timeline">
                <div class="about_title">
                  <h3>
                    <span>Experiência <span class="coloring">Profissional</span></span>
                  </h3>
                </div>
                <div class="list">
                  <ul>
                    <li v-for="(work, i) in aboutData.working" :key="i">
                      <div class="list_inner">
                        <div class="time">
                          <span>{{ work.year }}</span>
                        </div>
                        <div class="place">
                          <h3>{{ work.company }}</h3>
                          <span>{{ work.deg }}</span>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
              <div class="partners">
                <div class="about_title">
                  <h3>
                    <span>Meus <span class="coloring">Parceiros</span></span>
                  </h3>
                </div>
                <div class="list">
                  <ul>
                    <li v-for="(partner, i) in aboutData.partnersLogos">
                      <div class="list_inner">
                        <img :src="partner" alt="" />
                        <a class="cavani_tm_full_link" href="#"></a>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
              <div class="testimonial">
                <div class="about_title">
                  <h3>
                    <span>Feedback de <span class="coloring">Clientes</span></span>
                  </h3>
                </div>
                <div class="list">
                  <swiper
                    :loop="true"
                    :slidesPerView="1"
                    :spaceBetween="10"
                    :loopAdditionalSlides="1"
                    :autoplay="{
                      delay: 6000,
                    }"
                    :modules="modules"
                    class="owl-carousel"
                  >
                    <swiper-slide>
                      <div class="list_inner">
                        <div class="text">
                          <i class="icon-quote-left"></i>
                          <p>
                            Belo design minimalista e ótima resposta rápida
                            com suporte. Altamente recomendado. Obrigado Micka!
                          </p>
                        </div>
                        <div class="details">
                          <div class="image">
                            <div
                              class="main"
                              :style="{ backgroundImage: 'url(img/testimonials/eli_mario.png)' }"
                            ></div>
                          </div>
                          <div class="info">
                            <h3>Eli Mário</h3>
                            <span>Jornalista - Tecla1</span>
                          </div>
                        </div>
                      </div>
                    </swiper-slide>
                    <swiper-slide>
                      <div class="list_inner">
                        <div class="text">
                          <i class="icon-quote-left"></i>
                          <p>
                            Essas pessoas realmente sabem o que estão fazendo! Ótimo
                            suporte ao cliente e excelente gentileza.
                          </p>
                        </div>
                        <div class="details">
                          <div class="image">
                            <div
                              class="main"
                              :style="{ backgroundImage: 'url(img/testimonials/paulo_gabriel_v2.png)' }"
                            ></div>
                          </div>
                          <div class="info">
                            <h3>Paulo Gabriel</h3>
                            <span>Presidente da Jorgraf e Jornalista<br>Arapiraca News</span>
                          </div>
                        </div>
                      </div>
                    </swiper-slide>
                    <swiper-slide>
                      <div class="list_inner">
                        <div class="text">
                          <i class="icon-quote-left"></i>
                          <p>
                            Tive um pequeno problema e o suporte foi apenas
                            incrível para resolver a situação rapidamente. Continuem
                            assim.
                          </p>
                        </div>
                        <div class="details">
                          <div class="image">
                            <div
                              class="main"
                              :style="{ backgroundImage: 'url(img/testimonials/mariana_new.jpg)' }"
                            ></div>
                          </div>
                          <div class="info">
                            <h3>Mariana Melo</h3>
                            <span>Enfermeira Consulttymed</span>
                          </div>
                        </div>
                      </div>
                    </swiper-slide>
                  </swiper>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Navigation, Pagination } from "swiper";
import { Swiper, SwiperSlide } from "swiper/vue";
import AnimationText from "../AnimationText.vue";
export default {
  name: `AboutPopup`,
  components: {
    Swiper,
    SwiperSlide,
    AnimationText,
  },
  data() {
    return {
      open: false,
      // data
      aboutData: {
        firstName: "Micka",
        lastName: "Bandeira",
        bithday: "18.10.1991",
        address: "Arapiraca/AL",
        phn: "WhatsApp: 82 996004382",
        email: "mickaelbandeira91@gmail.com",
        serviceLists: [
          "Agentes de IA | MCP, APIS, RAG",
          "AI Coding",
          "Saas IA",
          "N8N",
          "Supabase | Modelagem de Bancos de Dados",
          "FlutterFlow",
          ".Bubble",
          "Framer",
        ],
        skills: {
          programming: [
            { name: "Desenvolvimento Fullstack", value: "React, Next.js, Supabase, PostgreSQL" },
            { name: "IA & Automação", value: "n8n, OpenAI API, LangChain, Agentes de IA" },
            { name: "Ferramentas de Design", value: "Figma, Adobe Suite, Prototipagem de Alta Fidelidade" },
            { name: "Versionamento & Deploy", value: "Git, GitHub, Vercel, Docker" },
            { name: "Infraestrutura e Dados", value: "Hostinger - Infraestrutura Serverless, Hospedagem VPS - Hetzner - Infraestrutura Avançada, PostgreSQL - Modelagem de Dados" },
          ],
          language: [
            { name: "Português", value: "100" },
          ],
        },
        education: [
          {
            year: "Atualmente",
            unv: "Em Curso",
            degree: "Inteligência Artificial",
          },
        ],
        working: [
          {
            year: "Atualmente",
            company: "AeC",
            deg: "Analista de Conteúdo",
          },
          {
            year: "9 Anos",
            company: "Experiência Geral",
            deg: "Designer Gráfico, Diagramador, Dev & IA",
          },
        ],
        partnersLogos: [
          "img/partners/consultymed.png",
          "img/partners/blog_do_bina.png",
          "img/partners/tecla1.png",
          "img/partners/aec.png",
          "img/partners/partner_6.png",
          "img/partners/partner_7.png",
          "img/partners/partner_8.png",
          "img/partners/partner_9.png",
        ],
      },
    };
  },
  methods: {
    close() {
      this.open = false;
    },
  },
  mounted() {
    const aboutPopup = document.getElementById("aboutPopup");
    aboutPopup.addEventListener("click", () => {
      this.open = true;
    });

    const myCircle = document.querySelectorAll(".myCircle");
    myCircle.forEach((circle) => {
      let progress = circle.getAttribute("data-value");
      let span = document.createElement("span");
      span.className = "number";
      const value = `${progress * 100}%`;
      span.innerHTML = value;
      circle.appendChild(span);
      circle.style.setProperty("--progress", value);
      circle.setAttribute("aria-valuenow", value);
    });
  },
  setup() {
    return {
      modules: [Navigation, Pagination],
    };
  },
};
</script>

<style scoped>
.testimonial {
  overflow: hidden;
}
.owl-carousel.swiper {
  overflow: unset;
}

.myCircle {
  --hue: 220;
  --holesize: 67%;
  --track-bg: hsl(233, 34%, 92%);

  min-width: 110px;
  min-height: 110px;
  display: grid;
  align-items: center;
  justify-items: center;
  place-items: center;
  position: relative;
  margin-bottom: 5px;
}
.myCircle::before {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  border-radius: 50%;
  z-index: -1;
  background: conic-gradient(
    var(--main-color) var(--progress, 0%),
    rgba(255, 255, 255, 0.15) var(--progress, 0%) 100%
  );

  mask-image: radial-gradient(
    transparent var(--holesize),
    black calc(var(--holesize) + 1px)
  );
}

.edrea_tm_modalbox .about_popup_details .left .list ul li span a {
  word-break: break-all;
  display: inline-block;
  line-height: 1.4;
}
</style>
