from django.urls import path
from .views import * 
from .models import * 

urlpatterns = [     
        path('boardmembers/', BoardMemberListCreate.as_view(), name='boardmember-list-create'),
        path('boardmembers/<uuid:uuid>/', BoardMemberRetrieveUpdateDestroy.as_view(), name='boardmember-retrieve-update-destroy'),
        path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
        path('reviews/<uuid:uuid>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-retrieve-update-destroy'),
]