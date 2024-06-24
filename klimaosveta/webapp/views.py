from django.views.generic import TemplateView, ListView, DetailView, View
from django.shortcuts import redirect
from webapp.models import BasicSite, Course, Lector, CourseParticipant, Region, CourseDetail
from webapp.forms import ContactForm, CourseParticipantForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils.timezone import now


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

class RegionView(TemplateView):
    template_name = 'webapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = BasicSite.objects.get(name='region')
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        return self.render_to_response(self.get_context_data(form=form))


class AboutView(DetailView):
    model = BasicSite
    template_name = 'webapp/about.html'
    context_object_name = 'basic_site'

    def get_object(self):
        return get_object_or_404(BasicSite, name='about')


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

class ConfirmEmailView(View):
    def get(self, request, *args, **kwargs):
        confirmation_code = kwargs.get('confirmation_code')
        participant = get_object_or_404(CourseParticipant, confirmation_code=confirmation_code, confirm=False, confirmation_code_expires__gte=now())
        participant.confirm = True
        participant.save()
        return render(request, 'webapp/course_finish.html', {'participant': participant})

class RegionDetailView(DetailView):
    model = Region
    template_name = 'webapp/region_detail.html'
    context_object_name = 'region'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True


class CourseRegisterView(View):
    form_class = CourseParticipantForm
    template_name = 'webapp/course_register.html'  # Aktualizujte cestu k šabloně

    def get(self, request, *args, **kwargs):
        course_detail = get_object_or_404(CourseDetail, pk=kwargs['pk'])
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'course_detail': course_detail})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.course_detail = get_object_or_404(CourseDetail, pk=kwargs['pk'])
            participant.save()
            return render(request, 'webapp/course_confirm.html', {'participant': participant})
        return render(request, self.template_name, {'form': form, 'course': course.participant.course_detail})
