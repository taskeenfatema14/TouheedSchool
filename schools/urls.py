from django.urls import path
from . import views

urlpatterns = [
    path('boardmembers/', views.BoardMemberListCreate.as_view(), name='boardmember-list-create'),
    path('boardmembers/<int:pk>/', views.BoardMemberRetrieveUpdateDestroy.as_view(), name='boardmember-retrieve-update-destroy'),
    path('reviews/', views.ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-retrieve-update-destroy'),
]
