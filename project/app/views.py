from django.shortcuts import render
from .models import Cars

# Create your views here.


from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
class CarsSerializer(serializers.ModelSerializer):
  class Meta:
        model = Cars
        fields = ['id', 'name','color','type', 'con'],
        
class CarsViewsets(viewsets.ModelViewSet):
    serializer_class = CarsSerializer
    queryset = Cars.objects.all()



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cars', CarsViewsets)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
