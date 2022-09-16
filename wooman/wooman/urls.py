from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from wooman.web.views import WomenViewSet

router = SimpleRouter()
router.register('woman', WomenViewSet, basename='woman')
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path(r'joser/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
