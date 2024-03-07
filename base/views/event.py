from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse 

# DRF
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import Event
from base.serializers import EventSerializer

from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

# Create your views here.
def getRouter(request):
        return JsonResponse('Hello',safe=False)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAdminUser,)


@api_view(["GET"])
def getEventList(request):

        event = Event.objects.all()
        page = request.query_params.get('page')
        paginator = Paginator(event, 10)
        print('page : ', page)
        try:
                event = paginator.page(page)
        except PageNotAnInteger:
                event = paginator.page(1)
        except EmptyPage:
                event = paginator.page(paginator.num_pages)
        if page == None:
                page = 1 

        page = int(page)
        # event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response({'event' : serializer.data, 'page': page, 'pages': paginator.num_pages })

@api_view(["GET"])
def get_event_detail(request,pk):
        event = Event.objects.get(id=pk)
        serializier = EventSerializer(event,many=False)
        return Response(serializier.data)