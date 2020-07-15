from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import *

# Register your models here.
admin.site.register(app_user)
admin.site.register(project)
admin.site.register(species)
admin.site.register(map_data)
admin.site.register(survey_questions)
admin.site.register(survey_data)
admin.site.register(survey_template)
admin.site.register(incident_observations)
admin.site.register(observation_type)
admin.site.register(survey_methods)
admin.site.register(survey_method_types)