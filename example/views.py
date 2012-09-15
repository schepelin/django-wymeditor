from django.views.generic import FormView
from example.forms import ExampleForm


class ExampleFormView(FormView):
    form_class = ExampleForm
    success_url = '/'
    template_name='index.html'
