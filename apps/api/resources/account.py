from tastypie.resources import ModelResource

from apps.shared.cors import BaseCORSResource
from apps.account.models import PaymentPlan, User 


class PaymentPlansResource(BaseCORSResource, ModelResource):
    class Meta:
        queryset = PaymentPlan.objects.exclude(available=False)
        resource_name = 'account/payment-plans'
        list_allowed_methods = ['get',]
        detail_allowed_methods = ['get',]


class UsersResource(BaseCORSResource, ModelResource):
    class Meta:
        queryset = User.objects.exclude(is_admin=True)
        resource_name = 'account/users'
        list_allowed_methods = []
        detail_allowed_methods = ['post', ]
