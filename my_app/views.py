from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/d/services/search/bbb?query={}'
# Create your views here.
def home(request):
    return render(request,'base.html')

def new_search(request):
    models.Search.objects.create()
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    # print(quote_plus(search))
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    print(final_url)
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    post_listings = soup.find_all('li',{'class': 'result-row'})
    post_title = post_listings[0].find(class_='result-title').text
    post_url = post_listings[0].find('a').get('href')
    post_price = post_listings[0].find(class_='result-date')
    print(post_title)
    print(post_price)
    print(post_url)

    final_posting =[]

    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        post_price = post.find(class_='result-date').text
        final_posting.append((post_title,post_url,post_price))








    stuff_for_frontend = {
        'search':search,
        'final_posting':final_posting,
                          }
    return render(request, 'my_app/new_search.html',stuff_for_frontend)