from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from makeupapi.models import Profile, MakeupSkill
from django.contrib.auth.models import User


class ProfileViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        profile = []
        profile = Profile.objects.get(pk=pk)
        if "current" in request.query_params:
            profile = Profile.objects.get(user=request.auth.user)
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)

    def list(self, request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def create(self, request):
      
        profile = Profile.objects.create(
            User=request.auth.user,
            makeup_skill= MakeupSkill.objects.get(pk=request.data['makeup_skill'])
        )
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)

    def update(self, request, pk=None):
        profile = Profile.objects.get(pk=pk)
        profile.User = request.data['user']
        profile.makeup_skill = MakeupSkill.objects.get(pk=request.data['makeup_skill'])
        profile.save()
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        profile = Profile.objects.get(pk=pk)
        profile.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'User', 'makeup_skill')
        depth = 1