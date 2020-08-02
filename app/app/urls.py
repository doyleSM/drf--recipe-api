from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Recipes API",
        default_version='v1',
        description="Test description",
        terms_of_service="",
        contact=openapi.Contact(email="gdoyle.dev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/recipe/', include('recipe.urls')),
    path("swagger/", schema_view.with_ui('swagger',
                                         cache_timeout=0),
         name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc',
                                       cache_timeout=0),
         name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
