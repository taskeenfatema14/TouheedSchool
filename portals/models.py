from django.db import models
from .constants import POST, PUT, DELETE, GET, GETALL
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your models here.


# # Create your models here.

# class BaseModel(models.Model):
#     id         = models.UUIDField(default=uuid.uuid4,primary_key=True)
#     created_on = models.DateTimeField(auto_now_add=True,editable=False)
#     updated_on = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True
#         ordering = ("-created_on",)



class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True,editable=False, null = True, blank = True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_on",)


class BaseAPIView(APIView):
    allowed_methods = [GET, GETALL, POST, PUT, DELETE]
    search_ignore_fields = []
    archive_in_delete = False

    def get(self, request, id=None, *args, **kwargs):
        if id == "list":
            if not GETALL in self.allowed_methods:
                return Response({'msg': "Not Found"}, status=404)
            print("get all")
            pg = request.GET.get("pg") or 0
            limit = request.GET.get("limit") or 20
            search = request.GET.get('q', '')
            queryset = self.get_queryset()
            if search:
                queryset = queryset.filter(self.search_query_filter(search_query=search))
            for param in self.request.query_params:
                if param not in ['pg', 'q', 'limit']:
                    param_value = self.request.query_params[param]
                    if self.request.query_params[param] == 'true':
                        param_value = True
                    if self.request.query_params[param] == 'false':
                        param_value = False
                    queryset = queryset.filter(**{param: param_value})
            count = queryset.count()
            objs = queryset[
                int(pg) * int(limit) : (int(pg) + 1) * int(limit)
            ]
            return Response(
                data={"rows": self.serializer(objs, many=True).data, "count": count, **self.get_extra_list_data()},
                status=200,
            )
        else:
            if not GET in self.allowed_methods:
                return Response({'msg': "Method not allowed"}, status=405)
            print("get by id")
            try:
                return Response(
                    data=self.serializer(self.model.objects.get(id=id)).data,
                    status=200,
                )
            except (self.model.DoesNotExist, ValidationError):
                return Response(
                    data={
                        "msg": str(self.model._meta).split(".")[1]
                        + " object does not exists, Invalid ID"
                    },
                    status=400,
                )
