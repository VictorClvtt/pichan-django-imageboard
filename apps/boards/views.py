from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
import uuid

from . import models
from apps.threads.forms import ThreadForm
from apps.threads.models import Thread


class Board(View):

    def get(self, request, slug):
        board = get_object_or_404(models.Board, slug=slug)

        context = {
            "current_board": board,
            "slugs": models.Board.objects.values_list('slug', flat=True),
            "threads": Thread.objects.filter(board=board),
            "thread_form": ThreadForm
        }

        return render(request, 'boards/board.html', context)

    def post(self, request, slug):
        board = get_object_or_404(models.Board, slug=slug)
        form = ThreadForm(request.POST)

        if 'anon_id' not in request.session:
            request.session['anon_id'] = str(uuid.uuid4())

        if form.is_valid():
            thread = form.save(commit=False)
            thread.board = board
            thread.anon_id = request.session['anon_id']
            thread.save()

            return redirect('board', slug=slug)

        context = {
            "current_board": board,
            "slugs": models.Board.objects.values_list('slug', flat=True),
            "thread_form": form,
        }

        return render(request, 'boards/board.html', context)