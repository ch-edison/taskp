from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from taskapp import views
from rest_framework import routers
from taskapp.views import taskViewSet
from django.conf.urls import include
router = routers.SimpleRouter()
router.register(r'rest_framework', taskViewSet)
urlpatterns = [
    url(r'^addimage/', views.ProfileDetail.as_view()),
    url(r'^',include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
