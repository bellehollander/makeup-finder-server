from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from makeupapi.models import ProductReview, Product, Profile


class ProductReviewViewSet(ViewSet):

    def retrieve(self, request, pk=None):
        product_review = ProductReview.objects.get(pk=pk)
        serializer = ProductReviewSerializer(product_review, many=False)
        return Response(serializer.data)


    def list(self, request):
        # Get the 'product_id' query parameter from the request
        product_id = request.query_params.get('product_id')

        # Check if the 'product_id' parameter is provided
        if product_id is not None:
            # Filter ProductReview instances based on the provided 'product_id'
            product_reviews = ProductReview.objects.filter(product_id=product_id)
        else:
            # If 'product_id' is not provided, return all ProductReview instances
            product_reviews = ProductReview.objects.all()

        serializer = ProductReviewSerializer(product_reviews, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        product_review = ProductReview.objects.create(
            profile=Profile.objects.get(User=request.auth.user),
            product=Product.objects.get(pk=request.data['product']),
            review=request.data['review'],
            rating=request.data['rating'],
        )
        serializer = ProductReviewSerializer(product_review, many=False)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        product_review = ProductReview.objects.get(pk=pk)
        product_review.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ('id', 'profile', 'product', 'review', 'rating')
        depth = 2
       