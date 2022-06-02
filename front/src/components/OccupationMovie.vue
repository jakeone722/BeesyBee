<template>
  <div class="movie-rec">
    <h3 v-if="profile.occupation === '0'">대충 아무에게나 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '1'">교권 어디갔지 : 교육자에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '2'">영감 덩어리 : 예술가에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '3'">사장놈... : 사무관리직에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '4'">교수님 제발 : 대학생 및 대학원생에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '5'">인간혐오 : 서비스업 종사자에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '6'">코로나 그만! : 의사 및 의료계 종사자에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '7'">일들 좀 해라 : 임원 및 관리자 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '8'">비야 와라 - 케이시 : 농부에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '9'">집 정리 좀... : 전업주부에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '10'">공부는 무슨 : 청소년 및 학생에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '11'">대통령도 법조인 : 법조인에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '12'">우리는 3D야.. : 프로그래머에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '13'">소일거리 대신! : 은퇴하신 분에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '14'">갑질 멈춰! : 영업 및 마케팅 직종에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '15'">오르트 구름 : 과학자에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '16'">일 좀 주이소 : 프리랜서에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '17'">니들이 현장을 알아? : 기계공 및 엔지니어에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '18'">카드보단 계좌이체로 : 소상공인에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '19'">할 수 있다! : 백수에게 추천하는 영화</h3>
    <h3 v-if="profile.occupation === '20'">책 좀 읽어라 : 작가에게 추천하는 영화</h3>
      <div id="carouselExampleControls2" class="carousel slide carousel-fade" data-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active ">
            <div class="row">
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[0].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[0].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[1].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[1].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[2].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[2].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[3].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[3].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[4].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[4].poster_path}`"  alt="...">
                </router-link>
              </div>
            </div>
          </div>
          <div class="carousel-item ">
            <div class="row">
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[5].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[5].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[6].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[6].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[7].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[7].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[8].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[8].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[9].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[9].poster_path}`"  alt="...">
                </router-link>
              </div>
            </div>
          </div>
          <div class="carousel-item ">
            <div class="row">
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[10].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[10].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[11].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[11].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[12].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[12].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[13].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[13].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[14].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[14].poster_path}`"  alt="...">
                </router-link>
              </div>
            </div>
          </div>
          <div class="carousel-item ">
            <div class="row">
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[15].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[15].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[16].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[16].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[17].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[17].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[18].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[18].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[19].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[19].poster_path}`"  alt="...">
                </router-link>
              </div>
            </div>
          </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleControls2" role="button" data-slide="prev" style="width: 7%">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleControls2" role="button" data-slide="next" style="width: 7%">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'


export default {
  name : 'OccupationMovies',
  props: {
    profile: Object
  },
  computed: {
    ...mapGetters(['occupationMovies', 'currentsUser']), 
  },    
}
</script>

<style>

</style>