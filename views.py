from django.shortcuts import render,redirect
from .models import receipe

def add_receipe(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')

        print(name)
        print(description)

        
        image = request.FILES.get('image')
        print(image)
        receipe.objects.create(name=name,
                               description=description,
                               image=image)

        return redirect('/receipe/')

    queryset=receipe.objects.all()
    context={"receipes":queryset}
    return render(request, "receipe.html",context)
def delete_receipe(request,id):
    receipe.objects.get(id=id).delete()
    return redirect('/receipe/')
def update_receipe(request,id):
    queryset=receipe.objects.get(id=id)
    context={"receipe":queryset}
    return render(request,"update_receipe.html",context)
