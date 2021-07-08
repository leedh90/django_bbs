from django.contrib import admin

# Register your models here.
from bbs.models import bbs_list

admin.site.register(bbs_list)
# db테이블에 대한 권한을 등록해 준다.