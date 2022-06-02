// import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  // namespaced: true,

  // state는 직접 접근하지 않겠다!
  state: {
    ageMovies : [],
    occupationMovies : [],
    genderMovies : [],
    searchMovies : [],
    detailMovie : {},
    costeffectiveMovies : [],
  },
  // 모든 state는 getters 를 통해서 접근하겠다.
  getters: {
    ageMovies: state => state.ageMovies,
    occupationMovies: state => state.occupationMovies,
    genderMovies: state => state.genderMovies,
    searchMovies: state => state.searchMovies,
    detailMovie: state => state.detailMovie,
    costeffectiveMovies: state => state.costeffectiveMovies,
  },

  mutations: {
    SET_AGE_MOVIES : (state, ageMovies) => state.ageMovies = ageMovies,
    SET_OCCUPATION_MOVIES : (state, occupationMovies) => state.occupationMovies = occupationMovies,
    SET_GENDER_MOVIES : (state, genderMovies) => state.genderMovies = genderMovies,
    SET_SEARCH_MOVIES : (state, searchMovies) => state.searchMovies = searchMovies,
    SET_DETAIL_MOVIE : (state, detailMovie) => state.detailMovie = detailMovie,
    SET_COSTEFFECTIVE_MOVIES : (state, costeffectiveMovies) => state.costeffectiveMovies = costeffectiveMovies,
    SET_MOVIE_REVIEWS: (state, reviews) => (state.detailMovie.review_set = reviews),
  },
  actions: {
    setAgeMovies({ commit, getters }, userName) {
      axios({
        url : drf.movies.age(userName),
        method : 'get',
        headers : getters.authHeader,
      })
        .then(res => commit('SET_AGE_MOVIES', res.data))
        .catch(err => console.log(err.response))
    },
    setGenderMovies({ commit, getters }, userName) {
      axios({
        url : drf.movies.gender(userName),
        method : 'get',
        headers : getters.authHeader,
      })
        .then(res => commit('SET_GENDER_MOVIES', res.data))
        .catch(err => console.log(err.response))
    },
    setOccupationMovies({ commit, getters }, userName) {
      axios({
        url : drf.movies.occupation(userName),
        method : 'get',
        headers : getters.authHeader,
      })
        .then(res => commit('SET_OCCUPATION_MOVIES', res.data))
        .catch(err => console.log(err.response))
    },
    setSearchMovies({ commit, getters }, searchMovie){
      axios({
        url : drf.movies.search(searchMovie),
        method : 'get',
        headers : getters.authHeader,
      })
        .then(res => commit('SET_SEARCH_MOVIES', res.data))
        .catch(err => console.log(err.response))
    },
    setDetailMovie({commit, getters}, detailMovie) {
      axios({
        url : drf.movies.detail(detailMovie),
        method : 'get',
        headers : getters.authHeader,
      })
        .then(res => commit('SET_DETAIL_MOVIE', res.data))
        .catch(err => console.log(err.response))
    },
    setCosteffectiveMovies({ commit, getters }) {
      axios({
        url : drf.movies.costeffective(),
        method : 'get',
        headers : getters.authHeader,
      })
        .then(res => commit('SET_COSTEFFECTIVE_MOVIES', res.data))
        .catch(err => console.log(err.response))
    },
    createReview( { commit, getters }, { moviePk, content, rate}) {
      const data1 = { content, rate }
      axios({
        url : drf.movies.createReview(moviePk),
        method : 'post',
        data : data1,
        headers : getters.authHeader,
      })
        .then(res => 
          commit('SET_MOVIE_REVIEWS', res.data))
        .catch(err => console.log(err.response))
    },
    deleteReview({ commit, getters }, { reviewPk }) {
      console.log(reviewPk)
      /* 댓글 삭제
      사용자가 확인을 받고
        DELETE: comment URL (token)
          성공하면
            응답으로 state.article의 comments 갱신
          실패하면
            에러 메시지 표시
      */
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.movies.deleteReview(reviewPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => 
              commit('SET_MOVIE_REVIEWS', res.data)
            )
            .catch(err => console.error(err.response))
        }
    },
    updateReview({ commit, getters }, { reviewPk, content, rate }) {
      /* 댓글 수정
      PUT: comment URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      console.log('가는중')
      const review = { content, rate }
      console.log(review)
      axios({
        url: drf.movies.updateReview(reviewPk),
        method: 'put',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
    },
  }
}