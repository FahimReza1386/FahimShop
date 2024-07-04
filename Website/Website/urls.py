from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Store.urls')),
    path('Cart/', include('Cart.urls')),
    path('Payment/', include('Payment.urls')),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
