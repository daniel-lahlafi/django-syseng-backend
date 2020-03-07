from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('save_questions.urls')),
    path('api/', include('nlp_search.urls')),
    path('api/', include('web_scrap.urls')),
    path('api/', include('quiz.urls'))
]