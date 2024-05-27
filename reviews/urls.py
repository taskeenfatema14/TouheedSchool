from django.urls import path
from .views import * 
from .models import * 

urlpatterns = [     
        path('boardmembers/', BoardMemberAPI.as_view(), name='boardmember-list-create'),
        path('boardmembers/<uuid>/', BoardMemberAPI.as_view(), name='boardmember-retrieve-update-destroy'),

        path('reviewlist/', ReviewAPI.as_view(), name='review-list-create'),
        path('reviewedit/<uuid>/', ReviewAPI.as_view(), name='review-retrieve-update-destroy'),
]