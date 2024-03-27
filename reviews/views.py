from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


class BoardMemberListCreate(generics.ListCreateAPIView):
    queryset = BoardMember.objects.all()
    serializer_class = BoardMemberSerializer

class BoardMemberRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardMember.objects.all()
    serializer_class = BoardMemberSerializer

################################  REVIEW  ############################################################

class ReviewListCreateAPIView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class MailLogAPIView(APIView):
    def get(self, request):                                 
        try:
            mail_logs = MailLog.objects.all()
            serializer = MailLogSerializer(mail_logs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = MailLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            mail_log = MailLog.objects.get(pk=pk)
        except MailLog.DoesNotExist:
            return Response({"error": "Mail log does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MailLogSerializer(mail_log, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            mail_log = MailLog.objects.get(pk=pk)
        except MailLog.DoesNotExist:
            return Response({"error": "Mail log does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        mail_log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
