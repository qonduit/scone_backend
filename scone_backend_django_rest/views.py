from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from scone_backend_django_rest.serializers import UserSerializer, GroupSerializer, SchemesSerializer, OPPSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'SchemesList': '/schemes-list/',
        'SchemesAdd': '/schemes-add/',
        'OPPAdd': '/opp-add/',
    }

    return Response(api_urls)


@api_view(['GET'])
def SchemesList(request):
    schemes = Schemes.objects.all()
    serializer = SchemesSerializer(schemes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def SchemesAdd(request):
    serializer = SchemesSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def OPPAdd(request):
    serializer = OPPSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
