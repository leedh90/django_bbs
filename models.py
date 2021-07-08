from django.db import models

# Create your models here.
# 모델페이지는 DB의 테이블을 만둘어 주는 페이지
# class로서 DB 테이블 속성과 컬럼을 만들 수 있다.
class bbs_list(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    contents = models.TextField(max_length=300)
    createDate = models.DateTimeField('date published')
