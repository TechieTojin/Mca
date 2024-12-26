from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback.urls')),
    path('', RedirectView.as_view(url='feedback/')),  # Redirect root URL to 'feedback/'
]
