from __future__ import absolute_import

from django import template
from django.conf import settings

from glossary.models import Term

CONTEXT_VARIABLE = 'TT_GLOSSARY'

register = template.Library()


@register.simple_tag(takes_context=True)
def load_glossary(context, glossary_name):
    variable = getattr(settings, 'GLOSSARY_CONTEXT_VARIABLE', CONTEXT_VARIABLE)
    if not variable in context:
        context[variable] = {}

    glossary = context[variable]
    for term in Term.objects.filter(glossary__name=glossary_name):
        glossary[term.name] = term.definition


@register.simple_tag(takes_context=True)
def gloss(context, term_name):
    variable = getattr(settings, 'GLOSSARY_CONTEXT_VARIABLE', CONTEXT_VARIABLE)
    glossary = context.get(variable, {})
    definition = glossary.get(term_name)
    if definition:
        return u'<abbr class="gloss glossed" title="%s">%s</abbr>' % (
            definition, term_name)
    else:
        return u'<abbr class="gloss">%s</abbr>' % term_name
