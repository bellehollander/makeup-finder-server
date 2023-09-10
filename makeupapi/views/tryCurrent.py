
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from makeupapi.models import Profile
from rest_framework import serializers



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_profile(request):
    try:
        # Retrieve the current user's profile
        profile = Profile.objects.get(User=request.auth.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    except Profile.DoesNotExist:
        return Response({'detail': 'Profile not found for the current user.'}, status=status.HTTP_404_NOT_FOUND)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'User', 'makeup_skill')
        depth = 1
