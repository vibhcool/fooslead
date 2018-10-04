from django.contrib import admin
from django.conf.urls import url,include

from foos_web import urls

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('foos_web.urls')),

]
