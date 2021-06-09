from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
    path('calc_duration', views.calc_duration, name='calc_duration'),
    path('auto_load_extra', views.auto_load_extra, name='auto_load_extra'),

    path('submit_form', views.submit_form, name='submit_form'),
    path('up_submit_form', views.up_submit_form, name='up_submit_form'),
    path('cr_submit_form', views.cr_submit_form, name='cr_submit_form'),
    path('ur_submit_form', views.ur_submit_form, name='ur_submit_form'),

    path('create_planned_maintenance', views.Create_planned_maintenance.as_view(), name='create_planned_maintenance'),
    path('update_planned_maintenance', views.Update_planned_maintenance.as_view(), name='Ureate_planned_maintenance'),
    path('create_reactive_maintenance', views.Create_reactive_maintenance.as_view(), name='create_reactive_maintenance'),
    path('update_reactive_maintenance', views.Update_reactive_maintenance.as_view(), name='update_reactive_maintenance'),

    path('maintain_splice_circuit', views.Maintain_splice_circuit.as_view(), name='maintain_splice_circuit'),
]
