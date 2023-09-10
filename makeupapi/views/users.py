from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
""" import auth.user model"""
from django.contrib.auth.models import User


class UserViewSet(ViewSet):

    def retrieve(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    
    def list(self, request):
        users = User.objects.all()
        if "current" in request.query_params:
            users = users.filter(pk=request.user.pk)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
