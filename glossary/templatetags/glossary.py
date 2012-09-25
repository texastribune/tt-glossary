from __future__ import absolute_import

from django import template

from glossary.models import Term

GLOSSARY_CONTEXT_VARIABLE = 'TT_GLOSSARY'

register = template.Library()


@register.simple_tag(takes_context=True)
def load_glossary(context, glossary_name):
    if not GLOSSARY_CONTEXT_VARIABLE in context:
        context[GLOSSARY_CONTEXT_VARIABLE] = {}
    context_glossary = context[GLOSSARY_CONTEXT_VARIABLE]
    for term in Term.objects.filter(glossary__name=glossary_name):
        context_glossary[term.name] = term.definition


@register.simple_tag(takes_context=True)
def gloss(context, term_name):
    glossary = context.get(GLOSSARY_CONTEXT_VARIABLE, {})
    definition = glossary.get(term_name)
    if definition:
        return u'<abbr class="gloss glossed" title="%s">%s</abbr>' % (
            definition, term_name)
    else:
        return u'<abbr class="gloss">%s</abbr>' % term_name
