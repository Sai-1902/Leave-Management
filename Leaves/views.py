
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LeaveRequestForm
from .models import Leave
import calendar

@login_required
def leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = request.user
            leave.save()
            return redirect('leave_list')
    else:
        form = LeaveRequestForm()
    return render(request, 'leaves.html', {'form': form})

@login_required
def leave_list(request):
    leaves = Leave.objects.filter(user=request.user)
    return render(request, 'leave_list.html', {'leaves': leaves})

@login_required
def leave_count(request):
    user = request.user
    leaves = Leave.objects.filter(user=user)
    leave_count = len(leaves)
    return render(request, 'leave_count.html', {'leave_count': leave_count})

