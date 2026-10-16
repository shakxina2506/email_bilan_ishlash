from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.views.generic import CreateView,TemplateView,FormView
from .utils import generate_activation_code
from .service import send_activation_email


class UserCreationView(CreateView):

    form_class = RegisterForm
    template_name = 'users/register.html'
    context_object_name = 'user'
    success_url = reverse_lazy('code_sent')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        code=generate_activation_code()
        send_activation_email(user.email, code)
        return super().form_valid(form)

class CodeSentView(TemplateView):
     template_name = 'users/code_sent.html'



@login_required
def profile(request):
    context = {'user': request.user}
    return render(request, 'users/profile.html', context)