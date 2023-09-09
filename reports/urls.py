from django.urls import path
from . import views

app_name = 'reports'
urlpatterns = [
    path('hitting',views.HittingReports.as_view(),name='hitting_report'),
    path('hitting/report/delete/<int:id>/', views.DeleteHittingReport.as_view(), name='delete_report'),
    path('hitting/edit/<int:id>/',views.EditHittingReport.as_view(),name='edit_report'),
     path('pitching',views.PitchingReports.as_view(),name='pitching_report'),
    path('pitching/delete/<int:id>/', views.DeletePitchingReport.as_view(), name='delete_preport'),
    path('pitching/edit/<int:id>/',views.EditPitchingReport.as_view(),name='edit_preport')

]
