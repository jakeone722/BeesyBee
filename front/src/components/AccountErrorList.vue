<template>
  <!-- Error -->
  <div class="account-error-list">
    <p class="animate__animated animate__shakeX" v-for="(errors, field) in authError" :key="field">
      <span>
      로그인 정보가 잘못되었습니다.
      </span>
      <br>
      <span>
      아이디 / 비밀번호를 확인해주세요.
      </span>
    </p>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError'])
    },
    metaInfo: {
    // Children can override the title.
    title: 'Error Page',
    // Result: My Page Title ← My Site
    // If a child changes the title to "My Other Page Title",
    // it will become: My Other Page Title ← My Site
    titleTemplate: 'Error',
    // Define meta tags here.
    meta: [
      {http_equiv: 'Content-Type', content: 'text/html; charset=utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {name: 'description', content: 'I have things here on my site.'}
    ]
  }
  }
</script>

<style>
  .account-error-list {
    color: red;
  }

</style>
