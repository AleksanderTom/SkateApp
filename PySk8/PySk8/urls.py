"""PySk8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from PySk8 import settings
from SkateApp.views import UserFormView, HomePageView, LoginUser, Logout, UserAccView, SoloSkateView, MiniForumView, \
    EditPostView, DeletePostView, AddWarnView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view()),
    url(r'^register/$', UserFormView.as_view()),
    url(r'^login/', LoginUser.as_view(), name='login'),
    url(r'^logout/', Logout.as_view()),
    url(r'^user_acc$', UserAccView.as_view(), name='user_acc'),
    url(r'^solo_skate$', SoloSkateView.as_view()),
    url(r'^mini_forum$', MiniForumView.as_view(), name='mini_forum'),
    url(r'^edit_post/(?P<id>[0-9]+)$', EditPostView.as_view()),
    url(r'^delete_post/(?P<id>[0-9]+)$', DeletePostView.as_view()),
    url(r'^add_warn/(?P<id>[0-9]+)$', AddWarnView.as_view()),
]

if settings.DEBUG:
    # static files (images, css, javasript, etc.)
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]
