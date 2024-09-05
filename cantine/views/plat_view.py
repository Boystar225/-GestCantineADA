from django.shortcuts import render, get_object_or_404,redirect
from ..models.plat_model import Plat
from ..forms import PlatForm

def plat_list(request):
    plats = Plat.objects.all()
    return render(request, 'cantine/plats.html', {'plats': plats})

def plat_detail(request, plat_id):
    plat = get_object_or_404(Plat, id=plat_id)
    return render(request, 'cantine/plat_detail.html', {'plat': plat})



# Create View
def create_plat(request):
    if request.method == 'POST':
        form = PlatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plat_list')
    else:
        form = PlatForm()
    return render(request, 'plat_form.html', {'form': form})

# Read View
def plat_list(request):
    plats = Plat.objects.all()
    return render(request, 'plat_list.html', {'plats': plats})

def plat_detail(request, pk):
    plat = get_object_or_404(Plat, pk=pk)
    return render(request, 'plat_detail.html', {'plat': plat})

# Update View
def update_plat(request, pk):
    plat = get_object_or_404(Plat, pk=pk)
    if request.method == 'POST':
        form = PlatForm(request.POST, instance=plat)
        if form.is_valid():
            form.save()
            return redirect('plat_list')
    else:
        form = PlatForm(instance=plat)
    return render(request, 'plat_form.html', {'form': form})

# Delete View
def delete_plat(request, pk):
    plat = get_object_or_404(Plat, pk=pk)
    if request.method == 'POST':
        plat.delete()
        return redirect('plat_list')
    return render(request, 'plat_confirm_delete.html', {'plat': plat})
