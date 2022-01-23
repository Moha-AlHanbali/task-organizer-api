
import json
import datetime

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from .models import CustomUser
from rest_framework import serializers

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['age'] = json.dumps(user.age.__str__())
        return token

class AccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'},write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'},write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'age')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'age': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            age = validated_data['age']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
