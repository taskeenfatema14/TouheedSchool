from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class BoardMemberAPI(APIView):
    def get(self, request, uuid=None):
        if uuid:
            return self.retrieve(request, uuid)
        else:
            return self.list(request)

    def list(self, request):
        board_members = BoardMember.objects.all()
        serializer = BoardMemberSerializer(board_members, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoardMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, uuid):
        try:
            return BoardMember.objects.get(id=uuid)
        except BoardMember.DoesNotExist:
            raise Http404

    def retrieve(self, request, uuid):
        board_member = self.get_object(uuid)
        serializer = BoardMemberSerializer(board_member)
        return Response(serializer.data)

    def put(self, request, uuid):
        board_member = self.get_object(uuid)
        serializer = BoardMemberSerializer(board_member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        board_member = self.get_object(uuid)
        board_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def get_paginated_data(self, request):
        limit = max(int(request.GET.get('limit', 0)), 4)  
        page_number = max(int(request.GET.get('page', 0)), 1)
        
        queryset = BoardMember.objects.all()
    
################################  REVIEW  ############################################################
class ReviewAPI(APIView):
    def get(self, request, uuid=None):
        if uuid:
            return self.retrieve(request, uuid)
        else:
            return self.list(request)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, uuid):
        try:
            return Review.objects.get(id=uuid)
        except Review.DoesNotExist:
            raise Http404

    def list(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, uuid):
        review = self.get_object(uuid)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def delete(self, request, uuid):
        review = self.get_object(uuid)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_paginated_data(self, request):
        limit = max(int(request.GET.get('limit', 0)), 4)  
        page_number = max(int(request.GET.get('page', 0)), 1)
        
        queryset = Review.objects.all()


#################################################################################
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
