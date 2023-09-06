from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from makeupapi.models import Wishlist, Profile, Product

class WishlistViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        wishlist = Wishlist.objects.get(pk=pk)
        serializer = WishlistSerializer(wishlist, many=False)
        return Response(serializer.data)

    def list(self, request):
        wishlist = Wishlist.objects.all()
        serializer = WishlistSerializer(wishlist, many=True)
        return Response(serializer.data)

    def create(self, request):
        wishlist = Wishlist.objects.create(
            profile = Profile.objects.get(pk=request.data['profile']),
            product = Product.objects.get(pk=request.data['product'])
        )
        serializer = WishlistSerializer(wishlist, many=False)
        return Response(serializer.data)

    def update(self, request, pk=None):
        wishlist = Wishlist.objects.get(pk=pk)
        wishlist.profile = Profile.objects.get(pk=request.data['profile'])
        wishlist.product = Product.objects.get(pk=request.data['product'])
        wishlist.save()
        serializer = WishlistSerializer(wishlist, many=False)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        wishlist = Wishlist.objects.get(pk=pk)
        wishlist.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ('id', 'profile', 'product')
        depth = 1