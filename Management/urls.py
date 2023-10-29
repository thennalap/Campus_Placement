from django.urls import path,include
from Management import views

urlpatterns=[
    path('jobregistration',views.job_registration,name='jobregistration'),
    path('jobdetails/<int:jobid>',views.jobdetails,name='jobdetails'),
    path('showjobs/<int:studentid>',views.show_job,name='showjobs'),
    path("jobupdate/<int:jobid>",views.job_details_update,name='jobupdate'),
    path("jobsapplied/<int:studentid>/<int:jobid>",views.appliedjobs,name='jobsapplied'),
    path("viewappliedjobs",views.view_applied_jobs,name="viewappliedjobs"),
    path("viewjobsbycompany",views.view_applied_jobs_by_company,name='viewjobsbycompany'),
    path('deletejobs/<int:jobid>',views.delete_registered_jobs,name='deletejobs'),
    path('selection/<int:appliedjobsid>',views.selection,name='selection'),
]