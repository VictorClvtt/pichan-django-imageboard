from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from . import models

class Board(View):
    
    def get(self, request, slug):
        

        context = {
            "current_board": get_object_or_404(models.Board, slug=slug),
            "slugs": models.Board.objects.values_list('slug', flat=True)
        }

        return render(request, 'boards/board.html', context)
