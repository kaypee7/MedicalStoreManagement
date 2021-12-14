from django.conf.urls import include
from django.contrib import admin
from django.db import router
from django.urls import path
from rest_framework import routers
from DjangoMedicalApp import views

router=routers.DefaultRouter()
router.register("company", views.CompanyViewSet,basename="company")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
