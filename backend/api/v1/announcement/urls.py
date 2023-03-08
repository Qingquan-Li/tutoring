from django.urls import path
from .views import AnnouncementList

# docs.djangoproject.com/en/4.1/intro/tutorial03/#namespacing-url-names
app_name = 'api_v1_announcement'

urlpatterns = [
    path('announcements/', AnnouncementList.as_view(), name='announcement-list'),
]
