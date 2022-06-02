<template>
  <div class="wrapper-signup fadeInDown-signup">
    <div id="formContent-signup">
      <!-- Signup Card -->
      <div class="fadeIn-signup first-signup">
        <img src="../images/제목을 입력해주세요_-001 (4).png" id="icon" alt="User Icon" />
      </div>
      <account-error-list v-if="authError"></account-error-list>
      <p class="background: #FFCC5B;"></p>
      <!-- Signup Form -->
      <form @submit.prevent="signup(credentials)">
          <input v-model="credentials.username" type="text" id="username" placeholder="아이디" class="fadeIn-signup first-signup text-signup" required/>
          <input v-model="credentials.password1" type="password" id="password1" placeholder="패스워드" class="fadeIn-signup first-signup pwd-signup" required />
          <input v-model="credentials.password2" type="password" id="password2" placeholder="패스워드 확인" class="fadeIn-signup first-signup pwd-signup" required />   
          <input v-model="credentials.age" type="number" id="age" min="1" placeholder="나이" class="fadeIn-signup third-signup number-signup" required />
          <select v-model="credentials.gender" type="gender" id="gender" class="fadeIn-signup fourth-signup my-1 select-signup"  required >
            <option value="">성별을 선택하세요.</option>
            <option value="M" style="height :5px;">남자</option>
            <option value="F">여자</option>
          </select>
          <select v-model="credentials.occupation" type="occupation" id="occupation" class="fadeIn-signup fourth-signup my-1 select-signup" required >
            <option value="">직업을 선택하세요.</option>
            <option value="0">기타</option>
            <option value="1">교육자</option>
            <option value="2">예술가</option>
            <option value="3">사무관리직</option>
            <option value="4">대학생 및 대학원생</option>
            <option value="5">서비스업 종사자 </option>
            <option value="6">의사 및 의료계 종사자</option>
            <option value="7">임원 및 관리자 </option>
            <option value="8">농부</option>
            <option value="9">전업주부</option>
            <option value="10">청소년 및 학생</option>
            <option value="11">법조인</option>
            <option value="12">프로그래머</option>
            <option value="13">은퇴</option>
            <option value="14">영업 및 마케팅</option>
            <option value="15">과학자</option>
            <option value="16">프리랜서</option>
            <option value="17">기계공 및 엔지니어</option>
            <option value="18">소상공인</option>
            <option value="19">백수</option>
            <option value="20">작가</option>
          </select>
          <p class="background: #FFCC5B;"></p>
          <input type="submit" class="fadeIn-signup fourth-signup submit-signup" value="회원 가입" style="margin: 5px 20px 20px 20px;">
          <input type="submit" class="fadeIn-signup fourth-signup submit-signup" value="뒤로 가기" @click.self.prevent="back()"> 
      </form>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
          age : '',
          gender : '',
          occupation : '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup']),
      back() {
        
        this.$router.back()
      }
    },
    metaInfo: {
      // Children can override the title.
      title: 'SIGN UP | BEESY',
      // Result: My Page Title ← My Site
      // If a child changes the title to "My Other Page Title",
      // it will become: My Other Page Title ← My Site
      titleTemplate: 'BEESY | SIGN UP',
      // Define meta tags here.
      meta: [
        {http_equiv: 'Content-Type', content: 'text/html; charset=utf-8'},
        {name: 'viewport', content: 'width=device-width, initial-scale=1.0,maximum-scale=2.0'},
        {name: 'description', content: 'Beesy Movie에 회원가입 하셔서 영화 추천 서비스를 즐기세요.'}
      ]
    }
  }
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap");
/* STRUCTURE */


.wrapper-signup {
  display: flex;
  align-items: center;
  flex-direction: column; 
  justify-content: center;
  width: 100%;
  min-height: 100%;
  padding: 20px;
}

#formContent-signup {
  -webkit-border-radius: 10px 10px 10px 10px;
  border-radius: 10px 10px 10px 10px;
  background: #FFCC5B;
  padding: 30px;
  width: 90%;
  max-width: 450px;
  position: relative;
  padding: 0px;
  -webkit-box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);
  box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);
  text-align: center;
}

#formfooter-signup {
  background-color: #7C683C;
  border-top: 1px solid #7C683C;
  padding: 25px;
  text-align: center;
  -webkit-border-radius: 0 0 10px 10px;
  border-radius: 0 0 10px 10px;
}

.signupcancle {
  text-decoration: none;
  text-align: center;
  font-size : 16px;
}

/* TABS */

h2.inactive {
  color: #FFCC5B;
}

h2.active {
  color: #0d0d0d;
  border-bottom: 2px solid #C7EBEF;
}



/* FORM TYPOGRAPHY*/

input[type=button], .submit-signup, input[type=reset]  {
  background-color: #7C683C;
  border: none;
  color: #FFCC5B;
  padding: 15px 80px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  text-transform: uppercase;
  font-size: 13px;
  -webkit-box-shadow: 0 10px 30px 0 rgba(95,186,233,0.4);
  box-shadow: 0 10px 30px 0 rgba(95,186,233,0.4);
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
  margin: 5px 20px 40px 20px;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -ms-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
}

