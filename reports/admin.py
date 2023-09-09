from django.contrib import admin
from .models import HittingReport,PitchingReport
# Register your models here.



class HittingReportAdmin(admin.ModelAdmin):
    list_display = ['player_name']



admin.site.register(HittingReport,HittingReportAdmin)

class PitchingReportAdmin(admin.ModelAdmin):
    list_display = ['player_name']



admin.site.register(PitchingReport,PitchingReportAdmin)