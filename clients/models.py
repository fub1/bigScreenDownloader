# clients/models.py
from django.db import models


# Create your models here.
class Client(models.Model):
    identifier = models.CharField(max_length=255, verbose_name="客户端识别代码")  # 品牌+型号+Android_ID
    client_android_api = models.CharField(max_length=255, verbose_name="客户端API版本")
    webview_version = models.CharField(max_length=255, verbose_name="客户端webview版本")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="客户端注册日期")
    is_deleted = models.BooleanField(default=False, verbose_name="客户端关闭")

    class Meta:
        verbose_name = "客户端"
        verbose_name_plural = "客户端"

    def __str__(self):
        return self.identifier


class ClientLog(models.Model):
    client = models.ForeignKey(Client,
                               related_name='logs',
                               on_delete=models.CASCADE,
                               verbose_name="客户端识别代码")
    ip = models.CharField(max_length=15, verbose_name="客户端ip地址")
    logged_at = models.DateTimeField(auto_now_add=True, verbose_name="在线日期")

    class Meta:
        verbose_name = "客户端日志"
        verbose_name_plural = "客户端日志"
