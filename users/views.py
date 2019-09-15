from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class SignUpView(CreateView):

    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def post(self, request):
        my_data = request.POST
        print (my_data)

# Create your views here.

