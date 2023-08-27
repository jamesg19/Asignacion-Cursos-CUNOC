from django.urls import path


from .views import SimularHorario
urlpatterns = [
    path('simular/', SimularHorario, name='simulation'),

]
