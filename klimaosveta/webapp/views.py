from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect
from webapp.models import BasicSite, Course, Lector
from webapp.forms import ContactForm

class Home(TemplateView):
    template_name = 'webapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = BasicSite.objects.get(name='home')
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        return self.render_to_response(self.get_context_data(form=form))


class CourseListView(ListView):
    model = Course
    template_name = 'webapp/courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all().order_by('order')


class LectorListView(ListView):
    model = Lector
    template_name = 'webapp/lectors.html'
    context_object_name = 'lectors'

    def get_queryset(self):
        return Lector.objects.all().order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basic_site'] = BasicSite.objects.get(name='lectors')
        return context
