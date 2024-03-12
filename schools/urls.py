from django.urls import path
from .views import * 


urlpatterns = [
    path('school', SchoolApi.as_view()),
    path('productput/<uuid:id>/', SchoolPutDeleteApi.as_view(), name='category-detail'),

]