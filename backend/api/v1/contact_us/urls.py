from django.urls import path
from .views import MessageList

# docs.djangoproject.com/en/4.1/intro/tutorial03/#namespacing-url-names
app_name = 'api_v1_contact_us'

urlpatterns = [
    path('contact-us/', MessageList.as_view(), name='message-list'),
]
