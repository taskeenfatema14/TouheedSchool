from django.urls import path
from .views import *

urlpatterns = [
    path('boardmembers/', BoardMemberListCreate.as_view(), name='boardmember-list-create'),
    path('boardmembers/<int:pk>/', BoardMemberRetrieveUpdateDestroy.as_view(), name='boardmember-retrieve-update-destroy'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-retrieve-update-destroy'),
    path('mail-logs/', MailLogAPIView.as_view(), name='mail_logs'),

###################################################
    path('school', SchoolApi.as_view()),
    path('productput/<uuid:id>/', SchoolPutDeleteApi.as_view(), name='category-detail'),
]
