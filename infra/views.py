from django.shortcuts import render


# Create your views here.
from infra.models import Demo
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def about(request):
    
    return render(request, 'about.html')

@require_http_methods(["GET"])
def project(request):
    return render(request, 'project.html')

@require_http_methods(["GET"])
def contact(request):
    return render(request, 'contact.html')
   

class DemoList(ListView):
    
    model = Demo
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    pass

class DemoDetail(DetailView):
    model = Demo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    pass


