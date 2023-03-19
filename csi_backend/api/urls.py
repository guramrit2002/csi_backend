from django.urls import path
from .views import Sigcontrol,Teamcontrol,Eventcontrol

urlpatterns = [
    # urls for sig 
    path('sig/all/',Sigcontrol.as_view(),name = 'All-Sig'),
    path('detail/<str:name>/',Sigcontrol.as_view(),name = 'Specific-Sig'),
    # urls for team members
    path('all/team/',Teamcontrol.as_view(),name = 'Team-Sig'),
    path('team/detail/<int:id>/',Teamcontrol.as_view(),name = 'Team-Sig'),
    # urls for event members
    path('all/events/',Eventcontrol.as_view(),name = 'Event-Sig'),
    path('event/detail/<int:id>/',Eventcontrol.as_view(),name = 'Event-Sig'),

]
