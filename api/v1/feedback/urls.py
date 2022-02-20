from django.urls import path
from .views import CreateFeedbackView

app_name = 'feedback'

urlpatterns = [
    path('create/', CreateFeedbackView.as_view(),  name = 'create'),

]