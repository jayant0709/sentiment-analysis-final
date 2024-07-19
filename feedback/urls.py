from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('feedback_form', views.feedback_form, name='feedback_form'),  # Assuming 'feedback_form' is your form view
    path('', views.home, name="home_page"),
    path('thank-you/<int:feedback_id>/', views.thank_you, name='thank_you'),
    path('view-feedback/<int:feedback_id>/', views.view_feedback, name='view_feedback'),
    path('chatbot-api/', views.chatbot_api, name='chatbot_api'),
]
