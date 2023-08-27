
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('docentes.urls')),
    path('api_simular/',include('asignacion_curso.urls'))
]
