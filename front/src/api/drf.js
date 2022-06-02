const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const REVIEW = 'review/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: () => HOST + ACCOUNTS + 'profile/',
    updateProfile: () => HOST + ACCOUNTS + 'update/',
    resetPassword: () => HOST + ACCOUNTS + 'password/' + 'change/'
  },
  movies: {
    gender : (userName) => HOST + MOVIES + 'gender/' +`${userName}`,
    age : (userName) => HOST + MOVIES + 'age/' +`${userName}` ,
    occupation : (userName) => HOST + MOVIES + 'occupation/' +`${userName}`,
    search : (userName) => HOST + MOVIES + 'search/' +`${userName}`,
    detail : (userId) => HOST + MOVIES + 'detail/' +`${userId}`,
    costeffective : () => HOST + MOVIES + 'costeffective/',
    createReview : (moviePk) => HOST + MOVIES + REVIEW +`${moviePk}` + '/create/',
    deleteReview : (reviewPk) => HOST + MOVIES + REVIEW + `${reviewPk}` + '/delete/',
    updateReview : (reviewPk) => HOST + MOVIES + REVIEW + `${reviewPk}` + '/update/',
  },
}
