from rest_framework import serializers
from .models import Person, EmploymentDetails

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        exclude = ('employment_details','id','hours_per_week')
        
class EmploymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentDetails
        fields = '__all__'