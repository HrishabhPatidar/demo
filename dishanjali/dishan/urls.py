from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import *


urlpatterns = [
                  url(r'^index.html/', views.Index , name='Index'),
                  url(r'^index/', views.Index , name='Index'),
                  url(r'^motivation.html/' , views.Motivation , name='Motivation'),
                  url(r'^donate.html/', views.Donate, name='Doante'),
                  url(r'^center.html/',views.Center, name='Center'),
                  url(r'^about.html/', views.About.as_view() , name='About'),
                  url(r'^involve.html/', views.Involve ,name='Involve'),
                  url(r'^contact.html/', views.ContactView.as_view() ,name='Contact'),
                  url(r'^gallery.html/', views.GalleryView.as_view() , name='Gallery'),
                  url(r'^event.html/', views.Event , name='Event'),
              ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)