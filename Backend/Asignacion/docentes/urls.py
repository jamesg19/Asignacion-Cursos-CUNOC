from django.urls import path
from .views import DocentesList, DocentesRetrieveUpdateDestroyView, DocenteDeleteById,guardar_lista_objetos

urlpatterns = [
    path('docentes/', DocentesList.as_view(), name='docente-list'),
    path('docentes/<int:pk>/', DocentesRetrieveUpdateDestroyView.as_view(), name='docente-retrieve-update-destroy'),
    path('docentes/<int:pk>/delete/', DocenteDeleteById.as_view(), name='docente-delete'),
    path('docentes/save/', guardar_lista_objetos, name='docente-guardar'),
]
