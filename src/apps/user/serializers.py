from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from apps.user.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    """ User registration serializer """
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name',
            'patronymic', 'avatar', 'position', 'salary',
            'age', 'department', 'password', 'password2',
        )
        extra_kwargs = {
            "salary": {'required': True},
            "age": {'required': True},
            "department": {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        attrs.pop('password2')
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name')

    class Meta:
        model = User
        fields = (
            'id', 'username', 'full_name', 'avatar', 'position', 'salary',
            'age', 'department'
        )
        extra_kwargs = {
            "full_name": {'read_only': True}
        }
