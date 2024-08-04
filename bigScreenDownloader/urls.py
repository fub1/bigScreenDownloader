"""
URL configuration for bigScreenDownloader project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from api.views import ClientApiEndpoint
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponse

schema_view = get_schema_view(
    openapi.Info(
        title="swagger-doc",
        default_version='v1',
        description="API ",
        terms_of_service="xxx",
        contact=openapi.Contact(email="xxx"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

def index(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>M2M</title>
    </head>
    <body>
        <h1>Welcome M2M service</h1>
        <p>.....</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('v1/api/endpoint/', ClientApiEndpoint.as_view(), name='device-info-api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)