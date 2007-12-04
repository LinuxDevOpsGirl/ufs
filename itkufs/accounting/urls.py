from django.conf.urls.defaults import *
from itkufs.accounting.views import *

urlpatterns = patterns('',
    # Account actions
    url(r'^(?P<group>[0-9a-z_-]+)/a/(?P<account>[0-9a-z_-]+)/deposit/$',
        transfer, {'transfer_type': 'deposit'}, name='account-deposit'),
    url(r'^(?P<group>[0-9a-z_-]+)/a/(?P<account>[0-9a-z_-]+)/withdraw/$',
        transfer, {'transfer_type': 'withdraw'}, name='account-withdraw'),
    url(r'^(?P<group>[0-9a-z_-]+)/a/(?P<account>[0-9a-z_-]+)/transfer/$',
        transfer, {'transfer_type': 'transfer'}, name='account-transfer'),

    # Admin: Transactions
    url(r'^(?P<group>[0-9a-z_-]+)/approve/$',
        approve, name='approve-transactions'),
    url(r'^(?P<group>[0-9a-z_-]+)/reject/$',
        reject_transactions, name='reject-transactions'),
    url(r'^(?P<group>[0-9a-z_-]+)/register/$',
        transfer, {'transfer_type': 'register'}, name='register-transactions'),
    url(r'^(?P<group>[0-9a-z_-]+)/multiple/$',
        transfer, {'transfer_type': 'multiple'}, name='multiple-transactions'),
)
