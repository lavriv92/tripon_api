from django.conf.urls import url, include
from tastypie.api import Api

from .resources import PaymentPlansResource

v1_api = Api(api_name='v1')
v1_api.register(PaymentPlansResource())

urlpatterns = [
    url(r'', include(v1_api.urls))
]
