from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.models import FlatPage
from django import forms
from codemirror2.widgets import CodeMirrorEditor
from webapp.models import BasicSite, Message, Course, Lector, Region, CourseDetail, CourseParticipant, FinalCourseParticipant
from django.utils.html import format_html
from imagekit.admin import AdminThumbnail

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



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'name', 'email_link', 'procesed')
    list_filter = ('procesed', 'timestamp')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('timestamp',)
    list_editable = ('procesed',)

    def email_link(self, obj):
        return format_html("<a href='mailto:{}'>{}</a>", obj.email, obj.email)
    email_link.short_description = "Email"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('headline', 'order', 'image_on_left', 'image_optimal_preview')
    list_editable = ('order', 'image_on_left')  # Umožňuje editaci 'order' a 'image_on_left' přímo v seznamu
    readonly_fields = ('image_optimal_preview',)
    fieldsets = (
        (None, {
            'fields': ('headline', 'html', 'image', 'shortcut', 'image_on_left', 'order', 'image_optimal_preview', 'program',),
        }),
    )

    def image_optimal_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" />', obj.image_optimal.url)
        else:
            return "No Image Uploaded"

    image_optimal_preview.short_description = 'Optimal Image Preview'


@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_image_preview', 'about_shortened', 'order')
    list_display_links = ('name',)
    search_fields = ('name', 'about')
    readonly_fields = ('admin_image_preview',)
    list_editable = ('order', )

    admin_image_preview = AdminThumbnail(image_field='image_admin')
    admin_image_preview.short_description = 'Optimal Image Preview'

    def about_shortened(self, obj):
        # Zkrátí text o lektorovi pro zobrazení v seznamu, pokud je příliš dlouhý
        return obj.about[:75] + '...' if len(obj.about) > 75 else obj.about
    about_shortened.short_description = 'About'


class CourseDetailInline(admin.TabularInline):
    model = CourseDetail
    extra = 1  # Kolik prázdných formulářů pro nové záznamy se má zobrazit



class CourseParticipantInline(admin.TabularInline):
    model = CourseParticipant
    extra = 1  # Kolik prázdných formulářů pro nové záznamy se má zobrazit

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CourseDetailInline]  # Přidání inline

@admin.register(CourseDetail)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display = ('region', 'date', 'course', 'lector', 'max_capacity', 'current_capacity')
    list_filter = ('region', 'date', 'course')
    search_fields = ('region__name', 'course__name', 'lector__name')
    inlines = [CourseParticipantInline]

@admin.register(CourseParticipant)
class CourseParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'course_detail', 'email', 'phone', 'note', 'confirm')
    list_filter = ('course_detail__region', 'confirm')
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ('confirmation_code', 'confirmation_code_expires')


@admin.register(FinalCourseParticipant)
class FinalCourseParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')
