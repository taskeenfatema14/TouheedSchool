from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from events.models import *
from services.models import *


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        exclude = ['created_on','updated_on']      

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class InfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Infrastructure
        fields = ['id','school','image','title']

class InfrastructurePutSerializer(ModelSerializer):
    class Meta:
        model = Infrastructure
        fields = '__all__'
        extra_kwargs = {
            'title': {'required': False},
            'school': {'required': False}
        }

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model  = FrequentlyAskedQuestion
        fields = ['id','school','question','answer']

class NoticeBoardImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeboardImage
        fields = ['image']

class NoticeBoardSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()  
    class Meta:
        model = Noticeboard
        fields = ['id','school', 'title', 'images']

    def get_images(self, obj):
        images = NoticeboardImage.objects.filter(noticeboard=obj)
        return NoticeBoardImageSerializer(images, many=True).data


class EventImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImages
        fields = ['image']

class SchoolEventSerializer(serializers.ModelSerializer):
    # images = EventImagesSerializer(many=True, read_only=True)

    class Meta: 
        model = Event
        fields = ['id','title', 'date', 'time', 'location', 'desc', 'thumbnail']


class BrochureSchooolSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Brochure
        fields = ['id', 'pdf','description']

class SchoolDetailSerializer(serializers.ModelSerializer):
    infrastructure    = InfrastructureSerializer(many=True)
    faq               = FaqSerializer(many=True, source='frequentlyquestion_set')
    noticeboard       = NoticeBoardSerializer(many=True, source='notice_board_set')
    noticeboard_image = NoticeBoardImageSerializer(many=True, read_only=True,source='notice_board_image_set')
    events            = SchoolEventSerializer(many=True,source='event_set')
    brochure          = BrochureSchooolSerializer(many=True, source='brochure_set')

    class Meta:
        model = School
        fields = ['name', 'location', 'image', 'video', 'description', 'summary','logo', 
                'infrastructure', 'faq','noticeboard','noticeboard_image', 'events','brochure', 'school_email','contact_no']

class AdditionalConceptSerializer1(serializers.ModelSerializer):
    class Meta:
        model  = AdditionalConcept
        fields = ['school','id','logomark','title']

class AdditionalConceptSerializer2(serializers.ModelSerializer):
    class Meta:
        model  = AdditionalConcept
        fields = ['school','id','title','image','description']

class AboutUsSerializer(serializers.ModelSerializer):
    infrastructure     = InfrastructureSerializer(many=True)
    additional_concept = AdditionalConceptSerializer1(many=True, source='additionalconcept_set')
    detail_additional_concept = AdditionalConceptSerializer2(many=True, source='additionalconcept_set')

    class Meta:
        model = School
        fields = ['image', 'video', 'name', 'description','summary','vision','mission','aim',
                'transportation','infrastructure','additional_concept','detail_additional_concept', 'logo']

