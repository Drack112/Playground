from django.urls import path


from .views import ClienteViewSet

urlpatterns = [path("", ClienteViewSet.as_view(), name="cliente-list")]
