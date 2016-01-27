from tastypie.resources import ModelResource

from apps.shared.cors import BaseCORSResource
from apps.account.models import PaymentPlan


class PaymentPlansResource(BaseCORSResource, ModelResource):
    class Meta:
        queryset = PaymentPlan.objects.exclude(available=False)
        resource_name = 'payment-plans'
        list_allowed_methods = ['get',]
        detail_allowed_methods = ['get',]
