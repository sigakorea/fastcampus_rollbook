from django.shortcuts import render
from attend.models import Attend


def index(request):
    attend_list = Attend.objects.all()
    return render(request, 'attend/index.html', {
        'attend_list': attend_list
    })
