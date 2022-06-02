<template>
  <div class="movie-rec">
    <h3>{{ profile.age }}살에는 봐야하는 영화</h3>
      <!-- ageMovie carousel -->
      <div id="carouselExampleControls3" class="carousel slide carousel-fade" data-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active ">
            <div class="row">
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[0].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[0].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[1].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[1].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[2].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[2].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[3].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[3].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[4].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[4].poster_path}`" class="" alt="...">
                </router-link>
              </div>
            </div>
          </div>
          <div class="carousel-item ">
            <div class="row">
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[5].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[5].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[6].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[6].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[7].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[7].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[8].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[8].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[9].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[9].poster_path}`" class="" alt="...">
                </router-link>
              </div>
            </div>
          </div>
          <div class="carousel-item ">
            <div class="row">
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[10].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[10].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[11].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[11].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[12].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[12].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[13].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[13].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[14].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[14].poster_path}`" class="" alt="...">
                </router-link>
              </div>
            </div>
          </div>
          <div class="carousel-item ">
            <div class="row">
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[15].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[15].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[16].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[16].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[17].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[17].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[18].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[18].poster_path}`" class="" alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${ageMovies.results[19].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${ageMovies.results[19].poster_path}`" class="" alt="...">
                </router-link>
              </div>
            </div> 
          </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleControls3" role="button" data-slide="prev" style="width: 7%">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleControls3" role="button" data-slide="next" style="width: 7%">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'


export default {
  name : 'AgeMovie',
  props: {
    profile: Object
  },  
  computed: {
    ...mapGetters(['ageMovies', 'currentsUser']), 
  },
}
</script>

<style>


</style>