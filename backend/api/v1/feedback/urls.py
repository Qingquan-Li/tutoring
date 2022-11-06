from django.urls import path
from .views import FeedbackList

# docs.djangoproject.com/en/4.1/intro/tutorial03/#namespacing-url-names
app_name = 'api_v1_feedback'

urlpatterns = [
    path('feedbacks', FeedbackList.as_view(), name='feedback-list'),
]
