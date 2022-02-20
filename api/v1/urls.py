from django.urls import path, include

urlpatterns = [

    path('feedback/', include('api.v1.feedback.urls'))

]