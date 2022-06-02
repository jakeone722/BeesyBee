<template>
  <div class="movie-rec">
    <h3>내가 돈쭐 내주마 : 코인형 영화</h3>
    <div id="carouselExampleControls4" class="carousel slide carousel-fade" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active ">
          <div class="row">
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[0][1]}` } }">
                <img :src="`${costeffectiveMovies[0][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[1][1]}` } }">
              <img :src="`${costeffectiveMovies[1][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[2][1]}` } }">
              <img :src="`${costeffectiveMovies[2][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[3][1]}` } }">
              <img :src="`${costeffectiveMovies[3][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[4][1]}` } }">
              <img :src="`${costeffectiveMovies[4][2]}`" class="" alt="...">
              </router-link>                
            </div>
          </div>
        </div>
        <div class="carousel-item ">
          <div class="row">
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[5][1]}` } }">
              <img :src="`${costeffectiveMovies[5][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[6][1]}` } }">
              <img :src="`${costeffectiveMovies[6][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[7][1]}` } }">
              <img :src="`${costeffectiveMovies[7][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[8][1]}` } }">
              <img :src="`${costeffectiveMovies[8][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[9][1]}` } }">
              <img :src="`${costeffectiveMovies[9][2]}`" class="" alt="...">
              </router-link>                
            </div>
          </div>
        </div>
        <div class="carousel-item ">
          <div class="row">
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[10][1]}` } }">
              <img :src="`${costeffectiveMovies[10][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[11][1]}` } }">
              <img :src="`${costeffectiveMovies[11][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[12][1]}` } }">
              <img :src="`${costeffectiveMovies[12][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[13][1]}` } }">
              <img :src="`${costeffectiveMovies[13][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[14][1]}` } }">
              <img :src="`${costeffectiveMovies[14][2]}`" class="" alt="...">
              </router-link>                
            </div>
          </div>
        </div>
        <div class="carousel-item ">
          <div class="row">
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[15][1]}` } }">
              <img :src="`${costeffectiveMovies[15][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[16][1]}` } }">
              <img :src="`${costeffectiveMovies[16][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[17][1]}` } }">
              <img :src="`${costeffectiveMovies[17][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[18][1]}` } }">
              <img :src="`${costeffectiveMovies[18][2]}`" class="" alt="...">
              </router-link>                
            </div>
            <div class="card-movie col" >
              <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[19][1]}` } }">
              <img :src="`${costeffectiveMovies[19][2]}`" class="" alt="...">
              </router-link>                
            </div>
          </div>
        </div>
      </div>
      <div>  
      <a class="carousel-control-prev" href="#carouselExampleControls4" role="button" data-slide="prev" style="width: 7%">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      </div>
      <div>
      <a class="carousel-control-next" href="#carouselExampleControls4" role="button" data-slide="next" style="width: 7%">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'


export default {
  name : 'CosteffectiveMovies',
  computed: {
    ...mapGetters(['costeffectiveMovies', 'currentsUser']), 
  },
}
</script>

<style>
.card-movie {
  border: none;

}
.carousel {
  justify-content: center;
  align-items: center;
}
.carousel-inner {
  padding: 2em 0em 4em 0em;
  justify-content: center;
  align-items: center;
}
.carousel-item .row {
  margin-left: 6em;
  margin-right: 6em;
}
.card-movie img {
  max-width: 100%;
  max-height: 100%;
  border-radius: 10px;
  box-shadow: 0 3px 5px 0 #7C683C;
}
.carousel-control-prev,
.carousel-control-next {
  background-color: #e1e1e1;
  border-radius: 50%;
  width: 7%;
}

@media (min-width: 768px) {
    .card-movie img {
      height: 20em;
    }
 }

.movie-rec h3 {
  color: #FFCC5B;
  padding-top: 1em;
  font-family: 'Do Hyeon', sans-serif;
}


.movie-rec {
  border-style: solid;
  border-width: 0.3em 0px 0px 0px;
  border-color: #FFCC5B;
}
</style>