<template>
  <div class="edrea_tm_section" id="contact">
    <div class="section_inner">
      <div class="edrea_tm_contact">
        <div class="edrea_tm_main_title">
          <h3>Entre em <span class="coloring">Contato</span></h3>
        </div>
        <div class="wrapper">
          <div class="left">
            <ul>
              <li>
                <div class="list_inner">
                  <i class="icon-location"></i>
                  <span
                    ><a href="#" class="href_location"
                      >Arapiraca/AL</a
                    ></span
                  >
                </div>
              </li>
              <li>
                <div class="list_inner">
                  <i class="icon-phone"></i>
                  <span><a href="#">WhatsApp: 82 996004382</a></span>
                </div>
              </li>
              <li>
                <div class="list_inner">
                  <i class="icon-mail-1"></i>
                  <span
                    ><a href="mailto:mickaelbandeira91@gmail.com"
                      >mickaelbandeira91@gmail.com</a
                    ></span
                  >
                </div>
              </li>
              <li>
                <div class="list_inner">
                  <i class="icon-instagram-1"></i>
                  <span
                    ><a href="https://www.instagram.com/mickaelbandeira/"
                      >@mickaelbandeira</a
                    ></span
                  >
                </div>
              </li>
            </ul>
          </div>
          <div class="right">
            <div class="fields">
              <form
                action="/"
                method="post"
                class="contact_form"
                id="contact_form"
              >
                <div
                  class="returnmessage"
                  data-success="Sua mensagem foi recebida, entraremos em contato em breve."
                ></div>
                <div class="empty_notice">
                  <span>Por favor, preencha os campos obrigatórios</span>
                </div>
                <div class="first">
                  <ul>
                    <li>
                      <div class="list_inner">
                        <input
                          id="name"
                          type="text"
                          placeholder="Nome"
                          autocomplete="off"
                        />
                      </div>
                    </li>
                    <li>
                      <div class="list_inner">
                        <input
                          id="email"
                          type="text"
                          placeholder="E-mail"
                          autocomplete="off"
                        />
                      </div>
                    </li>
                  </ul>
                </div>
                <div class="last">
                  <textarea id="message" placeholder="Mensagem"></textarea>
                </div>
                <div class="edrea_tm_button">
                  <a id="send_message" href="#">Enviar Mensagem</a>
                </div>

                <!-- If you want change mail address to yours, just open "modal" folder >> contact.php and go to line 4 and change detail to yours.  -->
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: `ContactComponent`,
};
</script>
