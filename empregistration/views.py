from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from .models import District, EmpDepartment
from .serializers import SerializerDistrict, SerializerEmpDepartment

# Create your views here.

class Districts(APIView):
    def get(self, request):
        districts=District.objects.all()
        print(districts)
        serializer=SerializerDistrict(districts, many=True)
        return Response(serializer.data)

    def post(self, request):
        data=request.data
        data=data["name"]
        print(data)
        global dist
        distname=District.objects.filter(name=data)
        """distname1=district.objects.filter(name=data).count()
        print(distname1)"""
        """for dist in distname:
            dist=dist.name
            print(dist)"""
        if dataname is None:
            serializer=SerializerDistrict(data=request.data)
            print(serializer)
            print(type(request.data))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Nessage":"Duplicate name is not allowed"},status=status.HTTP_406_NOT_ACCEPTABLE)
    
class District(APIView):
    def get_object(self, pk):
        try:
            return District.objects.get(pk=pk)
        except District.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        district=self.get_object(pk)
        serializer=serializerdistrict(district)
        return Response(serializer.data)



class EmpDepartment(APIView):
    def get(self, request):
        department=EmpDepartment.objects.all()
        print(department)
        serializer=SerializerEmpDepartment(department, many=True)
        return Response(serializer.data)
    


        

