<template>
  <div>
    <!-- Beesy 소개 -->
    <div class="bg-light">
      <div class="container py-5">
        <div class="row h-100 align-items-center py-5">
          <div class="col-lg-6 about-beesy">
            <p> </p>
            <h1 class="display-4">About Beesy Movie</h1>
            <p class="lead text-muted mb-0"> 영화 찾기 귀찮고,</p>
            <p class="lead text-muted mb-0"> 볼 시간도 없는,</p>
            <p class="lead text-muted mb-0"> 현대인들을 위한 Beesy의 영화 추천 서비스</p>
          </div>
          <div class="col-lg-5 px-5 mx-auto order-1 order-lg-2"><img src="@/images/bee.png" alt="" class="img-fluid mb-4 mb-lg-0"></div>
        </div>
      </div>
    </div>
    <!-- MovieLens / Youtube -->
    <div class="bg-white py-5" >
      <div class="container py-5">
        <div class="row align-items-center mb-5" >
          <div class="col-lg-6 order-2 order-lg-1 about-beesy">
            <i class="about-i fa fa-database fa-2x mb-3 text-primary"></i>
            <h2 class="font-weight-light mb-4" >영화 찾을 시간이 없는 당신</h2>
            <p class=" text-muted mb-4">Beesy는 MovieLens의 100만개 데이터를 활용하여, </p>
            <p class=" text-muted mb-4">당신의 취향을 저격합니다.</p>
            <a href="https://grouplens.org/datasets/movielens/" target=”_blank” class="btn btn-light px-5 rounded-pill shadow-sm">Learn More</a>
          </div>
          <div class="col-lg-5 px-5 mx-auto order-1 order-lg-2"><img src="http://www.pontneo.com/ctf/movies/images/movielenslogo.jpg" alt="" class="img-fluid mb-4 mb-lg-0"></div>
        </div>
        <p style="height : 100px"></p>
        <div class="row align-items-center">
          <div class="col-lg-5 px-5 mx-auto"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Logo_of_YouTube_%282011-2013%29.svg/800px-Logo_of_YouTube_%282011-2013%29.svg.png" alt="" class="img-fluid mb-4 mb-lg-0" style="width:300px"></div>
          <div class="col-lg-6 about-beesy">
            <i class="about-i fa-solid fa-stopwatch fa-2x mb-3 text-primary"></i>
            <h2 class="font-weight-light mb-4" >찾은 영화 볼 시간이 없는 당신</h2>
            <p class=" text-muted mb-4"> 안 본 영화도 본 척할 수 있게, </p>
            <p class=" text-muted mb-4">Beesy는 유튜브 리뷰 영상을 함께 보여드립니다.</p>
          </div>
        </div>
      </div>
    </div>
    <!-- Our team -->
    <div class="bg-light py-5">
      <div class="container py-5">
        <div class="row mb-4 justify-content-center">
          <div class="col-lg-5 about-beesy">
            <h2 class="display-4 font-weight-light">Our team</h2>
            <p class=" text-muted">SSAFY의 두 꿈나무를 소개합니다.</p>
          </div>
        </div>
        <div class="row text-center">
          <div class="col-xl-3 col-sm-6 mb-5">
          </div>
          <div class="col-xl-3 col-sm-6 mb-5 about-beesy">
            <div class="bg-white rounded shadow-sm py-5 px-4"><img src="https://bootstrapious.com/i/snippets/sn-about/avatar-3.png" alt="" width="100" class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm">
              <h5 class="mb-0">Jake Jeon</h5><span class="small text-uppercase text-muted last-word">"이게 된다고?"</span>
              <ul class="social mb-0 list-inline mt-3">
                <li class="list-inline-item"><a href="#" class="social-link"><i class="fa-brands fa-facebook-f"></i></a></li>
                <li class="list-inline-item"><a href="#" class="social-link"><i class="fa-brands fa-twitter"></i></a></li>
                <li class="list-inline-item"><a href="#" class="social-link"><i class="fa-brands fa-instagram"></i></a></li>
                <li class="list-inline-item"><a href="#" class="social-link"><i class="fa-brands fa-linkedin"></i></a></li>
              </ul>
            </div>
          </div>
          <!-- End-->

          <!-- Team item-->
          <div class="col-xl-3 col-sm-6 mb-5 about-beesy">
            <div class="bg-white rounded shadow-sm py-5 px-4"><img src="https://bootstrapious.com/i/snippets/sn-about/avatar-2.png" alt="" width="100" class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm">
              <h5 class="mb-0">Yosung Moon</h5><span class="small text-uppercase text-muted last-word">"금쪽같은 내 새끼"</span>
              <ul class="social mb-0 list-inline mt-3">
                <li class="list-inline-item"><a href="#" class="social-link"><i class="fa-brands fa-facebook-f"></i></a></li>
                <li class="list-inline-item"><a href="#" class="social-link"><i class="fa-brands fa-twitter"></i></a></li>
                <li class="list-inline-item"><a href="#" class="social-link"><i class="fa-brands fa-instagram"></i></a></li>
                <li class="list-inline-item"><a href="#" class="social-link"><i class="fa-brands fa-linkedin"></i></a></li>
              </ul>
            </div>
          </div>
          <!-- End-->

          <!-- Team item-->
          <div class="col-xl-3 col-sm-6 mb-5">

          </div>
          <!-- End-->

        </div>
      </div>
    </div>
    <!-- Footer  -->
    <footer class="bg-light pb-5">
      <div class="container text-center about-beesy">
        <p class=" text-muted mb-0">&copy; Copyrights Beesy.com All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>



<script>
export default {
    metaInfo: {
    title: 'ABOUT US | BEESY',
    titleTemplate: 'BEESY | ABOUT US',
    meta: [
      {http_equiv: 'Content-Type', content: 'text/html; charset=utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1.0,maximum-scale=2.0'},
      {name: 'description', content: 'Beesy Movie는 SSAFY 7기 교육생들이 만든 페이지입니다.'}
    ]
  }
}
</script>



<style>
.about-i {
  color: #FFCC5B
}

.about-beesy {
  font-family: 'Do Hyeon', sans-serif;
}

.text-muted {
  font-size: 1.5em;
}
.last-word {
  font-size: 3em;
}
</style>