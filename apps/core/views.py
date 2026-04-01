from django.shortcuts import render
from django.http import HttpResponse
from apps.boards.models import Board

def home(request):
    boards = Board.objects.all()

    context = {
        "boards": boards
    }

    return render(request, 'core/home.html', context)