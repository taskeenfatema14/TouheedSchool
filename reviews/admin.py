from django.contrib import admin
from .models import *
from .serializers import *

# Register your models here.
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'title') 

admin.site.register(BoardMember, BoardMemberAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'school')  

admin.site.register(Review, ReviewAdmin)