from django.urls import path,include
from home.views import index,person,ClassPerson,PersonViewSets,RegisterAPI,LoginAPI

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'person', PersonViewSets, basename='person')
urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path("index/", index, name='index'),
    path("person/", person, name='person'),
    path("register/", RegisterAPI.as_view(), name='register'),
    path("login/", LoginAPI.as_view(), name='login'),
    path("classperson/", ClassPerson.as_view(), name='classperson'),
]
