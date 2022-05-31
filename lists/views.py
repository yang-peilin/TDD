from django.shortcuts import render, redirect
from lists.models import Item, List
from django.http import HttpResponse

# Create your views here.

def home_page(request):
        # item = Item()
        # item.text = request.POST.get('item_text', '')
        # item.save()
        #
        # return render(request, 'home.html',{
        #     'new_item_text': item.text
        # })

        # if request.method == 'POST':
        #     Item.objects.create(text=request.POST['item_text'])
        #     return redirect('/lists/the-only-list-in-the-world/')

        return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text = request.POST['item_text'], list = list_)
    return redirect('/lists/the-only-list-in-the-world/')