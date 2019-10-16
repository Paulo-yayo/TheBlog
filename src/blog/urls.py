from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from posts.views import (
    index, blog, post, search, podcast, event, store, about, gallary,
    post_create, post_update, post_delete)


from users.views import(
    about_podcast, about_shop, about_media, about_events, term_conditions
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='post-list'),
    path('podcast/', podcast),
    path('about/', about),
    path('event/', event),
    path('store/', store),
    path('gallary/', gallary),
    path('about_podcast/', about_podcast),#The users app urls
    path('about_shop/', about_shop),#The users app urls
    path('about_media/', about_media),#The users app urls
    path('about_events/', about_events),#The users app urls
    path('term_conditions/', term_conditions),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('create/', post_create, name='post-create'),
    #path('^(?P<category>[^\.]+)/(?P<slug>[^\.]+)/', 'post', name='post_detail'), 
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls'))
   
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)