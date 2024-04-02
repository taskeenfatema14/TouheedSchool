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
            return self.get_paginated_data(request)

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
        pg = request.GET.get("pg") or 0
        limit = request.GET.get("limit") or 20

        queryset = BoardMember.objects.all()
        count = queryset.count()
        objs = queryset[
            int(pg) * int(limit) : (int(pg)+1)*int(limit)
        ]
        serializer = BoardMemberSerializer(objs, many = True)

        return Response({
            "error" : False,
            "count":count,
            "rows" : serializer.data,
        }, status=status.HTTP_200_OK)
    
    def get(self, request):
        return self.get_paginated_data(request)
    
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
        pg = request.GET.get("pg") or 0
        limit = request.GET.get("limit") or 20

        queryset = Review.objects.all()
        count = queryset.count()
        objs = queryset[
            int(pg) * int(limit) : (int(pg)+1)*int(limit)
        ]
        serializer = ReviewSerializer(objs, many = True)

        return Response({
            "error" : False,
            "count":count,
            "rows" : serializer.data,
        }, status=status.HTTP_200_OK)
    
    def get(self, request):
        return self.get_paginated_data(request)

#################################################################################
