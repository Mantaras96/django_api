from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.views import View

from .models import Company


class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        companies= list(Company.objects.values())
        if len(companies)> 0:
            datos = {'message':"Success",'companies':companies}
        else:
            datos = {'message': "Success", 'companies': companies}
        return JsonResponse(datos);

    def post(self, request):
        
        datos = {'message': "Success"}
        return JsonResponse(datos);

    def put(self, request):
        pass

    def delete(self, request):
        pass