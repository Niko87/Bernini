# -*- coding: utf-8 -*-
from rest_framework.documentation import include_docs_urls
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from views import *

urlpatterns = [
    url(r'^docs/', include_docs_urls(title='Cecotec API', 
                                    permission_classes=[])), # allow to non logged users to see docs
    url(r'^api/', include(apirouter.urls)),
    url(r'^', include(nonadmin.urls))
]

