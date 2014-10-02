from django.views.decorators.cache import cache_page
from django.shortcuts import render_to_response

import time


@cache_page(10)
def home(request):
    time.sleep(2)
    return render_to_response('home/home.html')
