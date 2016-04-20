from django.template import Template, Context, TemplateSyntaxError
from django.test import SimpleTestCase


def _render(template):
    context = Context({})
    return Template('{% load capture_tags %}' + template).render(context)


class CaptureTagTests(SimpleTestCase):
    """
    Test the capture syntax
    """

    def test_capture(self):
        """- check: {% capture %}"""
        self.assertEqual(_render('{% capture %}foo{% endcapture %}!{{ capture }}'), 'foo!foo')

    def test_capture_block(self):
        """- check: {% block x %}{% capture %}{% endblock"""
        # Can't access outer context inside block yet.
        # This won't be possible, as the block could also be overwritten.
        self.assertEqual(_render('{% block x %}{% capture %}foo{% endcapture %}{% endblock %}!{{ capture }}'), 'foo!')

    def test_capture_as_var(self):
        """- check: {% capture as var %}"""
        self.assertEqual(_render('{% capture as var %}foo{% endcapture %}!{{ var }}'), 'foo!foo')

    def test_capture_silent(self):
        """- check: {% capture silent %}"""
        self.assertEqual(_render('{% capture silent %}foo{% endcapture %}!{{ capture }}'), '!foo')

    def test_capture_as_var_silent(self):
        """- check: {% capture as var silent %}"""
        self.assertEqual(_render('{% capture as var silent %}foo{% endcapture %}!{{ var }}'), '!foo')

    def test_capture_as_silent(self):
        """- check: {% capture as silent %}"""
        self.assertEqual(_render('{% capture as silent %}foo{% endcapture %}!{{ silent }}'), 'foo!foo')

    def test_syntax_errors(self):
        self.assertRaises(TemplateSyntaxError, _render, '{% capture %}foo')
        self.assertRaises(TemplateSyntaxError, _render, '{% capture AS bar silent %}foo{% endcapture %}')
        self.assertRaises(TemplateSyntaxError, _render, '{% capture as bar SILENT %}foo{% endcapture %}')
