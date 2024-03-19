from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('apps.booking.urls')),
    # path('api/', include('apps.guest.urls')),
    # path('api/', include('apps.hotel.urls')),
    # path('api/', include('apps.room.urls')),
    # path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('', include('apps.hotel.urls'))
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

