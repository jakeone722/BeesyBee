<template>
<div class="review-item">
  <div class="main-div-reviewlistitem">
      <div class="row">
        <span class="col-sm-0 col-md-3 name-revielistitem box-moviename">
    <router-link :to =" { name : 'detail', query : {id : review.movie_id} }" class="router-search" style="text-decoration: none">
        <!-- 네임 -->
          {{ review.movie }}
    </router-link>
        </span>
        <!-- 평점 -->
        <div class="col-sm-0 col-md-3">
          <b-form-rating style="color: #FFCC5B; padding:0em; " id="rating-lg-no-border" no-border size="lg" v-model="payload.rate" value="payload.rate" readonly> </b-form-rating>
        </div>
        <!-- 내용 --> 
        <div class="col-sm-0 col-md-6">
          <p class="comment-text"> {{ review.content }}</p>
        </div>
        <!-- 수정 / 삭제 -->
      </div>
    <hr style="color: #FFCC5B; height:0.2em;">
  </div>

</div>
</template>


<script>

export default {
  name : 'MypageReview',
  props : {
    review : Array
  },
  data () {
    return {
      payload: {
        movie: this.review.movie,
        reviewPk: this.review.pk,
        content: this.review.content,
        rate : this.review.rate,
      },
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
  font-family: 'Noto Sans KR', sans-serif; 
}

.box-moviename {
  font-family: 'Do Hyeon', sans-serif;
}
</style>