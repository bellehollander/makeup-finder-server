from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from makeupapi.models import ProfilePreference, Profile, MakeupPreferences

class ProfilePreferencesViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        profile_preferences = ProfilePreference.objects.get(pk=pk)
        serializer = ProfilePreferencesSerializer(profile_preferences, many=False)
        return Response(serializer.data)

    def list(self, request):
        profile_preferences = ProfilePreference.objects.all()
        serializer = ProfilePreferencesSerializer(profile_preferences, many=True)
        return Response(serializer.data)

    def create(self, request):
        profile_preferences = ProfilePreference.objects.create(
        Profile = Profile.objects.get(pk=request.data['profile']),
         MakeupPreferences = MakeupPreferences.objects.get(pk=request.data['makeup_preferences'])
        )
        serializer = ProfilePreferencesSerializer(profile_preferences, many=False)
        return Response(serializer.data)

    def update(self, request, pk=None):
        profile_preferences = ProfilePreference.objects.get(pk=pk)
        profile_preferences.profile = Profile.objects.get(pk=request.data['profile'])
        profile_preferences.MakeupPreferences = MakeupPreferences.objects.get(pk=request.data['makeup_preferences'])
        serializer = ProfilePreferencesSerializer(profile_preferences, many=False)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        makeup_preferences = ProfilePreference.objects.get(pk=pk)
        makeup_preferences.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class MakeupPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakeupPreferences
        fields = ('id', 'label', 'image', 'product_type')
        depth = 1
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'User')
        depth = 1

class ProfilePreferencesSerializer(serializers.ModelSerializer):
    Profile = ProfileSerializer(many=False)
    MakeupPreferences  = MakeupPreferencesSerializer(many=False)

    class Meta:
        model = ProfilePreference
        fields = ('id', 'Profile', 'MakeupPreferences')