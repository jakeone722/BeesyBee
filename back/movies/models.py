from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


# Create your models here.

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    adult = models.CharField(max_length=50)
    budget = models.IntegerField()
    backdrop_path = models.TextField()
    genres = models.TextField()
    runtime = models.IntegerField()
    tagline = models.TextField()
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.CharField(max_length=100)
    vote_average = models.IntegerField()
    poster_path = models.TextField()
    revenue = models.IntegerField()

# detail 조회

# MOVIE_FEMALE = 20개 * tmdb추천 영화를 20* 20 400개 *20 8000개
# Movie_M
# 성별2 
# 직업20
# 연령6

# 메인페이지 

# 성별 추천
# 남자일 경우랑
#  영화 아이디로 TMDB api 추천 조회
#  영화목록
#  보내기
# 여자일 경우


# 서치

# 서치 검색한 영화 평점
# 서치의 경우에는 TMDB 보내고
#     있으면 모델에 추가

# 댓글 모델 추가
# 게시글
# 작성자
# 내용
# 평점
# 생성일
# 수정일


class Moviedata(models.Model):
    movieId = models.IntegerField(primary_key=True)
    tmdbId = models.IntegerField()
#     genres = models.CharField(max_length=100)



# class Userdata(models.Model):
#     id = models.IntegerField(primary_key=True)
#     gender = models.CharField(max_length=100)
#     age = models.IntegerField()
#     occupation = models.IntegerField()
#     movie_rate = models.ManyToManyField(Moviedata, through='Rate')



# class Rate(models.Model):
#     user = models.ForeignKey(Userdata, on_delete=models.CASCADE)
#     movie = models.ForeignKey(Moviedata, on_delete=models.CASCADE)
#     rate = models.IntegerField()
    

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rate = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(5)])
    content = models.CharField(max_length=400)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    