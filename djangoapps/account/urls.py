from django.conf.urls import url, include

from .resources import PaymentPlansResource

payment_plans = PaymentPlansResource()

urlpatterns = [
    url(r'', include(payment_plans.urls))
]
