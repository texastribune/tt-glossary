from django.template import Context, Template
from django.test import TestCase

from glossary.models import Glossary, Term


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
        html = template.render(context=context)
        self.assertEqual(html, '<abbr class="gloss">%s</abbr>' % t.name)
        template = Template("""
            {% load glossary %}
            {% load_glossary "Higher Ed" %}
            {% gloss object.name %}
        """)
        html = template.render(context=context)
        self.assertTrue('<abbr class="gloss glossed"' in html)
        self.assertTrue('title="%s"' % t.definition in html)
        self.assertTrue('>%s</abbr>' % t.name in html)
