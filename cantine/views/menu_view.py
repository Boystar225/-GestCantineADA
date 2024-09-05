from django.shortcuts import render, get_object_or_404, redirect
from ..models.menu_model import Menu
from ..forms import MenuForm


# Create View
def create_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm()
    return render(request, 'menu_form.html', {'form': form})

# Read View
def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'cantine/index.html', {'menus': menus})

def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_detail.html', {'menu': menu})

# Update View
def update_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('cantine:menu_list')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'menu_form.html', {'form': form})

# Delete View
def delete_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('menu_list')
    return render(request, 'menu_confirm_delete.html', {'menu': menu})
