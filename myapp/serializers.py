from rest_framework import serializers
from myapp.models import Category



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
        