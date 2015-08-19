from rest_framework import serializers

from .models import Tournament, Participant

class TournamentSerializer(serializers.ModelSerializer):
    team_string = serializers.StringRelatedField(source='tournament.name')

    class Meta:
        model = Tournament
        fields = ('pk', 'name')


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('pk', 'name')