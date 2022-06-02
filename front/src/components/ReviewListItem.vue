<template>
  <div class="review-item">
      <hr>
    <div v-if="isEditing" class="main-div-reviewlistitem">
      <div class="row">
        <div class="col-1 name-revielistitem box-username">
        <!-- 네임 -->
          {{ review.user.username }}
        </div>
        <!-- 평점 -->
        <div class="col-2" >
          <b-form-rating style="color: #FFCC5B; " id="rating-lg-no-border" no-border size="lg" v-model="payload.rate" value="payload.rate"> </b-form-rating>
        </div>
        <!-- 내용 --> 
        <div class="col-7">
          <input type="textarea" class="box-content-input" v-model="payload.content" value="payload.content">
        </div>
        <!-- 수정 / 삭제 -->
        <span class="col-2">
          <button @click="onUpdate" class="btn" style="background-color : #7C683C; color: #FFCC5B;">완료</button> |
          <button @click="switchIsEditing" class="btn" style="background-color : #7C683C; color: #FFCC5B;">취소</button>
        </span>
      </div>
    </div>
    <div v-if="!isEditing" class="main-div-reviewlistitem">
      <div class="row">
        <div class="col-1 name-revielistitem box-username">
        <!-- 네임 -->
          {{ review.user.username }}
        </div>
        <!-- 평점 -->
        <div class="col-2">
          <b-form-rating style="color: #FFCC5B; " id="rating-lg-no-border" no-border size="lg" v-model="payload.rate" value="payload.rate" readonly> </b-form-rating>
        </div>
        <!-- 내용 --> 
        <div class="col-7">
          <p class="comment-text"> {{ review.content }}</p>
        </div>
        <!-- 수정 / 삭제 -->
        <span class="col-2" >
          <div v-if="currentUser.username === review.user.username && !isEditing">
          <button @click="switchIsEditing" class="btn" style="background-color : #7C683C; color: #FFCC5B;">수정</button> |
          <button @click="deleteReview(payload)" class="btn" style="background-color : #7C683C; color: #FFCC5B;">삭제</button>
          </div>
        </span>
      </div>
    </div>

  </div>
</template>

<script>

import { mapGetters, mapActions } from 'vuex'

export default {
  name : 'ReviewListItem',
  props : { review : Object },
  data () {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie,
        reviewPk: this.review.pk,
        content: this.review.content,
        rate : this.review.rate,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      console.log(this.payload)
      this.updateReview(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.date-revielistitem{font-size: 11px}
.comment-text-revielistitem{font-size: 12px}
.fs-12-revielistitem{font-size: 12px}
.shadow-none-revielistitem{box-shadow: none}
.cursor-revielistitem{cursor: pointer}
.textarea-revielistitem{resize: none}
.review-item .row {
  align-items: center;
}
.comment-text {
  margin: 0;
}
</style>