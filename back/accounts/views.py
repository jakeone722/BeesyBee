from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from movies.models import Movie
# from ..movies.serializers import ReviewSerializer

User = get_user_model()

@api_view(['POST'])
def profile(request):
    reviews = request.user.review_set.all()
    # 리스트 안에 딕셔너리겠죠
    # 리스트 순회
    review_list = []

    for review in reviews:
        context = {}
        context['id'] = review.id
        context['movie_id'] = review.movie_id
        context['movie'] = Movie.objects.get(id = review.movie.id).title
        context['rate'] = review.rate
        context['content'] = review.content
        review_list.append(context)

    user_info = {
        'username': request.user.username,
        'age': request.user.age,
        'gender': request.user.gender,
        'occupation': request.user.occupation,
        'review_list' : review_list
    }
    return JsonResponse(user_info)


@api_view(['PUT'])
def update(request):
    user = User.objects.get(username=request.user)
    reviews = request.user.review_set.all()
    review_list = []

    for review in reviews:
        context = {}
        context['id'] = review.id
        context['movie_id'] = review.movie_id
        context['movie'] = Movie.objects.get(id = review.movie.id).title
        context['rate'] = review.rate
        context['content'] = review.content
        review_list.append(context)
    
    user.age = request.data.get('age')
    user.gender = request.data.get('gender')
    user.occupation = request.data.get('occupation')
    user.save()
    user_info = {
        'username': user.username,
        'age': user.age,
        'gender': user.gender,
        'occupation': user.occupation,
        'review_list' : review_list
    }

    return JsonResponse(user_info)
