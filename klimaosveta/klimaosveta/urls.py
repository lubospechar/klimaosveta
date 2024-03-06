from django.contrib import admin
from django.urls import include, path
from webapp.views import Home, CourseListView, LectorListView, AboutView, Region
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('kurzy/', CourseListView.as_view(), name='courses'),
    path('lektori/', LectorListView.as_view(), name='lectors'),
    path('o-projektu/', AboutView.as_view(), name='about'),
    path('kraje/', Region.as_view(), name='regions'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
