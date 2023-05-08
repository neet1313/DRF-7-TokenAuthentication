from rest_framework import viewsets
from API import serializers, models

# There are 4 ways to generate Token:
# 1. Admin Application
# 2. python manage.py drf_create_token <username> command
# 3. By exposing an API endpoint
# 4. Using signals


# ------- Model Serializer ------


class StudentViewset(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

# To install httpie command line tool-> pip install httpie
# Generating/Viewing Token for a user-> http POST http://127.0.0.1:8000/gettoken/ username='' pasword='' 