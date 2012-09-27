from django.contrib import admin

from glossary.models import Glossary, Term


class TermInline(admin.TabularInline):
    model = Term
    prepopulated_fields = {'slug': ('name',)}


class GlossaryAdmin(admin.ModelAdmin):
    model = Glossary
    prepopulated_fields = {'slug': ('name',)}
    inlines = [TermInline]

admin.site.register(Glossary, GlossaryAdmin)
