from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import TodoItems

# Create your views here.
class MyTodoApp(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        todo_list = TodoItems.objects.all()
        context = super().get_context_data(**kwargs)
        context['todo_list'] =  todo_list
        return context


    

class RedirectToA(TemplateView):

    def post(self, request):
        new_todo_item = request.POST['Enter']
        if new_todo_item != '' :
            my_item = TodoItems(todo_items = new_todo_item)
            my_item.save()
        
        return HttpResponseRedirect('/')


    
class RedirectToB(TemplateView):

    def post(self, request):
        a = request.POST['items']
        todo_all_items = TodoItems.objects.all()
        for x in todo_all_items:
            if str(x.id) == a:
                x.delete()
                break
        return HttpResponseRedirect('/')