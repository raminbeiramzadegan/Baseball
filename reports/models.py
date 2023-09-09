from bs4 import BeautifulSoup
from django.db import models
import requests
from django.utils import timezone
def get_team_choices():
    url = "https://www.mlb.com/news"
    team_choices = []

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            team_names = soup.find_all('a', class_='header__subnav__item header__subnav--teams__team')[:30]

            for names in team_names:
                name = names.find('span', class_="header__subnav--teams__team--name")
                team_name = name.get_text()
                team_choices.append((team_name, team_name))  # Append a tuple with the same value for both display and value

        return team_choices
     
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
    

TEAM = get_team_choices()
BATS = (
    ('l', 'L'),
    ('r', 'R'),
    ('S', 'S'),
    )
THROWS = (
    ('l', 'L'),
    ('r', 'R'),
    
    )
POS = (
    ('S', 'S'),
    ('LHP', 'LHP'),
    ('RHP', 'RHP'),
    ('SS', 'SS'),
    ('C', 'C'),
    ('OF','OF'),
    ('3B','3B'),
    ('1B', '1B'),
    ('2B', '2B'),
    )
PITCH_TYPES = (
    ('FASTBALL','fastball'),
    ('CHANEUP','changeup'),
    ('SLIDER','slider'),
    ('CURVEBALL','curveball'),
    ('SLURVE','slurve'),
    ('CUT FASTBALL','cut fastball'),
    ('SPLIT FINGER','split finger'),
    ('KNUCKLE BALL','knuckle ball'),
    ('SINKER','sinker'),
    ('RUNS','runs'),

)
INTEGER_CHOICES = [(i, i) for i in range(20, 81, 5)]
    


class HittingReport(models.Model):
  

    player_name = models.CharField(max_length=255)
    team = models.CharField(max_length=30,choices=TEAM)
    bats = models.CharField(max_length=10,choices=BATS)
    throws = models.CharField(max_length=10,choices=THROWS)
    pos = models.CharField(max_length=10,choices=POS)
    report_date = models.DateTimeField(default=timezone.now)
    Declarative_Statement = models.TextField()
    fvforhit = models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)
    fvforfielding = models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)
    fvforpower = models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)
    fvforthrowing = models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)
    fvforrun = models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)

    commentforhit = models.CharField(max_length=255,blank=True,null=True)
    commentforfielding = models.CharField(max_length=255,blank=True,null=True)
    commentforpower = models.CharField(max_length=255,blank=True,null=True)
    commentforthrowing = models.CharField(max_length=255,blank=True,null=True)
    commentforrun = models.CharField(max_length=255,blank=True,null=True)
    hit = models.PositiveIntegerField(choices=INTEGER_CHOICES)
    fielding = models.PositiveIntegerField(choices=INTEGER_CHOICES)
    power = models.PositiveIntegerField(choices=INTEGER_CHOICES)
    throwing = models.PositiveIntegerField(choices=INTEGER_CHOICES)
    run = models.PositiveIntegerField(choices=INTEGER_CHOICES)
    overall_grade = models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True
    )
    future_grade = models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)

    def __str__(self):
        return self.player_name
    

class PitchingReport(models.Model):
    player_name = models.CharField(max_length=255)
    team = models.CharField(max_length=30,choices=TEAM)
    throws = models.CharField(max_length=10,choices=THROWS)
    pos = models.CharField(max_length=10,choices=POS)
    report_date = models.DateTimeField()
    Declarative_Statement = models.TextField(blank=True,null=True)
    overall_grade = models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True
    )
    future_grade = models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)
    pitch1 = models.CharField(max_length=20,choices=PITCH_TYPES,blank=True,null=True)
    pitch2 = models.CharField(max_length=20,choices=PITCH_TYPES,blank=True,null=True)
    pitch3 = models.CharField(max_length=20,choices=PITCH_TYPES,blank=True,null=True)
    pitch4 = models.CharField(max_length=20,choices=PITCH_TYPES,blank=True,null=True)
    pitch1_velo_low =  models.CharField(max_length=255,blank=True,null=True)
    pitch2_velo_low =  models.CharField(max_length=255,blank=True,null=True)
    pitch3_velo_low =  models.CharField(max_length=255,blank=True,null=True)
    pitch4_velo_low =  models.CharField(max_length=255,blank=True,null=True)
    pitch1_velo_high =  models.CharField(max_length=255,blank=True,null=True)
    pitch2_velo_high = models.CharField(max_length=255,blank=True,null=True)
    pitch3_velo_high =  models.CharField(max_length=255,blank=True,null=True)
    pitch4_velo_high = models.CharField(max_length=255,blank=True,null=True)
    pitch1_grade =models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)
    pitch2_grade =models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)
    pitch3_grade = models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)
    pitch4_grade = models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)
    pitch1_comment = models.CharField(max_length=255,blank=True,null=True)
    pitch2_comment = models.CharField(max_length=255,blank=True,null=True)
    pitch3_comment = models.CharField(max_length=255,blank=True,null=True)
    pitch4_comment = models.CharField(max_length=255,blank=True,null=True)
    pitch1_fv =  models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)
    pitch2_fv =  models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)
    pitch3_fv =  models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)
    pitch4_fv =  models.PositiveIntegerField(choices=INTEGER_CHOICES,blank=True,null=True)

    def __str__(self):
        return self.pitch1