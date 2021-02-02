import re

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import Photo


class RegisterSerializer(serializers.Serializer):
    def login_validator(value):
        if not re.match('^[a-z0-9]{3,32}$', string=value, flags=re.IGNORECASE):
            raise ValidationError('Логин должен состоять из латинских цифробукв')
        if User.objects.filter(username__iexact=value):
            raise ValidationError('Такой логин уже занят')

    def email_validator(value):
        if User.objects.filter(email__iexact=value):
            raise ValidationError('Такая почта уже зарегистрирована')

    username = serializers.CharField(max_length=32, validators=[login_validator])
    email = serializers.EmailField(max_length=50, validators=[email_validator])
    password = serializers.CharField(max_length=20, validators=[validate_password])

    def save(self):
        User.objects.create_user(
            username=self.validated_data['username'],
            password=self.validated_data['password'],
            email=self.validated_data['email']
        )


class PhotoSerializer(serializers.ModelSerializer):
    date_add = serializers.DateTimeField(read_only=True)
    preview = serializers.SerializerMethodField()

    def get_preview(self, obj: Photo):
        try:
            path = self.context['request'].build_absolute_uri(obj.img).split('.')

            path[-2] += '_preview'
            return '.'.join(path)
        except:
            return None

    def get_username(self, obj):
        return obj.user.username

    username = serializers.SerializerMethodField("get_username")

    class Meta:
        model = Photo
        fields = 'id', 'name', 'img', 'views', 'date_add', 'username', 'preview'

    def create(self, validated_data):
        validated_data['user'] = self.context['view'].request.user
        return super().create(validated_data)
