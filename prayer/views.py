from django.shortcuts import get_object_or_404, redirect, render

from .forms import PrayerForm
from .models import Prayer


# Dashboard view
def dashboard_view(request):
    prayers = Prayer.objects.all()
    context = {"prayers": prayers}
    return render(request, "dashboard.html", context)


def prayer_view(request):
    if request.method == "POST":
        form = PrayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = PrayerForm()
    context = {"form": form}
    return render(request, "prayer/prayerForm.html", context)

def update_prayer(request, pk):
    prayer = get_object_or_404(Prayer, pk = pk)
    if request.method == "POST":
        form = PrayerForm(request.POST, instance=prayer)
        if form.is_valid():
            form.save()
            return redirect ('dashboard')
    else:
        form = PrayerForm(instance=prayer)
    context = {"form": form}
    return render(request, 'prayer/prayerForm.html', context)

def delete_prayer(request, pk):
    prayer = get_object_or_404(Prayer, pk=pk)
    if request.method == 'POST':
        prayer.delete()
        return redirect('dashboard')
    context = {"prayer": prayer}
    return render(request, 'prayer/delete_prayer.html', context)