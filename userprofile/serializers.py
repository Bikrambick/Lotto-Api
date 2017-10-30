from rest_framework import serializers 
from .models import User
from django.shortcuts import get_object_or_404
from .models import UserProfile
from django.contrib.auth.models import Group

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    address = serializers.CharField(source='profile.address', allow_blank=True, required=False)
    avatar = serializers.ImageField(source='profile.avatar', required=False, allow_null=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'avatar', 'username', 'email', 'first_name', 'last_name', 'password', 'address', 'groups')
        extra_kwargs = {'url': {'view_name': 'users:user_detail'}}
    
    def create(self, data):

        user = User.objects.create(
            email = data['email'],
            username = data['username'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            password = data['password'],
        )

        profile_data = data.pop('profile')

        profile = UserProfile.objects.create(
            user = user,
            avatar = profile_data['avatar'],
            address = profile_data['address']
        )

        return user
