from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from clients.models import Client, ClientLog
from datetime import timedelta
from terminals.models import TerminalClientBinding, Terminal, TerminalApkDistribution
from distributions.models import Apk, DistributionProject
from api.Serializer import ApkSerializer

class ClientApiEndpoint(APIView):
    def post(self, request, *args, **kwargs):
        identifier = request.data.get('identifier')
        android_api = request.data.get('android_api')
        client_ip = request.META.get('REMOTE_ADDR', '')

        response_data = {
            'client_id': None,
            'terminal_id': None,
            'apk_name': None,
            'apk_download_url': None
        }

        # 查询客户端是否存在
        if Client.objects.filter(identifier=identifier).exists():
            response_data['client_id'] = Client.objects.get(identifier=identifier).id
        # 如果不存在，创建一个新的客户端
        else:
            client = Client.objects.create(identifier=identifier, client_android_api=android_api)
            response_data['client_id'] = client.id

        # 创建客户端日志,过去1H内的日志不再记录
        if not ClientLog.objects.filter(logged_at__gte=timezone.now() - timedelta(hours=1), client_id=response_data['client_id']).exists():
            client_log = ClientLog.objects.create(client_id=response_data['client_id'], ip=client_ip)
            client_log.timestamp = timezone.now()
            client_log.save()



        # 查询客户端对应的终端信息
        terminal_client_binding = TerminalClientBinding.objects.filter(client_id=response_data['client_id'],
                                                                       start_date__lte=timezone.now(),
                                                                       end_date__gte=timezone.now())

        if terminal_client_binding.exists():
            response_data['terminal_id'] = terminal_client_binding.last().terminal_id

            # 查询终端对应的APK信息
            terminal_apk_distribution = TerminalApkDistribution.objects.filter(terminal_id=response_data['terminal_id'])
            if terminal_apk_distribution.exists():
                apk = terminal_apk_distribution.first().apk
                response_data['apk_name'] = apk.apk_file.name
                response_data['apk_download_url'] = request.build_absolute_uri(apk.apk_file.url)



        return Response(response_data)