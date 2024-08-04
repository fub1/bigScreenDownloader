from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from clients.models import Client, ClientLog
from datetime import timedelta
from terminals.models import TerminalClientBinding, Terminal, TerminalApkDistribution
from distributions.models import Apk


class ClientApiEndpoint(APIView):
    def post(self, request, *args, **kwargs):
        identifier = request.data.get('identifier')
        android_api = request.data.get('android_api')
        client_ip = request.META.get('REMOTE_ADDR', '')
        webview_version = request.data.get('webview_version')

        response_data = {
            'client_id': None,
            'terminal_id': None,
            'apk_name': None,
            'apk_download_url': None
        }

        # Ensure identifier is provided
        if not identifier:
            return Response(response_data)

        # 查询客户端是否存在
        client, created = Client.objects.get_or_create(
            identifier=identifier,
            defaults={
                'client_android_api': android_api,
                'webview_version': webview_version
            }
        )
        response_data['client_id'] = client.id

        # 创建客户端日志, 过去1小时内的日志不再记录
        if not ClientLog.objects.filter(logged_at__gte=timezone.now() - timedelta(hours=1),
                                        client_id=response_data['client_id']).exists():
            ClientLog.objects.create(client_id=response_data['client_id'], ip=client_ip)

        # 查询客户端对应的终端信息
        terminal_client_binding = TerminalClientBinding.objects.filter(
            client_id=response_data['client_id'],
            start_date__lte=timezone.now(),
            end_date__gte=timezone.now()
        ).first()

        if terminal_client_binding:
            response_data['terminal_id'] = terminal_client_binding.terminal_id

            # 查询终端对应的APK信息
            terminal_apk_distribution = TerminalApkDistribution.objects.filter(
                terminal_id=response_data['terminal_id']
            ).first()
            if terminal_apk_distribution:
                apk = terminal_apk_distribution.apk
                response_data['apk_name'] = apk.apk_file.name
                response_data['apk_download_url'] = request.build_absolute_uri(apk.apk_file.url)

        return Response(response_data)
