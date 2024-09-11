from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .const import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg, Count
from .models import *
from .serialiser import PersonSerializer, EmploymentDetailsSerializer

class CustomPagination(LimitOffsetPagination):
    default_limit = PAGINATION_DEFAULT_LIMIT
    limit_query_param = PAGINATION_LIMIT_QUERY_PARAM
    offset_query_param = PAGINATION_OFFSET_QUERY_PARAM
    
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = CustomPagination

    @action(detail=False, methods=['get'], url_path='age-filter')
    def filter_by_age(self, request):
        age = request.query_params.get('age')
        age = int(age)

        persons = self.queryset.filter(age=age)
        page = self.paginate_queryset(persons)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(persons, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='occupation-filter')
    def filter_by_occupation(self, request):
        occupation = request.query_params.get('occupation')
        employees = self.queryset.filter(employment_details__occupation=occupation)
        page = self.paginate_queryset(employees)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(employees, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='education-filter')
    def filter_by_education(self, request):
        education = request.query_params.get('education')
        employees = self.queryset.filter(employment_details__education=education)
        page = self.paginate_queryset(employees)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(employees, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='avg-age')
    def avg_age(self, request):
        occupation = request.query_params.get('occupation')
        avg_age = self.queryset.filter(employment_details__occupation=occupation).aggregate(Avg('age'))
        avg_age_value = avg_age['age__avg']
        
        if avg_age_value is not None:
            avg_age_value = round(avg_age_value, 2)
        
        return Response({"average_age": avg_age_value})

    @action(detail=False, methods=['get'], url_path='group-by-country')
    def group_by_country(self, request):
        countries = self.queryset.values('native_country').annotate(count=Count('id'))
        page = self.paginate_queryset(countries)
        if page is not None:
            return self.get_paginated_response(page)
        
        return Response(countries)
    
    @action(detail=False, methods=['get'], url_path='top-capital-gain')
    def top_capital_gain(self, request):
        top_gain = self.queryset.order_by('-capital_gain')
        serializer = self.get_serializer(top_gain, many=True)
        page = self.paginate_queryset(top_gain)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)

    
    @action(detail=False, methods=['get'], url_path='order-by-age')
    def order_by_age(self, request):
        persons = self.queryset.order_by('-age')
        page = self.paginate_queryset(persons)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(persons, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='count-males-by-age')
    def count_males_by_age(self, request):
        age = request.query_params.get('age')
        males_count = self.queryset.filter(age=age, sex='Male').count()
        return Response({"age": age, "males_count": males_count})

    @action(detail=False, methods=['get'], url_path='count-females')
    def count_females_by_age(self, request):
        females_count = self.queryset.filter(sex='Female').count()
        return Response({"females_count": females_count})
    
    @action(detail=False, methods=['get'], url_path='get_employement_details')
    def get_employement_details_by_person_id(self, request, pk=None):
        id = request.query_params.get('id')
        if id is None:
            return Response(status=400,data={"error": "id is required"})
        
        if Person.objects.filter(id=id).count() == 0:
            return Response(status=404,data={"error": "Person not found"})
        
        employment_details = self.queryset.get(id=int(id)).employment_details
        return Response(EmploymentDetailsSerializer(employment_details).data)
        
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = EmploymentDetails.objects.all()
    serializer_class = EmploymentDetailsSerializer
    pagination_class = CustomPagination