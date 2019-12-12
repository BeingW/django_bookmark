from .models import *
from rest_framework import serializers

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        #Bookmark 모델을 api 로 내보낸다.
        model = Bookmark
        fields = '__all__'