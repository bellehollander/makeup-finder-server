from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from makeupapi.models import ProductType


class ProductTypeViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        product_type = ProductType.objects.get(pk=pk)
        serializer = ProductTypeSerializer(product_type, many=False)
        return Response(serializer.data)

    def list(self, request):
        product_type = ProductType.objects.all()
        serializer = ProductTypeSerializer(product_type, many=True)
        return Response(serializer.data)

    def create(self, request):
        product_type = ProductType.objects.create(
            label=request.data['label'],
        )
        serializer = ProductTypeSerializer(product_type, many=False)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product_type = ProductType.objects.get(pk=pk)
        product_type.label = request.data['label']
        product_type.save()
        serializer = ProductTypeSerializer(product_type, many=False)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        product_type = ProductType.objects.get(pk=pk)
        product_type.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ('id', 'label')