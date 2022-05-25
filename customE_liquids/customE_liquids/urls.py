"""customE_liquids URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('autenticacion/', include('autenticacion.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('cart/', include('cart.urls')),
    path('promociones/', include('promos.urls')),
    path('contact/', include('contact.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#     from django.conf.urls.static import static
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),