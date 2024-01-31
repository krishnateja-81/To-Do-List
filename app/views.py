from django.shortcuts import render, redirect, get_object_or_404
from . import models


def home(request):
    item = models.ToDoItem.objects.all()
    items = {
        'items': item
    }
    return render(request, 'home.html', items)


def completed(request, item):
    item = get_object_or_404(models.ToDoItem, id=item)
    item.status = True
    item.save()
    
    return redirect('home')


def create(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        item = models.ToDoItem.objects.create(
            title = title,
            description = description
        )
        item.save()
    
    return redirect('home')



def delete_item(request, item):
    item = get_object_or_404(models.ToDoItem, id=item)
    item.delete()
    
    return redirect('home')


def update_item(request, item):
    item = get_object_or_404(models.ToDoItem, id=item)
    items = {'title': item.title, 'description': item.description}
    # print(item.description)
    # print(item)
    # for i in item:
    #     print(i.description, i.title)
    # print(item)
    if request.method=="POST":
        title = request.POST['title']
        description = request.POST['description']
        # item = models.ToDoItem.objects.get(id=item)
        item.title = title
        item.description = description
        item.save()
        return redirect('home')
    return render(request, 'update.html', items)