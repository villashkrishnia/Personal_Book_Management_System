from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import Bookform
from .filters import BookFilter
from .models import Book

@login_required(login_url='login')
def dash(request):
    user = request.user
    books = user.book_set.all()
    myFilter = BookFilter(request.GET,queryset=books)
    books=myFilter.qs
    totalbooks = books.count()
    return render(request, 'book/dash.html', {'books': books,
                                              'myFilter':myFilter,
                                              'totalbooks': totalbooks,
                                                       })


@login_required(login_url='login')
def add_book(request):
    if request.method == 'POST':
        form = Bookform(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            book = form.save()
            return redirect('dash')
    else:
        form = Bookform()
    return render(request, 'book/add_book.html', {'form': form})


@login_required(login_url='login')
def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "POST":
        book.delete()
        return redirect('dash')
    return render(request,'book/delete_book.html',{'book':book})


@login_required(login_url='login')
def edit_book(request,pk):
    book=Book.objects.get(id=pk)
    if request.method=="POST":
        form = Bookform(data=request.POST,instance=book)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('dash')
    else:
        form=Bookform(instance=book)
    return render(request, 'book/add_book.html', {'form': form})
