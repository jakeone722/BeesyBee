<template>
  <div class="searchdiv mt-3 row">
    <div v-if="searchmovies.length === 0" class="error-search"> 
        <p>
            영화가 조회되지 않습니다. 
        </p>
        <p>
            다시 검색해주세요
        </p>
    </div>
    <div v-for="searchmovie in searchmovies" :key="searchmovie.id" class="col-6">
        <router-link :to =" { name : 'detail', query : {id : searchmovie.id,} }" class="router-search" style="text-decoration: none">
            <section class="search-result-item mt-3 mb-3">
                <img class="image image-link" :src="`https://image.tmdb.org/t/p/original/${searchmovie.poster_path}`">
                <div class="search-result-item-body">
                    <div class="">
                        <div class="">
                            <h4 class="search-result-item-heading" style="text-align : left;">
                                {{ searchmovie.title }}
                            </h4>
                            <hr>  
                            <div class="row" style="text-align : left;">
                                <div class="info"> 개봉일 : {{ searchmovie.release_date }} </div>
                                <div class="info"> TDMB 평점 : {{ searchmovie.vote_average }} </div>
                            </div>
                            <hr>
                            <div class="row" style="text-align : left;">
                                <div class="info" v-if="searchmovie.overview.length < 100"> 줄거리 : {{ searchmovie.overview }} </div>
                                <div class="info" v-if="searchmovie.overview.length >= 100"> 줄거리 : 생략 </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name : 'SearchList',
  props : {
    searchmovies : Array
  },
  computed : {
  },
}
</script>

<style>
.router-search {
    text-decoration: none ;
}

.info {
    font-size : 0.8em;
    font-family: 'Noto Sans KR', sans-serif;
    color: black;
}

.error-search {
    font-size : 3em;
	font-family: 'Do Hyeon', sans-serif;	
    color: #7C683C;
    padding: 2em;
}

.searchdiv{
  margin :20px;
  background-color: #eee;
}

.search-result-categories>li>a {
    color: #b6b6b6;
    font-weight: 400
}

.search-result-categories>li>a:hover {
    background-color: #ddd;
    color: #555
}

.search-result-categories>li>a>.glyphicon {
    margin-right: 5px
}

.search-result-categories>li>a>.badge {
    float: right
}

.search-results-count {
    margin-top: 10px
}

.search-result-item {
    padding: 20px;
    background-color: #fff;
    border-radius: 4px
}

.search-result-item:after,
.search-result-item:before {
    content: " ";
    display: table
}

.search-result-item:after {
    clear: both
}

.search-result-item .image-link {
    display: block;
    overflow: hidden;
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px
}

@media (min-width:768px) {
    .search-result-item .image-link {
        display: inline-block;
        margin: -20px 0 -20px -20px;
        float: left;
        width: 200px
    }
}

@media (max-width:767px) {
    .search-result-item .image-link {
        max-height: 200px
    }
}

.search-result-item .image {
    max-width: 100%
}

.search-result-item {
    margin-top: 5px;
    font-size: 20px;
    color: #999
}

.search-result-item .description {
    font-size: 15px;
    text-align : left;
}

.search-result-item+.search-result-item {
    margin-top: 20px
}

@media (min-width:768px) {
    .search-result-item-body {
        margin-left: 200px
    }
}


.search-result-item-heading {
    color: #555;
    font-size : 1.5em;
	font-family: 'Do Hyeon', sans-serif;	
    font-weight: bolder;
    text-decoration: none;
}

@media (min-width: 768px) {
    .search-result-item img {
      height: 15em;
    }
 }
</style>

