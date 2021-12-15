import re
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from myapp.models import Category
from myapp.serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



class CategoryListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        category = Category.objects.all()
        serializer= CategorySerializer(category, many=True)
        return Response(serializer.data)

class CategioryDetailView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer= CategorySerializer(category, many=False)
        return Response(serializer.data)    

class CategoryCreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        serializer= CategorySerializer(data=request.data)    
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)    
        else:
            return Response(serializer.errors)

class CategoryUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer= CategorySerializer(category, many=False)
        return Response(serializer.data) 
        
    def put(self, request, pk):
        category= Category.objects.get(pk=pk)            
        serializer= CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)    

    def patch(self, request, pk):
        category= Category.objects.get(pk=pk)            
        serializer= CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 


class CategoryDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def delete(self, request, pk):
        category= Category.objects.get(pk=pk) 
        category.delete()
        return Response("deleted")







