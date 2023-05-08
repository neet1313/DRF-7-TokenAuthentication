from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('api', views.StudentViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/', obtain_auth_token)
]
