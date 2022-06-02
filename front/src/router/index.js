import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SearchView from '@/views/SearchView.vue'
import DetailView from '@/views/DetailView.vue'
import MypageView from '@/views/MypageView.vue'
import AboutusView from '@/views/AboutusView.vue'
import ContactUsView from '@/views/ContactUsView.vue'
import NotFound404 from '@/views/NotFound404.vue'
import store from '../store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },  
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/search/',
    name: 'search',
    component: SearchView
  },
  {
    path: '/detail/',
    name: 'detail',
    component: DetailView
  },
  {
    path: '/mypage',
    name: 'mypage',
    component: MypageView
  },
  {
    path: '/aboutus',
    name: 'aboutus',
    component: AboutusView
  },
  {
    path: '/contactus',
    name: 'contactus',
    component: ContactUsView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior () {
    return { x: 0, y: 0 }
  }
})

router.beforeEach((to, from, next) => {
  // 이전 페이지에서 발생한 에러메시지 삭제
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login', 'signup', 'home']
  const signupLogin = ['login', 'signup', ]


  const isAuthRequired = !noAuthPages.includes(to.name)
  const isSignupLogin = !signupLogin.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('로그인된 사용자만 이용 가능합니다.')
    next({ name: 'home' })
  } else {
    next()
  }
  if (!isSignupLogin && isLoggedIn) {
    alert('이미 로그인 했습니다.')
    next({ name: 'home' })
  }


})
export default router
