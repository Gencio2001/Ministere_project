from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. On place les modules spécifiques EN PREMIER
    path('rapports/', include('rapports.urls')),
    path('recommandations/', include('recommandations.urls')),
    path('affectations/', include('affectations.urls')),
    path('structures/', include('structures.urls')), 
    path('utilisateurs/', include('users.urls')),    
    path('journaux/', include('journaux.urls')),
    
    # 2. Le dashboard par défaut EN DERNIER
    path('', include('core.urls')), 
]