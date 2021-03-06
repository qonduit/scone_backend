from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SchemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schemes
        fields = '__all__'

class OPPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPP
        fields = '__all__'
