from django import forms
from .models import HittingReport,PitchingReport


class HittingReportsForm(forms.ModelForm):
     class Meta:
        model = HittingReport
        fields = '__all__'
        widgets = {
            'player_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last, First'}),
            'team' : forms.Select(attrs={'class': 'form-control'}),
            'bats' : forms.Select(attrs={'class': 'form-control'}),
            'hit': forms.Select(attrs={'class': 'form-control'}),
            'throws' : forms.Select(attrs={'class': 'form-control'}),
            'pos' : forms.Select(attrs={'class': 'form-control'}),
            'report_date' : forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'Declarative_Statement' : forms.Textarea(attrs={'class': 'form-control','placeholder':"Summarize this player's scouting look in a few brief sentences"}),
            'power':forms.Select(attrs={'class': 'form-control'}),
            'fielding':forms.Select(attrs={'class': 'form-control'}),
            'power':forms.Select(attrs={'class': 'form-control'}),
            'run':forms.Select(attrs={'class': 'form-control'}),
            'throwing':forms.Select(attrs={'class': 'form-control'}),
            'fvforrun':forms.Select(attrs={'class': 'form-control'}),
            'fvforpower':forms.Select(attrs={'class': 'form-control'}),
            'fvforfielding':forms.Select(attrs={'class': 'form-control'}),
            'fvforthrowing':forms.Select(attrs={'class': 'form-control'}),
            'fvforhit':forms.Select(attrs={'class': 'form-control'}),
            'commentforrun':forms.TextInput(attrs={'class': 'form-control'}),
            'commentforfielding':forms.TextInput(attrs={'class': 'form-control'}),
            'commentforthrowing':forms.TextInput(attrs={'class': 'form-control'}),
            'commentforpower':forms.TextInput(attrs={'class': 'form-control'}),
            'commentforhit':forms.TextInput(attrs={'class': 'form-control'}),
            'overall_grade':forms.Select(attrs={'class': 'form-control'}),
            'future_grade':forms.Select(attrs={'class': 'form-control'}),
            
        }

class PitchingReportForm(forms.ModelForm):
    class Meta:
        model = PitchingReport
        fields = '__all__'
        widgets = {
            'player_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last, First'}),
            'team' : forms.Select(attrs={'class': 'form-control'}),
            'hit': forms.Select(attrs={'class': 'form-control'}),
            'throws' : forms.Select(attrs={'class': 'form-control'}),
            'pos' : forms.Select(attrs={'class': 'form-control'}),
            'report_date' : forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'Declarative_Statement' : forms.Textarea(attrs={'class': 'form-control','placeholder':"Summarize this player's scouting look in a few brief sentences"}),
            'pitch1': forms.Select(attrs={'class': 'form-control'}),
            'pitch2':forms.Select(attrs={'class': 'form-control'}),
            'pitch3':forms.Select(attrs={'class': 'form-control'}),
            'pitch4':forms.Select(attrs={'class': 'form-control'}),
            'pitch1_velo_low':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Low Velocity'}),
            'pitch2_velo_low':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Low Velocity'}),
            'pitch3_velo_low':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Low Velocity'}),
            'pitch4_velo_low':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Low Velocity'}),
            'pitch1_velo_high':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'High Velocity'}),
            'pitch2_velo_high':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'High Velocity'}),
            'pitch3_velo_high':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'High Velocity'}),
            'pitch4_velo_high':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'High Velocity'}),
            'pitch1_grade':forms.Select(attrs={'class': 'form-control'}),
            'pitch2_grade':forms.Select(attrs={'class': 'form-control'}),
            'pitch3_grade':forms.Select(attrs={'class': 'form-control'}),
            'pitch4_grade':forms.Select(attrs={'class': 'form-control'}),
            'pitch1_comment':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment here'}),
            'pitch2_comment':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment here'}),
            'pitch3_comment':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment here'}),
            'pitch4_comment':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment here'}),
            'pitch1_fv':forms.Select(attrs={'class': 'form-control'}),
            'pitch2_fv':forms.Select(attrs={'class': 'form-control'}),
            'pitch3_fv':forms.Select(attrs={'class': 'form-control'}),
            'pitch4_fv':forms.Select(attrs={'class': 'form-control'}),
            'overall_grade':forms.Select(attrs={'class': 'form-control'}),
            'future_grade':forms.Select(attrs={'class': 'form-control'}),
            
        }




