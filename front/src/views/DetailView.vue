<template>
  <div class="mb-5">
    <!-- Backdrop & Title -->
    <div class="backdrop-path" :style="{ backgroundImage: `url(${detailMovie.backdrop_path})` }">
      <h1 class="title-detail">
        {{ detailMovie.title }} 
      </h1>
    </div>
    <!-- poster / Youtube -->
    <div class="row" style="width : 100%; margin:0;">
      <div class="col-4" >
        <div class="img-box">
          <img :src="`${detailMovie.poster_path}`" class="img-fluid img-detail" alt="">
        </div>
      </div>
      <div class="col-8 content row align-items-center second">
        <div class="second-box">
          <div class="custom-control custom-switch">
            <label class="switch">
              <input type="checkbox" @click="spoiler_change()">
              <span class="slider-detail round"></span>
            </label>
              <div class="switch-info" v-if="!spoiler">스포일러 켜기</div>
              <div class="switch-info" v-if="spoiler">스포일러 끄기</div>
          </div>
          <div v-if="spoiler">
            <video-item :selected-video="selectedVideo2"></video-item>
          </div>
          <div v-if="!spoiler">
            <video-item :selected-video="selectedVideo1"></video-item>
          </div>
        </div>
      </div>
    </div>
    <!-- overview -->
    <div class="third-box" style="width:100%">
      <p class="p-tagline">{{ detailMovie.tagline }}</p>      
      <hr v-if="detailMovie.tagline">       
      <p class="p-overview">{{ detailMovie.overview }}</p>
      <hr v-if="detailMovie.overview"> 
      <p class="p-time"> 개봉일 {{detailMovie.release_date}} | 상영시간 : {{detailMovie.runtime}} 분</p>
    </div>      
    <hr style="color:#7C683C; height: 0.3em;">  
    <!-- review-list -->
    <review-list :reviews="detailMovie.review_set" class="box-review"></review-list>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import ReviewList from '@/components/ReviewList.vue'
  import VideoItem from '@/components/VideoItem.vue'
  import axios from 'axios'

  const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
  const API_URL = 'https://www.googleapis.com/youtube/v3/search'

  export default {
    metaInfo: {
    // Children can override the title.
    title: 'DETAIL | BEESY',
    // Result: My Page Title ← My Site
    // If a child changes the title to "My Other Page Title",
    // it will become: My Other Page Title ← My Site
    titleTemplate: 'BEESY | DETAIL',
    // Define meta tags here.
    meta: [
      {http_equiv: 'Content-Type', content: 'text/html; charset=utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1.0,maximum-scale=2.0'},
      {name: 'description', content: 'Beesy는 TMDB와 YOUTUBE의 영화 정보를 이용합니다.'}
    ]
    },
    name : 'DetailView',
    data() {
      return {
        spoiler: false,
        videos1: [],
        selectedVideo1: null,
        videos2: [],
        selectedVideo2: null,
      }
    },
    components : {
      ReviewList,
      VideoItem
    },
    methods : {
      ...mapActions(['setDetailMovie']),
      spoiler_change() {
        this.spoiler = !this.spoiler
      },
      loadVideo1() {
        let params = {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.detailMovie.title + ' 예고편'
        }
        axios({
          method: 'GET',
          url: API_URL,
          params,
        })
          .then(res => {
            this.videos1 = res.data.items
            this.selectedVideo1 = this.videos1[0]
          })
          .catch(res => {
            console.log(res)
          })
      },
      loadVideo2() {
        let params = {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.detailMovie.title + '영화 리뷰'
        }
        axios({
          method: 'GET',
          url: API_URL,
          params,
        })
          .then(res => {
            this.videos2 = res.data.items
            this.selectedVideo2 = this.videos2[0]
          })
          .catch(err => {
            console.log(err)
        })
      }
    },
    computed : {
      ...mapGetters(['detailMovie']),
    inlineStyle () {
      return {
        backgroundImage: `url(${this.detailMovie.backdrop_path})` 
      }
    }
    },
    watch : {
      detailMovie : function () {
        this.loadVideo1()
        this.loadVideo2()
      }
    },
    created() {
      this.setDetailMovie(this.$route.query.id)
    },

  }
</script>

<style>
  .bee-img {
    max-width: 100%;
    height: 10em;
  }

  .second-box {
    background-color: #222222;;
    border-radius: 10px;
    box-shadow: 7px 7px 7px 0 #7C683C;
    padding-top: 1em;
    padding-bottom: 0.5em;
  }

  .img-detail {
    border-radius: 10px;
    box-shadow: 7px 7px 7px 0 #7C683C;
  }

  .backdrop-path {
    background-size:cover; 
  }

  .title-detail {
    padding-top: 3em;
    padding-bottom: 3em;
    color: black;
    background-color: rgba( 255, 255, 255, 0.5 );
    font-family: 'Do Hyeon', sans-serif;
    font-size: 5em;
    box-shadow: 0 7px 7px 0 #7C683C;
    text-shadow: 0.01em 0.01em 0 white;
  }

  .img-box {
    border: 2.5em solid white;
  }

  .slider-detail {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    -webkit-transition: .4s;
    transition: .4s;
  }

  .slider-detail:before {
    position: absolute;
    content: "";
    height: 26px;
    width: 26px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    -webkit-transition: .4s;
    transition: .4s;
  }

  .slider-detail.round {
    border-radius: 34px;
  }

  .slider-detail.round:before {
    border-radius: 50%;
  }

  input:checked + .slider-detail {
    background-color: #FFCC5B;
  }

  input:focus + .slider-detail {
    box-shadow: 0 0 1px #FFCC5B;
  }

  .third-box {
    background-color: #FFCC5B;
    border-radius: 5px;
    overflow: auto;
    border: 2.5em solid white;
    padding: 2em;
  }

  .second {
    border: 1.5em solid white;
  }

  input:checked + .slider-detail:before {
    -webkit-transform: translateX(26px);
    -ms-transform: translateX(26px);
    transform: translateX(26px);
  }
  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  .switch {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 34px;
  }

  .p-tagline {
    font-family: 'Do Hyeon', sans-serif;
    font-size: 1.5em;
    padding-bottom: 1m;
  }

  .p-overview {
    font-family: 'Noto Sans KR', sans-serif;
    padding-bottom: 1em;
  }

  .p-time { 
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 1.2em;
  }

  .switch-info {
    color:white;
    font-family: 'Do Hyeon', sans-serif;
  }
</style>