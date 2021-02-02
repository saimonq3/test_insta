from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from . import serializers
from .filters import PhotoFilter
from .models import Photo


class RegisterView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response()


class PhotoView(ModelViewSet):
    serializer_class = serializers.PhotoSerializer
    filter_backends = DjangoFilterBackend,
    filter_class = PhotoFilter

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        photo = self.get_object()
        photo.views += 1
        photo.save()
        return response


    def get_queryset(self):
        return Photo.objects.filter(user=self.request.user).all()
    #
    # @action(detail=False)
    # def top_10(self, request):
    #     return Response({'ololo': 123})
