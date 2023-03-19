from rest_framework import serializers
from django.db.models.fields import TextField
from .models import *
# write sreializers from here

class Sigserializer(serializers.ModelSerializer):
    class Meta:
        model = Sig
        fields = '__all__'

class Teamserializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        
class Eventserializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'