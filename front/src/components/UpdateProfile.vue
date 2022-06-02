<template>
  <div class="wrapper-signup fadeInDown-signup">
    <div id="formContent-signup">
      <!-- Icon -->
      <div class="fadeIn-update first-signup">
        <img src="../images/bee.png" id="icon" alt="User Icon" />
      </div>
      <!-- Signup Form -->
      <account-error-list v-if="authError"></account-error-list>
      <p class="background: #FFCC5B;"></p>
        <form @submit.prevent="signup(credentials)">
            <p class="p-update"><strong>{{ payload.username }}님, 꿀벌 카드를 수정해주세요!!</strong></p>
            <div class="fadeIn-update first-signup text-signup mb-2 ">
              <div class="row">
                <div class="col-3">
                  나이
                </div>
                <div class="col-9">
                  <input class="update-age" type="number" v-model="payload.age" value="payload.age">
                </div>
              </div>
            </div>
            <select v-model="payload.gender" type="gender" id="gender" class="fadeIn-update fourth-update my-1 select-signup"  required>
              <option value="">성별을 선택하세요.</option>
              <option value="M" style="height :5px;">남자</option>
              <option value="F">여자</option>
            </select>
            <select v-model="payload.occupation" type="occupation" id="occupation" class="fadeIn-update fourth-update my-1 select-signup"  required>
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
            <p class="background: #FFCC5B;"></p>
            <div>
              <button @click="onUpdate" class="btn-update fadeIn-update fourth-update submit-update">수정</button>
              <button @click="switching" class="btn-update fadeIn-update fourth-update submit-update">취소</button> 
            </div>
        </form>
    </div>

  </div>
</template>

<script>

import { mapActions } from 'vuex'

export default {
  name: 'UpdateProfile',
  components : {
  }, 
  props: {
    profile: Object,
  },
  data() {
    return {
      payload: {
        username: this.profile.username,
        age: this.profile.age,
        occupation: this.profile.occupation,
        gender: this.profile.gender,
      }
    }
  },
  methods: {
    ...mapActions(['updateProfile']),
    switching() {
      this.$emit('is-editing-changed')
    },
    onUpdate() {
      this.updateProfile(this.payload)
      this.$emit('is-editing-changed')
    }
  },
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap");
/* STRUCTURE */
.p-update {
	font-family: 'Do Hyeon', sans-serif;	
  font-size: 1.5em;
}

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
  font-size : 1em;
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


.btn-update, .submit-update, input[type=reset]  {
  background-color: #7C683C;
  border: none;
  color: #FFCC5B;
  padding: 15px 80px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  text-transform: uppercase;
  font-size: 2empx;
  -webkit-box-shadow: 0 10px 30px 0 rgba(95,186,233,0.4);
  box-shadow: 0 10px 30px 0 rgba(95,186,233,0.4);
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
  margin: 5px 20px 15px 20px;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -ms-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
  font-family: 'Do Hyeon', sans-serif;	
}

.btn-update:hover, .submit-update:hover, input[type=reset]:hover  {
  background-color: #7C683C;
}

.btn-update:active, .submit-update:active, input[type=reset]:active  {
  -moz-transform: scale(0.95);
  -webkit-transform: scale(0.95);
  -o-transform: scale(0.95);
  -ms-transform: scale(0.95);
  transform: scale(0.95);
}

.name-update {
  background-color: #7C683C;
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



.update-age {
  background-color: #C7EBEF;
  border: none;
  color: #0d0d0d;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border: 2px solid #C7EBEF;
  -webkit-transition: all 0.5s ease-in-out;
  -moz-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
}

.update-age:focus {
  background-color: #C7EBEF;
}


.update-age:placeholder {
  color: #C7EBEF;
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

.fadeIn-update.first-signup {
  -webkit-animation-delay: 0.4s;
  -moz-animation-delay: 0.4s;
  animation-delay: 0.4s;
}

.fadeIn-update.second-signup {
  -webkit-animation-delay: 0.6s;
  -moz-animation-delay: 0.6s;
  animation-delay: 0.6s;
}

.fadeIn-update.third-signup {
  -webkit-animation-delay: 0.8s;
  -moz-animation-delay: 0.8s;
  animation-delay: 0.8s;
}

.fadeIn-update.fourth-update {
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
