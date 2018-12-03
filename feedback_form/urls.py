from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from trainee_feedback.views import feedback_view, add_feedback_view, thankyou_view, trainer_view, report_view, feedback_detail_view
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('feedback/', feedback_view),
    path('add_feedback/', add_feedback_view),
    path('thankyou/', thankyou_view),
    path('trainer/', trainer_view),
    path('report/', report_view),
    path('feedback_detail/<int:pk>/', feedback_detail_view),
]
