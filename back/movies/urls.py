from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('gender/<str:username>/', views.gender_list, name='gender'),
    path('occupation/<str:username>/', views.occupation_list, name='occupation'),
    path('age/<str:username>/', views.age_list, name='age'),
    path('search/<str:movie_title>/', views.search, name='search'),
    path('detail/<int:movie_id>/', views.detail, name='detail'),
    path('review/<int:movie_id>/create/', views.review_create, name='review_create'),
    path('review/<int:review_id>/delete/', views.review_delete, name='review_delete'),
    path('review/<int:review_id>/update/', views.review_update, name='review_update'),
    path('costeffective/', views.costeffective_list, name='costeffective')
    ]
