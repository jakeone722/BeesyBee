<template>
	<nav class="navbar navbar-expand-xl">
		<router-link :to="{ name: 'home' }" class="navbar-brand">
				<img src="../images/bee.png" alt="" srcset="" class="img-fluid" width="110">
				Beesy Movie
			</router-link>  		

		<!-- Collection of nav links, forms, and other content for toggling -->
		<div id="navbarCollapse" class="navbar-collapse justify-content-between">		
			<div class="navbar-nav ml-auto">
				<router-link :to="{ name: 'aboutus' }" class="nav-item nav-link" v-if="isLoggedIn"><i class="fa fa-users"></i>Aboutus</router-link> 
				<router-link :to="{ name: 'contactus' }" class="nav-item nav-link" v-if="isLoggedIn"><i class="fa fa-envelope"></i>Contactus</router-link> 
				<router-link :to="{ name: 'mypage' }" class="nav-item nav-link" v-if="isLoggedIn" @click="fetchProfile()"><i class="fa fa-gears"></i>Mypage</router-link> 
				<router-link :to="{ name: 'logout' }" class="nav-item nav-link" v-if="isLoggedIn" @click="fetchProfile()"><i class="material-icons">&#xE8AC;</i>Logout</router-link>
			</div>
			<form class="navbar-form form-inline">
				<div class="input-group search-box">								
					<input type="text" id="search" class="form-control" placeholder="Movie here" @keydown.enter.prevent="movieSearch(searchMovie)" aria-label="Search" v-model="searchMovie">
					<span class="input-group-addon"><i class="material-icons">&#xE8B6;</i></span>
				</div>
			</form>
		</div>
	</nav>
</template>

<script>
  import { mapGetters } from 'vuex'
  import { mapActions } from 'vuex'
  
  export default {
    name: 'NavBar',
    data() {
      return {
        searchMovie : ''
      }
    },
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
    },
    methods : {
      ...mapActions(['fetchProfile']),
      movieSearch : function (searchMovie) {
        this.$router.push( {name : 'search', query: { searchMovie } }  )
        this.searchMovie = ''
      }
    },
    components: {

    }
  }
</script>

<style>
.navbar {
	color: #fff;
	background: #FFCC5B;
	padding: 5px 16px;
	border-radius: 0;
	border: none;
	box-shadow: 0 0 2em #7C683C;
}
.navbar img {
	border-radius: 50%;
	width: 36px;
	height: 36px;
	margin-right: 10px;
}
.navbar .navbar-brand {
	color: #7C683C;
	padding-left: 0;
	padding-right: 50px;
	font-size: 2em;
	font-family: 'Do Hyeon', sans-serif;	
}
.navbar .navbar-brand:hover, .navbar .navbar-brand:focus {
	color: #7C683C;
}
.navbar .navbar-brand i {
	font-size: 25px;
	margin-right: 5px;
}
.search-box {
	position: relative;
}	
.search-box input {
	padding-right: 35px;
	min-height: 38px;
	border: none;
	background: #faf7fd;
	border-radius: 3px ;
}
.search-box input:focus {		
	background: #fff;
	box-shadow: none;
}
.search-box .input-group-addon {
	min-width: 35px;
	border: none;
	background: transparent;
	position: absolute;
	right: 0;
	z-index: 9;
	padding: 10px 7px;
	height: 100%;
}
.search-box i {
	color: #a0a5b1;
	font-size: 19px;
}
.navbar .nav-item i {
	font-size: 18px;
}
.navbar .nav-item {
	position: relative;
	top: 3px;
	font-family: 'Noto Sans KR', sans-serif;
}
.navbar .navbar-nav > a {
	color: #7C683C;;
	padding: 8px 15px;
	font-size: 14px;		
}
.navbar .navbar-nav > a:hover, .navbar .navbar-nav > a:focus {
	color: #C7EBEF;
	text-shadow: 0 0 4px rgba(255,255,255,0.3);
}
.navbar .navbar-nav > a > i {
	display: block;
	text-align: center;
}
.navbar .navbar-nav .active a, .navbar .navbar-nav .active a:hover, .navbar .navbar-nav .active a:focus {
	color: #fff;
	text-shadow: 0 0 4px #7C683C;
	background: transparent ;
}
.navbar .navbar-toggle {
	border-color: #fff;
}
.navbar .navbar-toggle .icon-bar {
	background: #fff;
}
.navbar .navbar-toggle:focus, .navbar .navbar-toggle:hover {
	background: transparent;
}
.navbar .divider {
	background-color: #e9ecef ;
}
@media (min-width: 1200px){
	.form-inline .input-group {
		width: 350px;
		margin-left: 30px;
	}
}
@media (max-width: 1199px){
	.navbar .navbar-nav > a > i {
		display: inline-block;			
		text-align: left;
		min-width: 30px;
		position: relative;
		top: 4px;
	}
	.navbar .navbar-collapse {
		border: none;
		box-shadow: none;
		padding: 0;
	}
	.navbar .navbar-form {
		border: none;			
		display: block;
		margin: 10px 0;
		padding: 0;
	}
	.navbar .navbar-nav {
		margin: 8px 0;
	}
	.navbar .navbar-toggle {
		margin-right: 0;
	}
	.input-group {
		width: 100%;
	}
}
</style>
