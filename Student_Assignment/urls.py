from django.contrib import admin
from django.urls import path , include
from API import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

# router object
router = DefaultRouter()

router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='restframeworkurls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)