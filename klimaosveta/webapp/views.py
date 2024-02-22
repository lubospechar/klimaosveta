from django.views.generic import TemplateView
from django.shortcuts import redirect
from webapp.models import BasicSite
from webapp.forms import ContactForm

class Home(TemplateView):
    template_name = 'webapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Přidání obsahu stránky do kontextu
        context['page'] = BasicSite.objects.first()  # Příklad, jak načíst obsah
        context['form'] = ContactForm()  # Přidání prázdného formuláře
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('success_url')

        return self.render_to_response(self.get_context_data(form=form))
