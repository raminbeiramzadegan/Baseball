from django.shortcuts import render
from django.views import View
from reports.models import HittingReport,PitchingReport,get_team_choices
import requests
from bs4 import BeautifulSoup





class HomeView(View):
    def logos_crawler(self):
        
        url = "https://www.mlb.com/news"
        response = requests.get(url)
        logos_list = []
        names_list = []
        team_info = {}
        get_list  = get_team_choices()
      
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            team_logo = soup.find_all('a',class_='header__subnav__item header__subnav--teams__team')[:30]
            for nav in team_logo:
              
                    img = nav.find('img',class_="header__subnav--teams__team--logo")
                    # name = nav.find('span',class_ = "header__subnav--teams__team--name")
                    logo = "https:"+ img.get('src')
                    # team_name = name.get_text()
                    logos_list.append(logo)
                    # names_list.append(team_name)
                    i = 0
                    for i in range(len(logos_list)):
                        team_info[get_list[i][0]] = logos_list[i]

        return team_info

    def news_crawler(self):

        url = "https://www.mlb.com/news"
        response = requests.get(url)
        news_list = []
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all('article')[:4]

            for article in articles:
                article_link = article.find("a",class_ ="p-button__link")
                headline = article.find("h1", class_="article-item__headline")
                article_date = article.find('div', class_='article-item__contributor-date')
                body = article.find('div', class_='article-item__preview')
                image = article.find('img')
                
                if image:
                    srcset = image.get("data-srcset")

                if srcset:
                    sources = srcset.split(',')

                    first = sources[0].strip().split(' ')[0]
                
                   
                    news = {
                            # 'article_id':article_id.get['id'] if article_id else '',
                            'headline': headline.get_text() if headline else '',
                            'image': first if first else '',
                            'date': article_date.get_text() if article_date else '',
                            'body': body.get_text() if body else '',
                            'link':article_link.get('href') if article_link else '',
                        }
                    
                    news_list.append(news)
                    
                    
        return news_list 
        

    
    def get(self,request):
        team_info = self.logos_crawler()
        news_list = self.news_crawler()
        hitreports = HittingReport.objects.all()    
        pitchreports = PitchingReport.objects.all()
        return render(request, 'home/home.html', {'hitreports': hitreports, 'news_list': news_list,'team_info':team_info,'pitchreports':pitchreports})