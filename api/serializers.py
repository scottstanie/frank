# Serializers define how the API is presented.
# This file is imported into rest_api/viewsets.py

from rest_framework import serializers
from allauth.socialaccount.models import SocialToken
# Import your models to use with the API here:
from api.models import User, Question, Showdown, Friend
from rest_framework.authtoken.models import Token
# Import special API serializer mixins from api/mixins.py
from api.mixins import DynamicFieldsMixin


# Recursive Serializer, use for recursive models.
class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

# Serializers define the API representation.


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    friends = serializers.StringRelatedField(many=True, read_only=True)  # Prints names as str
    # friends = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # Prints ids
    date_joined = serializers.CharField(read_only=True)
    last_login = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'friends',
            'is_staff',
            'custom_data',
            'date_joined',
            'last_login'
        )


class TokenSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Token
        fields = ('key', 'user_id')


# Used only if Allauth is installed.
# Uncomment below to use in place of TokenSerializer:

class SocialTokenSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField('dynamic_user_id')
    key = serializers.SerializerMethodField('dynamic_key')

    def dynamic_user_id(self, token):
        user = self.context['request'].user
        if user is not None and not user.is_anonymous():
            return user.id

    def dynamic_key(self, token):
        return token.token

    class Meta:
        model = SocialToken
        fields = ('key', 'user_id')


class QuestionSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'title', 'description')


class ShowdownSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    rater = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    winner = serializers.PrimaryKeyRelatedField(queryset=Friend.objects.all())  # Prints names as str
    loser = serializers.PrimaryKeyRelatedField(queryset=Friend.objects.all())  # Prints names as str

    class Meta:
        model = Showdown
        fields = ('id', 'winner', 'loser', 'rater', 'question', 'created_at')


class FriendSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    source_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Friend
        fields = ('id', 'source_user', 'full_name', 'fb_source_user_id', 'invite_friend_id', 'facebook_id', 'image_url')
