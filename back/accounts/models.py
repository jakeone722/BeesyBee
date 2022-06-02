from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


GENDER_CHOICES = [
		('M',  "남성"), 
		('F',  "여성")
		]

OCCUPATION_CHOICES = [
		(0, "기타"),
		(1, "교육자"),
		(2, "예술가"),
		(3, "사무관리직"),
		(4, "대학생/대학원생"),
		(5, "서비스업"),
		(6, "의사/의료계"),
		(7, "임원/관리자"),
		(8, "농부"),
		(9, "전업주부"),
		(10, "청소년/학생"),
		(11, "법조인"),
		(12, "프로그래머"),
		(13, "은퇴"),
		(14, "영업/마케팅"),
		(15, "과학자"),
		(16, "프리랜서"),
		(17, "기계공/엔지니어"),
		(18, "소상공인"),
		(19, "무직"),
		(20, "작가"),
		]

class User(AbstractUser):
	age = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
	gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='M')
	occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES, default=0)