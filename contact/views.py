from contact.forms import ContactForm
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.urls import reverse 


class ContactFromView(FormView):
    template_name = 'contact-form.html'
    form_class = ContactForm
    success_url = reverse('contact')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
