from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:b_slug>/', views.blog_details, name='blog_details'),
    path('chat_bot/', views.chat_bot, name='chat_bot'),
    path('iot/', views.iot, name='iot'),
    path('ai/', views.ai, name='ai'),
    path('mobile_development/', views.mobile_development, name='mobile_development'),
    path('network/', views.network, name='network'),
    path('web_design/', views.web_design, name='web_design'),
    path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),
    path('contact_view/', views.ContactView, name='contact_view'),
    path('appointment/', views.appointment, name='appointment'),
    path('consultation/', views.consultation, name='consultation'),
    path('email_subscription/', views.email_subscription,name='email_subscription'),
    path('add_reviews/', views.add_reviews,name='add_reviews'),


]
