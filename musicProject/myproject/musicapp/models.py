from django.db import models

# Create your models here.
from django.db import models


class ArtistClassify(models.Model):
    artist_classify = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    category_id = models.CharField(max_length=4)

    class Meta:
        db_table = 'artist_classify' # 确保和数据库表名一致


class ArtistFan(models.Model):
    artist_name = models.CharField(max_length=255)
    fan_cnt = models.BigIntegerField()

    class Meta:
        db_table = 'artist_fan'
        verbose_name = 'Artist Fan'                 # 单数字符串
        verbose_name_plural = 'Artists Fans'        # 复数字符串