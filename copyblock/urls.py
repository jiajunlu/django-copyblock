from django.conf.urls import url

urlpatterns = [
        url(r'^$', 'copyblock.views.serve', name='serve'),
]
