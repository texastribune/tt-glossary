from __future__ import absolute_import

from django import template
from django.conf import settings

from glossary.models import Term

register = template.Library()


def get_context_variable():
    return getattr(settings, 'GLOSSARY_CONTEXT_VARIABLE', 'TT_GLOSSARY')


@register.simple_tag(takes_context=True)
def load_glossary(context, glossary_name):
    variable = get_context_variable()
    if not variable in context:
        context[variable] = {}

    glossary = context[variable]
    for term in Term.objects.filter(glossary__name=glossary_name):
        glossary[term.name] = term.definition


@register.simple_tag(takes_context=True)
def gloss(context, term_name):
    variable = get_context_variable()
    glossary = context.get(variable, {})
    definition = glossary.get(term_name)
    if definition:
        return u'<abbr class="gloss glossed" title="%s">%s</abbr>' % (
            definition, term_name)
    else:
        return u'<abbr class="gloss">%s</abbr>' % term_name
