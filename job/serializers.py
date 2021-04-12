from rest_framework import serializers 
from .models import Job, Category

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job 
        fields = '__all__'
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'