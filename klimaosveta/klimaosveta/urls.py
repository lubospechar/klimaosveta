from django.contrib import admin
from django.urls import include, path
from webapp.views import Home, CourseListView, LectorListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('kurzy/', CourseListView.as_view(), name='courses'),
    path('lektori/', LectorListView.as_view(), name='lektori'),
# path('', include('django.contrib.flatpages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
