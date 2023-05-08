from rest_framework import viewsets
from API import serializers, models


# To generate token on our own -> python manage.py drf_create_token <user_name>


# ------- Model Serializer ------


class StudentViewset(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

# To install httpie command line tool-> pip install httpie
# Generating Token for a user-> http POST http://127.0.0.1:8000/gettoken/ username='' pasword='' 