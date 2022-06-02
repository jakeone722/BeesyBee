<template>
  <div class="m-5">
    <review-list-item class=""
          v-for="review in reviews"
          :key="review.id"
          :review="review">
    </review-list-item>
    <review-list-form class="">
      
    </review-list-form>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
import ReviewListForm from '@/components/ReviewListForm.vue'

export default {
  name : 'ReviewList',
  components : {
    ReviewListItem,
    ReviewListForm
  },
  props : { reviews : Array },
  
}
</script>

<style>
.review-list {
  border : 5px dotted #7C683C;
}

</style>