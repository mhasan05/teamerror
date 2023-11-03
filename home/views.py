from django.shortcuts import render,HttpResponse
from django.views import View
from services.models import Services,Package
from feedback.models import Feedback
from experience.models import Experience


class HomeView(View):
    def get(self, request, *args, **kwargs):
        services = Services.objects.all()
        packages = Package.objects.all()
        feedbacks = Feedback.objects.all()
        experiences = Experience.objects.all()
        active_page = "Home"
        star = range(0,5)
        data = {
            "services": services,
            "packages": packages,
            "feedbacks": feedbacks,
            "experiences": experiences,
            "active_page": active_page,
            "star": star,
        }
        return render(request,'home.html',context=data)