
# terminals/models.py

from django.db import models
from clients.models import Client
from distributions.models import Apk
from django.utils import timezone


class Terminal(models.Model):
    terminal_code = models.CharField(max_length=100, verbose_name="发布终端代码")
    description = models.TextField(verbose_name="发布终端描述")
    location = models.TextField(verbose_name="发布终端位置")
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, verbose_name="发布终端暂停")

    class Meta:
        verbose_name = "发布终端"
        verbose_name_plural = "发布终端"

    def __str__(self):
        return self.description+ " (" + self.terminal_code + ")"

class TerminalClientBinding(models.Model):
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE, verbose_name="发布终端")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="客户端")
    start_date = models.DateField(verbose_name="开始日期")
    end_date = models.DateField(null=True, blank=True, verbose_name="结束日期")

    def __str__(self):
        return f"{self.terminal} -> {self.client}"

    def save(self, *args, **kwargs):
        if self.end_date is None:
            self.end_date = timezone.datetime(9999, 12, 31).date()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "终端-实体绑定"
        verbose_name_plural = "终端-实体绑定"



class TerminalApkDistribution(models.Model):
    # 一个terminal只能存在一个记录
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE, verbose_name="发布终端", unique=True)
    apk = models.ForeignKey(Apk, on_delete=models.CASCADE, verbose_name="激活安装包")

    def __str__(self):
        return f"{self.terminal} -> {self.apk}"

    class Meta:
        verbose_name = "安装包分发"
        verbose_name_plural = "安装包分发"