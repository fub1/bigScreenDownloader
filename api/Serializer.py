# api/serializers.py
from rest_framework import serializers
from clients.models import Client
from distributions.models import Apk


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'identifier', 'client_android_api', 'webview_version']


class ApkSerializer(serializers.ModelSerializer):
    apk_download_url = serializers.SerializerMethodField()

    class Meta:
        model = Apk
        fields = ['id', 'apk_file', 'apk_download_url']

    def get_apk_download_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.apk_file.url)
