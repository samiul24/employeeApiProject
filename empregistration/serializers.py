from .models import District, Thana, EmpDepartment, EmpDesignation, EmpBasicInfo, EmpSalary, EmpEducation
from rest_framework import serializers

class SerializerDistrict(serializers.ModelSerializer):
    class Meta:
        attribute=False
        model=District
        fields='__all__'

class SerializerEmpDepartment(serializers.ModelSerializer):
    class Meta:
        model=EmpDepartment
        fields='__all__'

