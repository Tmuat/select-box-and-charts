from django.shortcuts import render


def select(request):

    context = {
    }

    template = 'select.html'

    return render(request, template, context)
