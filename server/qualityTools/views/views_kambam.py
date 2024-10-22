from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from qualityTools.models import Board, Column, Card
from qualityTools.forms import BoardForm, ColumnForm, CardForm

class BoardView(View):
    def get(self, request):
        boards = Board.objects.all()
        return render(request, 'qualityTools/board_list.html', {'boards': boards})

    def post(self, request):
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_list')
        return render(request, 'qualityTools/board_form.html', {'form': form})

class ColumnView(View):
    def get(self, request, board_id):
        board = get_object_or_404(Board, id=board_id)
        columns = Column.objects.filter(board=board)
        return render(request, 'qualityTools/column_list.html', {'board': board, 'columns': columns})

    def post(self, request, board_id):
        board = get_object_or_404(Board, id=board_id)
        form = ColumnForm(request.POST)
        if form.is_valid():
            column = form.save(commit=False)
            column.board = board
            column.save()
            return redirect('column_list', board_id=board.id)
        return render(request, 'qualityTools/column_form.html', {'form': form, 'board': board})

class CardView(View):
    def get(self, request, column_id):
        column = get_object_or_404(Column, id=column_id)
        cards = Card.objects.filter(column=column)
        return render(request, 'qualityTools/card_list.html', {'column': column, 'cards': cards})

    def post(self, request, column_id):
        column = get_object_or_404(Column, id=column_id)
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.column = column
            card.save()
            return redirect('card_list', column_id=column.id)
        return render(request, 'qualityTools/card_form.html', {'form': form, 'column': column})