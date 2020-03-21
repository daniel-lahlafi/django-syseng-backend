from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('save_questions.urls')),
    path('api/', include('nlp_search.urls')),
    path('api/', include('web_scrap.urls')),
    path('api/', include('quiz.urls')),
    path('', include('frontend.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)