from django.contrib import admin
from mp.models import Mentor
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin



class MentorResource(resources.ModelResource):
    class Meta:
        model = Mentor

class MentorAdmin(ImportExportModelAdmin):
    resource_class = MentorResource
    pass

# Register your models here.
admin.site.register(Mentor,MentorAdmin)