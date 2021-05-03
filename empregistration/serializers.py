from .models import district, thana, empdepartment, empdesignation, empbasicinfo, empsalary, empeducation
from rest_framework import serializers

class serializerdistrict(serializers.ModelSerializer):
    class Meta:
        model=district
        fields='__all__'

