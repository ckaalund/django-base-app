from django.http import HttpResponse
from django.views.decorators.cache import cache_page

import time


@cache_page(10)
def home(request):
    time.sleep(2)
    return HttpResponse("Hello beautiful")
