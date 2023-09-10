from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from makeupapi.models import Product, MakeupPreferences

class ProductViewSet(ViewSet):

    def retrieve(self, request, pk=None):
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, many=False, context={'request': request})
            return Response(serializer.data)
    def list(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    def create(self, request):
        
       "create a product"
         
       product = Product.objects.create(
            label=request.data['label'],
            brand=request.data['brand'],
            price=request.data['price'],
            description=request.data['description'],
            image=request.data['image'],
            link=request.data['link'],
            makeup_preferences = MakeupPreferences.objects.get(pk=request.data['makeup_preferences'])
        )
       serializer = ProductSerializer(product, many=False)
       return Response(serializer.data)
    def update(self, request, pk=None):
        makeup_prefrences = MakeupPreferences.objects.get(pk=request.data['makeup_preferences'])
        product = Product.objects.get(pk=pk)
        product.label = request.data['label']
        product.brand = request.data['brand']
        product.price = request.data['price']
        product.description = request.data['description']
        product.image = request.data['image']
        product.link = request.data['link']
        product.makeup_preferences = makeup_prefrences
        product.save()
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    def destroy(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

        
class MakeupPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakeupPreferences
        fields = ('id', 'label', 'image', 'product_type')
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    makeup_preferences = MakeupPreferencesSerializer(many=False)
    class Meta:

        model = Product
        fields = ('id', 'label', 'brand', 'price', 'description', 'image', 'link', 'makeup_preferences')


        
        