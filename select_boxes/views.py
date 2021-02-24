from django.shortcuts import render, redirect

from select_boxes.models import Items


def select(request):

    if request.method == 'POST':
        selected = request.POST.get('id-selected')
        ids_split = selected.split(",")
        for id in ids_split:
            Items.objects.filter(id=id).delete()

    qs = Items.objects.all()

    context = {
        'items': qs
    }

    template = 'select.html'

    return render(request, template, context)
