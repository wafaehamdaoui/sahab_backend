from rest_framework import serializers
from .models import Counter, Report, Image
from django.contrib.auth.models import User

class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = ('__all__')
    
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('__all__')

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('__all__')
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')