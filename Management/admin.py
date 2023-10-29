from django.contrib import admin
from Management.models import job_details,applied_jobs,show_jobs,selected_students

# Register your models here.
admin.site.register(job_details)
admin.site.register(applied_jobs)
admin.site.register(show_jobs)
admin.site.register(selected_students)
