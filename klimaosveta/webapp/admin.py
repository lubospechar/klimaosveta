from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.models import FlatPage
from django import forms
from codemirror2.widgets import CodeMirrorEditor
from webapp.models import BasicSite
@admin.register(BasicSite)
class BasicSiteAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.attname == "html":
            kwargs['widget'] = CodeMirrorEditor(options={'mode': 'htmlmixed', 'lineNumbers': True},
                                                modes=['css', 'xml', 'javascript', 'htmlmixed'])
        return super(BasicSiteAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.unregister(FlatPage)

# Definice formuláře pro úpravu obsahu FlatPage pomocí CodeMirrorEditor
class FlatPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CodeMirrorEditor(options={"mode": "htmlmixed", "lineNumbers": True},
                                                       modes=["css", "xml", "javascript", "htmlmixed"]))

    class Meta:
        model = FlatPage
        fields = "__all__"


@admin.register(FlatPage)
class CustomFlatPageAdmin(FlatPageAdminOld):
    form = FlatPageAdminForm


