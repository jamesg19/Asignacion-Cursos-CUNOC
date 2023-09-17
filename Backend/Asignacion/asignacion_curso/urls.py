from django.urls import path


from .views import SimularHorario, HorariosCursos, PeriodosEdificio, SalonesEdificio,HorariosParametros

urlpatterns = [
    path('simular/', SimularHorario, name='simulation'),
    path('schedulee/<int:horario_id>/', HorariosCursos.as_view(), name="schedulee"),
    path('schedulee/periodos_edificio/<int:edificio_id>', PeriodosEdificio.as_view(), name="periodos_edificio"),
    path('schedulee/salones_edificio/<int:edificio_id>', SalonesEdificio.as_view(), name="periodos_edificio"),
    path('schedulee/parametros/<int:horario_id>', HorariosParametros.as_view(), name="horarios_parametros")

]
