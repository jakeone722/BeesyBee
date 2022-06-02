<template>
  <div>
    <hr>
    <form @submit.prevent="onSubmit" class="row">
      <div class="col-1 name-revielistitem box-username">
      <!-- 네임 -->
        {{currentUser.username}}
      </div>
      <!-- 평점 -->
      <div class="col-2">
        <b-form-rating style="color: #FFCC5B; " id="rating-lg-no-border" no-border size="lg" v-model="rate"></b-form-rating>
      </div>
      <!-- 내용 --> 
      <div class="col-7">
        <input type="textarea" class="box-content-input" v-model="content" required>
      </div>
      <!-- 수정 / 삭제 -->
      <div class="col-2">
        <button class="btn btn-create" style="background-color : #7C683C; color: #FFCC5B; " >Review 작성</button>
      </div>
    </form>
  </div>


</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { BFormRating } from 'bootstrap-vue'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: '',
      rate : null
    }
  },
  components : {
    BFormRating
  },
  computed : {
    ...mapGetters(['detailMovie', 'currentUser'])
  },
  methods: {
    ...mapActions(['createReview', 'fetchCurrentUser']),
    onSubmit() {
      const movieId = this.detailMovie.id
      if (this.rate==null) {
        alert('평점을 입력해 주세요 ')
      }
      else {
        this.createReview({ moviePk : movieId, content: this.content, rate : this.rate })
        this.content = ''
      }
    }
  },
}
</script>

<style>
.review-list-form {
  border: 1px solid black;
  padding: 1rem;
}
.box-username {
  margin:auto
}
.box-content-input {
  width:100%; 
  height:100%;
}
</style>