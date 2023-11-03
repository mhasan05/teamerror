from django.shortcuts import render
from django.views import View
from .models import Portfolio,RelatedImage
from feedback.models import Feedback
from experience.models import Experience


class PortfolioView(View):
    def get(self, request, *args, **kwargs):
        all_Portfolio = Portfolio.objects.all()
        active_page = "Portfolio"
        data ={'all_Portfolio': all_Portfolio,'active_page':active_page}
        return render(request,'portfolio.html',context=data)
    
class PortfolioDetailsView(View):
    def get(self, request,uuid, *args, **kwargs):
        request_Portfolio = Portfolio.objects.get(uuid = uuid)
        related_image = RelatedImage.objects.all()
        feedback = Feedback.objects.all()
        experiences = Experience.objects.all()
        active_page = "Portfolio"
        star = range(0,5)
        data ={'request_Portfolio': request_Portfolio,'related_image': related_image,'feedback': feedback,'star': star,'experiences': experiences,'active_page':active_page}
        return render(request,'portfolio_details.html',context=data)