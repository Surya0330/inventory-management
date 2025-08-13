from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import Brands





def index(request):
    items = Brands.objects.all()
    search_query = request.GET.get('q') 

    if search_query:
        items = items.filter(brand__icontains=search_query) | \
                items.filter(category__icontains=search_query) | \
                items.filter(model__icontains=search_query)

    
 
    return render(request, 'index.html', {'items': items})






def add_item(request):
    if request.method == "POST":
        brand = request.POST.get("brand")
        category = request.POST.get("category")
        model = request.POST.get("model")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        Brands.objects.create(
            brand=brand, category=category, model=model,
            quantity=quantity, price=price
        )
    return redirect("index")

def update_item(request, item_id):
    item = get_object_or_404(Brands, id=item_id)
    if request.method == "POST":
        item.brand = request.POST.get("brand")
        item.category = request.POST.get("category")
        item.model = request.POST.get("model")
        item.quantity = request.POST.get("quantity")
        item.price = request.POST.get("price")
        item.save()
    return redirect("index")

def delete_item(request, item_id):
    item = get_object_or_404(Brands, id=item_id)
    if request.method == "POST":
        item.delete()
    return redirect("index")

