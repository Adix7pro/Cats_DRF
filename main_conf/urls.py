from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/",include("apiapp.urls")),
    path("api/v1/auth/",include("rest_framework.urls")),
    path("api/v1/dj-rest-auth/",include("dj_rest_auth.urls")),
    path("api/v1/dj-rest-auth/registration/",include("dj_rest_auth.registration.urls")),
    path("api/schemas/",SpectacularAPIView.as_view(), name="schemas"),
    path("api/schemas/redoc/",SpectacularRedocView.as_view(
         url_name = "schemas"), name="redoc"),
     path("api/schemas/swagger/",SpectacularSwaggerView.as_view(
         url_name = "schemas"), name="swagger"),
]
