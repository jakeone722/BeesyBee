<template>
  <div id="app">
    <nav-bar v-if="isLoggedIn"></nav-bar>
    <router-view></router-view>
  </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'
  import { mapActions, mapGetters } from 'vuex'
  import './App.css'
  
  export default {
    name: 'App',
    components: { NavBar },

    methods: {
      ...mapActions(['fetchCurrentUser', 'setAgeMovies', 'setGenderMovies', 'setOccupationMovies', 'setSearchMovies'])
    },
    computed: {
      ...mapGetters(['currentUser', 'isLoggedIn',])
    },
    created(){
      this.fetchCurrentUser()

    },
    watch: {
    },
    // metaInfo: {
    //   meta: defualtMeta,
    // },

  }


</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
