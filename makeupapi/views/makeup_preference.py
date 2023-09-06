from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from makeupapi.models import MakeupPreferences, ProductType

class MakeupPreferencesViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        makeup_preferences = MakeupPreferences.objects.get(pk=pk)
        serializer = MakeupPreferencesSerializer(makeup_preferences, many=False)
        return Response(serializer.data)

    def list(self, request):
        makeup_preferences = MakeupPreferences.objects.all()
        serializer = MakeupPreferencesSerializer(makeup_preferences, many=True)
        return Response(serializer.data)
    def create(self, request):
        makeup_preferences = MakeupPreferences.objects.create(
            label=request.data['label'],
            image=request.data['image'],
            product_type=ProductType.objects.get(pk=request.data['product_type'])
        )
        serializer = MakeupPreferencesSerializer(makeup_preferences, many=False)
        return Response(serializer.data)
    def update(self, request, pk=None):
        makeup_preferences = MakeupPreferences.objects.get(pk=pk)
        makeup_preferences.label = request.data['label']
        makeup_preferences.image = request.data['image']
        makeup_preferences.product_type = ProductType.objects.get(pk=request.data['product_type'])
        makeup_preferences.save()
        serializer = MakeupPreferencesSerializer(makeup_preferences, many=False)
        return Response(serializer.data)
    def destroy(self, request, pk=None):
        makeup_preferences = MakeupPreferences.objects.get(pk=pk)
        makeup_preferences.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class MakeupPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakeupPreferences
        fields = ('id', 'label', 'image', 'product_type')
        depth = 1
    
