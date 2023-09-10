from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from makeupapi.models import Tips, MakeupSkill


class TipsViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        tips = Tips.objects.get(pk=pk)
        serializer = TipsSerializer(tips, many=False)
        return Response(serializer.data)

    def list(self, request):
        tips = Tips.objects.all()
        serializer = TipsSerializer(tips, many=True)
        return Response(serializer.data)

    def create(self, request):
        makeup_skill = MakeupSkill.objects.get(pk=request.data['makeup_skill'])
        tips = Tips.objects.create(
            label=request.data['label'],
            description=request.data['description'],
            image=request.data['image'],
            makeup_skill = makeup_skill
        )
        serializer = TipsSerializer(tips, many=False)
        return Response(serializer.data)

    def update(self, request, pk=None):
        tips = Tips.objects.get(pk=pk)
        tips.label = request.data['label']
        tips.description = request.data['description']
        tips.image = request.data['image']
        tips.makeup_skill = MakeupSkill.objects.get(pk=request.data['makeup_skill'])
        tips.save()
        serializer = TipsSerializer(tips, many=False)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        tips = Tips.objects.get(pk=pk)
        tips.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class MakeupSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakeupSkill
        fields = ('id', 'label')
class TipsSerializer(serializers.ModelSerializer):
    makeup_skill = MakeupSkillSerializer(many=False)
    class Meta:
        model = Tips
        fields = ('id', 'label', 'description', 'image', 'makeup_skill')