from django.shortcuts import render


def select(request):
    data = (20, 30, 10, 40)

    context = {
        'data': data
    }

    template = 'charts.html'

    return render(request, template, context)
