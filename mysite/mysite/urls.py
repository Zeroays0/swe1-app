from django.contrib import admin
from django.urls import include, path
from polls.views import index

from polls import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
