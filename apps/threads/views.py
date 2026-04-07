from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
import uuid

from apps.boards.models import Board
from .forms import ThreadForm


class Thread(View):

    def post(self, request, slug):
        board = get_object_or_404(Board, slug=slug)
        form = ThreadForm(request.POST, request.FILES)

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
            "threads": board.threads.all(),
            "thread_form": form,
        }

        return render(request, 'boards/board.html', context)