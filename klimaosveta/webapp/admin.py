from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from codemirror2.widgets import CodeMirrorEditor
from django import forms

admin.site.unregister(FlatPage)


class FlatPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CodeMirrorEditor(options={'mode': 'htmlmixed', 'lineNumbers': True},
                                                modes=['css', 'xml', 'javascript', 'htmlmixed']))

    # content = CharField()

    class Meta:
        model = FlatPage
        fields = '__all__'


@admin.register(FlatPage)
class CustomFlatPageAdmin(FlatPageAdmin):
    form = FlatPageAdminForm
