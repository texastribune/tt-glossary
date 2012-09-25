from django.conf import settings
from django.template import Context, Template
from django.test import TestCase

from glossary.models import Glossary, Term
from glossary.templatetags.glossary import get_context_variable


class TestGlossary(TestCase):
    def test_glossary_prepopulates_slug(self):
        g = Glossary(name=u'Higher Ed')
        g.save()
        self.assertEqual(g.slug, 'higher-ed')

    def test_glossary_has_terms(self):
        g = Glossary.objects.create(name=u'Public Ed')
        self.assertEqual(g.terms.count(), 0)

    def test_glossary_unicode(self):
        g = Glossary(name=u'Higher Ed')
        self.assertEqual(unicode(g), u'Higher Ed')

    def test_term_unicode(self):
        t = Term(name=u'THECB')
        self.assertEqual(unicode(t), u'THECB')

    def test_template_tags(self):
        g = Glossary.objects.create(name=u'Higher Ed')
        t = Term.objects.create(glossary=g, name=u'THECB',
                definition=u'Texas Higher Education Coordinating Board')
        context = Context({'object': t})
        template = Template("{% load glossary %}{% gloss object.name %}")
        variable = get_context_variable()
        html = template.render(context=context)
        self.assertEqual(html, '<dfn data-glossed="true">%s</dfn>' % t.name)
        self.assertTrue(variable not in context)
        template = Template("""
            {% load glossary %}
            {% load_glossary "Higher Ed" %}
            {% gloss object.name %}
        """)
        html = template.render(context=context)
        self.assertTrue('<dfn data-glossed="true"' in html)
        self.assertTrue('data-definition="%s"' % t.definition in html)
        self.assertTrue('>%s</dfn>' % t.name in html)
        self.assertTrue(variable in context)
