from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'good', views.GoodViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('good/', include('rest_framework.urls', namespace='rest_framework')),
    path("order/add/", views.OrderCreate.as_view()),
]
urlpatterns += router.urls 