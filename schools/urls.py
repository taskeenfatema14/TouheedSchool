from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('boardmembers/', views.BoardMemberListCreate.as_view(), name='boardmember-list-create'),
    path('boardmembers/<int:pk>/', views.BoardMemberRetrieveUpdateDestroy.as_view(), name='boardmember-retrieve-update-destroy'),
    path('reviews/', views.ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-retrieve-update-destroy'),
]
=======
from .views import * 


urlpatterns = [
    path('school', SchoolApi.as_view()),
    path('productput/<uuid:id>/', SchoolPutDeleteApi.as_view(), name='category-detail'),

]
>>>>>>> 162d812960618f74654658bb586d0e08fda77e96
