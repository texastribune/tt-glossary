from __future__ import absolute_import

from django import template

from glossary.models import Term

register = template.Library()


@register.simple_tag(takes_context=True)
def load_glossary(context, glossary):
    # TODO: Load the specified glossary to the context
    pass


@register.simple_tag(takes_context=True)
def gloss(context, term):
    term = Term.objects.get(name=term)
    return u'<abbr class="gloss glossed" title="%s">%s</abbr>' % (
        term.definition, term.name)
