from django.http import HttpResponse

from tastypie.resources import ModelResource

from ..shared.cors import BaseCORSResource
from .models import PaymentPlan


class PaymentPlansResource(BaseCORSResource, ModelResource):
    class Meta:
        queryset = PaymentPlan.objects.exclude(available=False)
        resource_name = 'payment-plans'
        list_allowed_methods = ['get', ]
        detail_allowed_methods = ['get', ]
