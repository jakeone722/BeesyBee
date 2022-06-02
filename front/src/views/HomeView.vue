<template>
  <div>
    <!-- Login view -->
    <div v-if="isLoggedIn">
      <div class="beesy-poster col-xl-12 ">
        <div>
          <h1>바쁘다 바빠 현대사회</h1>
          <h4>배달만 시켜놔, 영화는 골라줄게.</h4>
        </div>
      </div>
      <!-- MovieList -->
      <div class="beesy-bg">
        <costeffective-movie></costeffective-movie>
        <occupation-movie :profile="profile"></occupation-movie>
        <age-movie :profile="profile"></age-movie>
        <gender-movie :profile="profile"></gender-movie>
      </div>
    </div>
    <!-- !Login view -->
    <div v-if="!isLoggedIn">
      <div class="beesy d-flex align-items-center">
        <div class="container d-flex flex-column align-items-cneter">
          <h1>Beesy Movie</h1>
          <h2>바쁜 벌꿀은 영화볼 시간도 없다</h2>
          <span><router-link :to="{ name: 'login' }" style="text-decoration:none">로그인</router-link></span>
          <span><router-link :to="{ name: 'signup' }" style="text-decoration:none">회원가입</router-link></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import CosteffectiveMovie from '@/components/CosteffectiveMovie.vue'
  import OccupationMovie from '@/components/OccupationMovie.vue'
  import AgeMovie from '@/components/AgeMovie.vue'
  import GenderMovie from '@/components/GenderMovie.vue'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    metaInfo: {
    // Children can override the title.
    title: 'HOME | BEESY',
    // Result: My Page Title ← My Site
    // If a child changes the title to "My Other Page Title",
    // it will become: My Other Page Title ← My Site
    titleTemplate: 'BEESY | HOME',
    // Define meta tags here.
    meta: [
      {http_equiv: 'Content-Type', content: 'text/html; charset=utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1.0,maximum-scale=2.0'},
      {name: 'description', content: 'Beesy Movie에 오신 걸 환영합니다. 바쁜 현대인을 위한 영화 추천 플랫폼입니다.'}
    ]
    },
    name : 'HomeView',
    components : {
      OccupationMovie,
      CosteffectiveMovie,
      AgeMovie,
      GenderMovie,
    },
    methods: {
      ...mapActions(['setAgeMovies', 'setGenderMovies', 'setOccupationMovies', 'fetchCurrentUser',  'setCosteffectiveMovies', 'setCosteffectiveMovies', 'fetchProfile'])
    },
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser', 'profile']), 
    },
    watch : {
      currentUser : function () {
        this.setAgeMovies(this.currentUser.username)
        this.setGenderMovies(this.currentUser.username)
        this.setOccupationMovies(this.currentUser.username)
        this.setCosteffectiveMovies()
        this.fetchProfile()
      }
    },
    created(){
        this.fetchCurrentUser()
        this.fetchProfile()
    },

  }
</script>

  <style>
  a { text-decoration:none }

  .beesy-poster h1 {
    font-size: 100px;
    text-shadow: 0.1em 0.1em 0 black;
  }

  .beesy-poster h4 {
    font-size: 50px;
    text-shadow: 0.1em 0.1em 0 black;
  }

  .beesy-poster {
    width: 100%;
    height: 100%;
    text-align: center;
    position: relative;
    z-index: 1;
    color: white;
    font-size: 200px;
    font-family: 'Do Hyeon', sans-serif;
    padding-top: 300px;
    padding-bottom: 300px;
  }
  .beesy-poster::after {
    width: 100%;
    height: 100%;
    content: "";
    background: url("../images/posters_3.jpg");
    position: absolute;
    top: 0;
    left: 0;
    z-index: -1;
    opacity: 0.9;
    background-size: cover;
  }

  .beesy-bg {
    width: 100%;
    height: 100%;
    text-align: center;
    position: relative;
    z-index: 1;
  }
  .beesy-bg::after {
    width: 100%;
    height: 100%;
    content: "";
    background-color: #201919;
    position: absolute;
    top: 0;
    left: 0;
    z-index: -1;
    opacity: 0.95;
    background-size: cover;
  }

  .beesy {
    width: 100%;
    height: 100vh;
    background: url("../images/beesyhome.png") top right;
    background-size: cover;
  }
  .beesy .container {
    padding-top: 70px;
    position: relative;  
  }
  @media (max-width: 992px) {
    .beesy .container {
      padding-top: 58px;
    }
  }
  .beesy h1 {
    margin: 0.3em;
    font-size: 5em;
    font-weight: 700;
    line-height: 56px;
    color: #222222;
    font-family: 'Do Hyeon', sans-serif;
  }
  .beesy h2 {
    color: #222222;
    margin: 10px 0 0 0;
    font-size: 4em;
    font-family: 'Black Han Sans', sans-serif;
    text-shadow: 0.03em 0.03em 0 #7C683C;
  }
  .beesy a {
    font-family: 'Do Hyeon', sans-serif;
    text-transform: uppercase;
    font-weight: 600;
    font-size: 1em;
    letter-spacing: 1px;
    display: inline-block;
    padding: 12px 40px;
    border-radius: 50px;
    transition: 0.5s;
    margin-top: 30px;
    color: #fff;
    background: #7C683C;
  }
  .beesy a:hover {
    background: #7C683C;
  }
  @media (min-width: 1024px) {
    .beesy {
      background-attachment: fixed;
    }
  }
  @media (max-width: 992px) {
    .beesy:before {
      content: "";
      background: rgba(255, 255, 255, 0.8);
      position: absolute;
      bottom: 0;
      top: 0;
      left: 0;
      right: 0;
    }
    .beesy h1 {
      font-size: 28px;
      line-height: 36px;
    }
    .beesy h2 {
      font-size: 18px;
      line-height: 24px;
    }
  }
</style>
