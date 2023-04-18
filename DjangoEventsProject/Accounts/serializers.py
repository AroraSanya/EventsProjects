from rest_framework import serializers, status
from Events.models import *
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self,validated_data):
        user=super(UserSerializer,self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
            model = Profile
            fields = '__all__'
    def create(self, validated_data):
            user_data = validated_data.pop('user')
            user = UserSerializer.create(UserSerializer(), validated_data=user_data)
            register_user= Profile.objects.create(user=user,**validated_data)
            return register_user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password1 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password1')

    def validate(self, attrs):
        old_password=attrs.get('old_password')
        password1=attrs.get('password1')
        user=self.context.get('user')
        if not authenticate(username=user.username, password = old_password):
            raise serializers.ValidationError("Old password is wrong!!")
        else:
            user.set_password(password1)
            user.save()
        return attrs