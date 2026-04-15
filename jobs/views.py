from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import JobOffer, Application

def job_list(request):
    jobs = JobOffer.objects.filter(is_active=True)
    return render(request, 'jobs/list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(JobOffer, pk=pk)
    return render(request, 'jobs/detail.html', {'job': job})

@login_required
def apply(request, pk):
    job = get_object_or_404(JobOffer, pk=pk)
    if request.method == 'POST':
        cv           = request.FILES.get('cv')
        cover_letter = request.POST.get('cover_letter', '')
        if cv:
            Application.objects.create(
                offer=job,
                applicant=request.user,
                cv=cv,
                cover_letter=cover_letter
            )
            messages.success(request, 'Votre candidature a bien été envoyée !')
            return redirect('job_list')
        else:
            messages.error(request, 'Veuillez joindre votre CV.')
    return render(request, 'jobs/apply.html', {'job': job})