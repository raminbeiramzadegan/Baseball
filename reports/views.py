from django.shortcuts import render,redirect,get_object_or_404
from .models import HittingReport,PitchingReport
from .forms import HittingReportsForm,PitchingReportForm
from django.views import View
from django.contrib import messages

# Create your views here.

class HittingReports(View):
    form_class = HittingReportsForm
    template_name = 'reports/Hitting_reports.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self,request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                HittingReport.objects.create(player_name = cd['player_name'],team = cd['team'],bats=cd['bats'],
                                            throws=cd['throws'],pos=cd['pos'],report_date=cd['report_date'],
                                            Declarative_Statement=cd['Declarative_Statement'],hit=cd['hit'],
                                            fielding=cd['fielding'],power=cd['power'],throwing=cd['throwing'],run=cd['run']
                                            ,fvforhit=cd['fvforhit'],fvforrun=cd['fvforrun'],fvforthrowing = cd['fvforthrowing'],fvforfielding = cd['fvforfielding'],fvforpower=cd['fvforpower'],
                                            commentforhit=cd['commentforhit'],commentforrun=cd['commentforrun'],commentforthrowing = cd['commentforthrowing'],commentforfielding = cd['commentforfielding'],commentforpower=cd['commentforpower']
                                            ,overall_grade = cd['overall_grade'],future_grade = cd['future_grade']
                                            )
                messages.success(request, 'Form submitted successfully!','success')
                return redirect('home:homeview') 
            else:
                messages.error(request, 'Form submission failed. Please check the data.','danger')
        else:
            form = self.template_name

        return render(request, self.template_name, {'form': form})



class DeleteHittingReport(View):
    def get(self, request, id):

            hitting_report = HittingReport.objects.get(id=id)
            hitting_report.delete()

        
            return redirect('home:homeview') 





class  EditHittingReport(View):
    form_class = HittingReportsForm
    template_name = 'reports/Hitting_reports.html'

    def get(self, request, id=None):
        hittingreports = get_object_or_404(HittingReport, id=id)  
        form = self.form_class(instance=hittingreports)
        return render(request, self.template_name, {'form': form})
        
    def post(self, request, id=None):
        hittingreports = get_object_or_404(HittingReport, id=id)  
        form = self.form_class(request.POST, instance=hittingreports)
        if form.is_valid():
            form.save()
            messages.success(request,'Form has been updated successfully!','success')
            return redirect('home:homeview')
        else:
                messages.error(request, 'Form submission failed. Please check the data.','danger')
                
        return render(request, self.template_name, {'form': form}) 
        


class PitchingReports(View):
    form_class = PitchingReportForm
    template_name = 'reports/pitcher_reports.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self,request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                PitchingReport.objects.create( player_name = cd['player_name'],team = cd['team'],
                                            throws=cd['throws'],pos=cd['pos'],report_date=cd['report_date'],
                                            Declarative_Statement=cd['Declarative_Statement'],pitch1=cd['pitch1'],
                                            pitch2=cd['pitch2'],pitch3=cd['pitch3'],pitch4=cd['pitch4'],pitch1_comment=cd['pitch1_comment']
                                            ,pitch2_comment=cd['pitch2_comment'],pitch3_comment=cd['pitch3_comment'],pitch4_comment = cd['pitch4_comment'],pitch1_fv = cd['pitch1_fv'],pitch2_fv=cd['pitch2_fv'],
                                            pitch3_fv=cd['pitch3_fv'],pitch4_fv=cd['pitch4_fv'],pitch1_grade = cd['pitch1_grade'],pitch2_grade = cd['pitch2_grade'],pitch3_grade=cd['pitch3_grade'],pitch4_grade=cd['pitch4_grade']
                                            ,pitch1_velo_low=cd['pitch1_velo_low'],pitch2_velo_low=cd['pitch2_velo_low'],pitch3_velo_low=cd['pitch3_velo_low'],pitch4_velo_low=cd['pitch4_velo_low'],pitch1_velo_high=cd['pitch1_velo_high'],
                                            pitch2_velo_high=cd['pitch2_velo_high'],pitch3_velo_high=cd['pitch3_velo_high'],
                                            pitch4_velo_high=cd['pitch4_velo_high'],overall_grade = cd['overall_grade'],
                                            future_grade = cd['future_grade']
                                            )
                messages.success(request, 'Form submitted successfully!',extra_tags='success')
                return redirect('home:homeview') 
            else:
                messages.error(request, 'Form submission failed. Please check the data.','danger')

        else:
            form = self.template_name

        return render(request, self.template_name, {'form': form})



class DeletePitchingReport(View):
    def get(self, request, id):

            hitting_report = PitchingReport.objects.get(id=id)
            hitting_report.delete()

        
            return redirect('home:homeview') 





class  EditPitchingReport(View):
    form_class = PitchingReportForm
    template_name = 'reports/pitcher_reports.html'

    def get(self, request, id=None):
        pitchingreports = get_object_or_404(PitchingReport, id=id)  
        form = self.form_class(instance=pitchingreports)
        return render(request, self.template_name, {'form': form})
        
    def post(self, request, id=None):
        pitchingreports = get_object_or_404(PitchingReport, id=id)  
        form = self.form_class(request.POST, instance=pitchingreports)
        if form.is_valid():
            form.save()
            messages.success(request,'Form has been updated successfully!','success')
            return redirect('home:homeview')
        else:
                messages.error(request, 'Form submission failed. Please check the data.','danger')

        return render(request, self.template_name, {'form': form}) 
        