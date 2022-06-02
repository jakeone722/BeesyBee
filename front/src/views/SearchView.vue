<template>
  <div class="searchdiv">
    <div class="searchdiv">
      <search-list :searchmovies="searchMovies.results">
      </search-list>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SearchList from '@/components/SearchList.vue'

export default {
  name : 'SearchView',
  components : {
    SearchList
  },
  methods: {
    ...mapActions(['fetchCurrentUser', 'setSearchMovies'])
  },
  computed : {
    ...mapGetters(['searchMovies']),
    searchedmoive : function (){
      return this.$route.query.searchMovie
    }
  },
  beforeCreate() {
  },
  created() {
    this.setSearchMovies(this.$route.query.searchMovie)
  },
  watch : {
    searchedmoive : function () {
      this.setSearchMovies(this.$route.query.searchMovie)
     }
  },
  metaInfo: {
    // Children can override the title.
    title: 'SEARCH | BEESY',
    // Result: My Page Title ← My Site
    // If a child changes the title to "My Other Page Title",
    // it will become: My Other Page Title ← My Site
    titleTemplate: 'BEESY | SEARCH',
    // Define meta tags here.
    meta: [
      {http_equiv: 'Content-Type', content: 'text/html; charset=utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1.0,maximum-scale=2.0'},
      {name: 'description', content: 'Beesy Movie에서 원하는 영화를 검색해 주세요.'}
    ]
  }
}
</script>

<style>
.searchdiv{
  background-color: #eee;
}
</style>