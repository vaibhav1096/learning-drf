from rest_framework import serializers

from .models import Team, Player


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'nickname', 'founded')
        read_only_fields = ('id',)


class NewTeamSerializer(TeamSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name',)


class PlayerSerializer(serializers.ModelSerializer):
    team = NewTeamSerializer()

    class Meta:
        model = Player
        fields = ('id', 'name', 'jersey_number', 'team')
        read_only_fields = ('id',)

    def update(self, instance, validated_data):
        team = validated_data.pop('team')
        super().update(instance, validated_data)

        for i in team:
            print(i)
        return instance
