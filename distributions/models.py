from django.db import models

# distributions/models.py
# Create your models here.

class DistributionProject(models.Model):
    description = models.TextField(verbose_name= "项目描述")
    package_name = models.CharField(max_length=255,verbose_name= "项目包名")

    def __str__(self):
        return f"{self.description} ({self.package_name})"

    class Meta:
        verbose_name = "APP注册"
        verbose_name_plural = "APP注册"

class Apk(models.Model):
    project = models.ForeignKey(
        DistributionProject,
        related_name='apks',
        on_delete=models.CASCADE,
        verbose_name= "项目名称"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name= "上传日期")
    apk_file = models.FileField(upload_to='apks/', verbose_name= "apk文件")  # 存储在 MEDIA_ROOT/apks/ 目录下

    def __str__(self):
        return f"{self.project} uploaded on {self.uploaded_at}"

    class Meta:
        verbose_name = "安装包管理"
        verbose_name_plural = "安装包管理"


