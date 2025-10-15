from rest_framework import serializers
from .models import User, Organizer, Event

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'role')


class EventSerializer(serializers.ModelSerializer):
    organizer_name = serializers.CharField(source='organizer.org_name', read_only=True)
    
    class Meta:
        model = Event
        fields = ('id', 'title', 'location', 'start_date', 'end_date', 'organizer', 'organizer_name')


class OrganizerSerializer(serializers.ModelSerializer):
    events = EventSerializer(source='events', many=True, read_only=True)
    
    class Meta:
        model = Organizer
        fields = ('id', 'user', 'org_name', 'contact_no', 'web', 'events')
