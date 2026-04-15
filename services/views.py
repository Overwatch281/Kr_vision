from django.shortcuts import render
from .models import Service

from .models import Service, Partner

def home(request):
    services = Service.objects.filter(is_active=True)[:3]
    partners = Partner.objects.filter(is_active=True)
    return render(request, 'home.html', {
        'services': services,
        'partners': partners,
    })

def service_list(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'services/list.html', {'services': services})

from django.db.models import Q
from jobs.models import JobOffer
from blog.models import Article

def search(request):
    query    = request.GET.get('q', '')
    services = []
    jobs     = []
    articles = []

    if query:
        services = Service.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            is_active=True
        )
        jobs = JobOffer.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            is_active=True
        )
        articles = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            is_published=True
        )

    return render(request, 'search.html', {
        'query':    query,
        'services': services,
        'jobs':     jobs,
        'articles': articles,
    })