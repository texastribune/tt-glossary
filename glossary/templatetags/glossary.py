from __future__ import absolute_import

from django import template
from django.conf import settings

from glossary.models import Term

register = template.Library()


def get_context_variable():
    return getattr(settings, 'GLOSSARY_CONTEXT_VARIABLE', 'TT_GLOSSARY')


def get_or_create_context_glossary(context):
    variable = get_context_variable()
    if not variable in context:
        context[variable] = {}

    return context[variable]


@register.simple_tag(takes_context=True)
def load_glossary(context, glossary_name):
    glossary = get_or_create_context_glossary(context)
    for term in Term.objects.filter(glossary__name=glossary_name):
        glossary[term.name.lower()] = term
    return ''


@register.inclusion_tag('glossary/includes/dfn.html', takes_context=True)
def gloss(context, term_name):
    glossary = get_or_create_context_glossary(context)
    lower_term_name = term_name.lower()
    if lower_term_name in glossary:
        term = glossary[lower_term_name]
        term.name = term_name
    else:
        term = term_name
    return {'term': term}
