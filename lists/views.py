from django.shortcuts import render, redirect
from lists.models import Item
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

        if request.method == 'POST':
            Item.objects.create(text=request.POST['item_text'])
            return redirect('/')

        items = Item.objects.all()
        return render(request, 'home.html', {'items': items})
