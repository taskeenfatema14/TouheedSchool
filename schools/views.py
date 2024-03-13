# views.py
from rest_framework import generics
from .models import *
from .serializers import *

class BoardMemberListCreate(generics.ListCreateAPIView):
    queryset = BoardMember.objects.all()
    serializer_class = BoardMemberSerializer

class BoardMemberRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardMember.objects.all()
    serializer_class = BoardMemberSerializer

################################REVIEW############################################################

class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
