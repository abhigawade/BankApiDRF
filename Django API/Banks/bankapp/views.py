from django.shortcuts import render
from .serializers import BankModelSerializer
from .models import BankModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,  AllowAny
from rest_framework.authentication import BasicAuthentication

# Create your views here.
class BankModelView(APIView):
    """
    Bank Model View
    """
    authentication_classes = [BasicAuthentication]
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def get(self, request, format=None, pk=None):
        if pk is not None:
            bank = BankModel.objects.get(pk=pk)
            serializer = BankModelSerializer(bank)
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        else:
            banks = BankModel.objects.all()
            serializer = BankModelSerializer(banks, many=True)
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = BankModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None, pk=None):
        bank = BankModel.objects.get(pk=pk)
        bank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, format=None, pk=None):
        bank = BankModel.objects.get(pk=pk)
        serializer = BankModelSerializer(bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)