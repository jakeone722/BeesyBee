<template>
   <div v-if="selectedVideo" class="embed-responsive embed-responsive-16by9">
       <iframe :src="videoUrl" frameborder="0" class="embed-responsive-item"></iframe>
   </div>
 </template>

 <script>
 export default {
   name: 'VideoComponent',
   props: {
     selectedVideo: Object
   },
   computed: {
     videoUrl: function () {
       const videoId = this.selectedVideo.id.videoId
       return `https:www.youtube.com/embed/${videoId}`
     }
   }

 }

 </script>

 <style>

 </style>