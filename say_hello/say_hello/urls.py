
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from hi.views import( HelloView  , WelcomView  , RemoveView , NewList ,DetailList
 , edit_rest , CreateRest)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',HelloView.as_view())
    ,url(r'^bye/$',TemplateView.as_view(template_name="bye.html"))
    ,url(r'^$',TemplateView.as_view(template_name="welcome.html"))
    ,url(r'^kir/$',TemplateView.as_view(template_name="kir.html"))
    ,url(r'^welcome/$',WelcomView.as_view())
    ,url(r'^rest/create/$',CreateRest.as_view())
    ,url(r'^rest/$',NewList.as_view())
    ,url(r'^rest/(?P<slug>\w+)/$',NewList.as_view())
    ,url(r'^detail/(?P<slug>\w+)/$',DetailList.as_view())
    ,url(r'^remove/(?P<slug>\w+)/$',RemoveView.as_view())
    ,url(r'^edit/(?P<slug>\w+)/$',edit_rest)
]
