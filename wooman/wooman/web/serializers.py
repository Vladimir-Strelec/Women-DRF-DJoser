from rest_framework import serializers

from wooman.web.models import WomanModel


class WomanSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = WomanModel
        fields = '__all__'

    # def create(self, validated_data):
    #     return WomanModel.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.context = validated_data.get('context', instance.context)
    #     instance.create_profile = validated_data.get('create_profile', instance.create_profile)
    #     instance.update_profile = validated_data.get('update_profile', instance.update_profile)
    #     instance.save()
    #     return instance
