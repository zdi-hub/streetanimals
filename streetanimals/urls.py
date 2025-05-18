from django.contrib import admin
from django.urls import path
from donations import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.donate, name='donate'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('submit-testimonial/', views.submit_testimonial, name='submit_testimonial'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
