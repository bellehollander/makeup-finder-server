from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from makeupapi.models import MakeupSkill


class MakeupSkillViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        makeup_skill = MakeupSkill.objects.get(pk=pk)
        serializer = MakeupSkillSerializer(makeup_skill, many=False)
        return Response(serializer.data)

    def list(self, request):
        makeup_skill = MakeupSkill.objects.all()
        serializer = MakeupSkillSerializer(makeup_skill, many=True)
        return Response(serializer.data)

    def create(self, request):
        makeup_skill = MakeupSkill.objects.create(
            label=request.data['label']
        )
        serializer = MakeupSkillSerializer(makeup_skill, many=False)
        return Response(serializer.data)

    def update(self, request, pk=None):
        makeup_skill = MakeupSkill.objects.get(pk=pk)
        makeup_skill.label = request.data['label']
        makeup_skill.save()
        serializer = MakeupSkillSerializer(makeup_skill, many=False)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        makeup_skill = MakeupSkill.objects.get(pk=pk)
        makeup_skill.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
class MakeupSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakeupSkill
        fields = ('id', 'label')