input[type=button]:hover, .submit-signup:hover, input[type=reset]:hover  {
  background-color: #7C683C;
}

input[type=button]:active, .submit-signup:active, input[type=reset]:active  {
  -moz-transform: scale(0.95);
  -webkit-transform: scale(0.95);
  -o-transform: scale(0.95);
  -ms-transform: scale(0.95);
  transform: scale(0.95);
}

.text-signup {
  background-color: #C7EBEF;
  border: none;
  color: #0d0d0d;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 5px;
  width: 85%;
  border: 2px solid #FFCC5B;
  -webkit-transition: all 0.5s ease-in-out;
  -moz-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
}

.text-signup:focus {
  background-color: #C7EBEF;
  border-bottom: 2px solid #7C683C;
}

.text-signup:placeholder {
  color: #C7EBEF;
}

.pwd-signup {
  background-color: #C7EBEF;
  border: none;
  color: #0d0d0d;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 5px;
  width: 85%;
  border: 2px solid #C7EBEF;
  -webkit-transition: all 0.5s ease-in-out;
  -moz-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
}

.pwd-signup:focus {
  background-color: #C7EBEF;
  border-bottom: 2px solid #7C683C;
}

.pwd-signup:placeholder {
  color: #C7EBEF;
}

.number-signup {
  background-color: #C7EBEF;
  border: none;
  color: #0d0d0d;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 5px;
  width: 85%;
  border: 2px solid #C7EBEF;
  -webkit-transition: all 0.5s ease-in-out;
  -moz-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
}

.number-signup:focus {
  background-color: #C7EBEF;
  border-bottom: 2px solid #7C683C;
}


.number-signup:placeholder {
  color: #C7EBEF;
}

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.select-signup {
  background-color: #C7EBEF;
  border: none;
  color: #0d0d0d;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 5px;
  width: 85%;
  border: 2px solid #FFCC5B;
  -webkit-transition: all 0.5s ease-in-out;
  -moz-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
  text-align-last: center;
}
.select-signup {
  -moz-appearance: none;
	-webkit-appearance: none;
	appearance: none;
  padding: 15px 32px;
  
}

.select-signup:focus :focus {
  background-color: #C7EBEF;
  border-bottom: 2px solid #7C683C;
}

.select-signup:placeholder {
  color: #C7EBEF;
}

#formfooter-signup {
  background-color: #7C683C;
  border-top: 1px solid #7C683C;
  padding: 25px;
  text-align: center;
  -webkit-border-radius: 0 0 10px 10px;
  border-radius: 0 0 10px 10px;
}


/* ANIMATIONS */

/* Simple CSS3 Fade-in-down Animation */
.fadeInDown-signup {
  -webkit-animation-name: fadeInDown;
  animation-name: fadeInDown;
  -webkit-animation-duration: 1s;
  animation-duration: 1s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}

@keyframes fadeInDown {
  0% {
    opacity: 0;
    -webkit-transform: translate3d(0, -100%, 0);
    transform: translate3d(0, -100%, 0);
  }
  100% {
    opacity: 1;
    -webkit-transform: none;
    transform: none;
  }
}

@keyframes fadeInDown-signup {
  0% {
    opacity: 0;
    -webkit-transform: translate3d(0, -100%, 0);
    transform: translate3d(0, -100%, 0);
  }
  100% {
    opacity: 1;
    -webkit-transform: none;
    transform: none;
  }
}

/* Simple CSS3 Fade-in Animation */
@-webkit-keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
@-moz-keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
@keyframes fadeIn { from { opacity:0; } to { opacity:1; } }

.fadeIn {
  opacity:0;
  -webkit-animation:fadeIn ease-in 1;
  -moz-animation:fadeIn ease-in 1;
  animation:fadeIn ease-in 1;

  -webkit-animation-fill-mode:forwards;
  -moz-animation-fill-mode:forwards;
  animation-fill-mode:forwards;

  -webkit-animation-duration:1s;
  -moz-animation-duration:1s;
  animation-duration:1s;
}

.fadeIn-signup.first-signup {
  -webkit-animation-delay: 0.4s;
  -moz-animation-delay: 0.4s;
  animation-delay: 0.4s;
}

.fadeIn-signup.second-signup {
  -webkit-animation-delay: 0.6s;
  -moz-animation-delay: 0.6s;
  animation-delay: 0.6s;
}

.fadeIn-signup.third-signup {
  -webkit-animation-delay: 0.8s;
  -moz-animation-delay: 0.8s;
  animation-delay: 0.8s;
}

.fadeIn-signup.fourth-signup {
  -webkit-animation-delay: 1s;
  -moz-animation-delay: 1s;
  animation-delay: 1s;
}

/* Simple CSS3 Fade-in Animation */
.underlineHover:after {
  display: block;
  left: 0;
  bottom: -10px;
  width: 0;
  height: 2px;
  background-color: #C7EBEF;
  content: "";
  transition: width 0.2s;
}

.underlineHover:hover {
  color: #0d0d0d;
}

.underlineHover:hover:after{
  width: 100%;
}



/* OTHERS */

*:focus {
    outline: none;
} 

#icon {
  width:60%;
}



</style>
