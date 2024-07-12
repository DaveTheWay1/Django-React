from django.contrib.auth.models import User 
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "username", "password"]
                                # this tells django that we only want to accept a password
                                # not return; no one can read what the password is,
    extra_kwargs = {"password":{"write_only":True}}

  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user
  
class NoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Note
    fields = ["id", "title", "content", "created_at", "author"]
    extra_kwargs = {"author":{"read_only":True}} # this is so because we are manually setting who the author is and do not want to have someone write in who the author is