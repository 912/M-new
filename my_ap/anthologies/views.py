from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from anthologies.models import Book

# Create your views here.
def index(request):
    latest_book_list = Book.objects.order_by('price')[:5]
    output = ', '.join([p.book_text for p in latest_book_list])
    template = loader.get_template('anthologies/index.html')
    context = RequestContext(request, {'latest_book_list': latest_book_list,
})
def bookdetails(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'anthologies/detail.html', {'book': book})
    return HttpResponse("You're looking at book %s." % book_id)
    return HttpResponse(template.render(context))
    return HttpResponse(output)  
    return HttpResponse("Hello, world. You're at the anthologies store.")






