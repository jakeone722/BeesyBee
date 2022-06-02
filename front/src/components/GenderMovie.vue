<template>
  <div class="movie-rec">
    <h3 v-if="profile.gender === 'F'">여자에게 추천하는 영화</h3>
    <h3 v-if="profile.gender === 'M'">남자에게 추천하는 영화</h3>
      <div id="carouselExampleControls5" class="carousel slide carousel-fade" data-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active ">
            <div class="row">
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[0].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[0].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[1].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[1].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[2].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[2].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[3].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[3].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[4].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[4].poster_path}`"  alt="...">
                </router-link>
              </div>
            </div>
          </div>
          <div class="carousel-item ">
            <div class="row">
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[5].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[5].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[6].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[6].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[7].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[7].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[8].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[8].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[9].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[9].poster_path}`"  alt="...">
                </router-link>
              </div>
            </div>
          </div>
          <div class="carousel-item ">
            <div class="row">
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[10].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[10].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[11].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[11].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[12].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[12].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[13].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[13].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[14].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[14].poster_path}`"  alt="...">
                </router-link>
              </div>
            </div>
          </div>
          <div class="carousel-item ">
            <div class="row">
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[15].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[15].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[16].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[16].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[17].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[17].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[18].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[18].poster_path}`"  alt="...">
                </router-link>
              </div>
              <div class="card-movie col" >
                <router-link :to =" { name : 'detail', query : { id : `${genderMovies.results[19].id}` } }">
                <img :src="`https://image.tmdb.org/t/p/original/${genderMovies.results[19].poster_path}`"  alt="...">
                </router-link>
              </div>
            </div>
          </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleControls5" role="button" data-slide="prev" style="width: 7%">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleControls5" role="button" data-slide="next" style="width: 7%">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'


export default {
  name : 'GenderMovies',
  props: {
    profile: Object
  },
  computed: {
    ...mapGetters(['genderMovies', 'currentsUser']), 
  },
}
</script>

<style>
</style>