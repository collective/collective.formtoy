# based on http://www.teamrubber.com/blog/cookin-with-traverse_subpath/

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserPage

class FormToy(BrowserPage):

    def __init__(self, context, request):
        self.context = context  # Use Martin's aq_magic
        self.request = request
        self._path = []

    def publishTraverse(self, request, name):
        self._path.append(name)
        return self

    @property
    def traverse_subpath(self):
        return self._path

    __call__ = ViewPageTemplateFile('formtoy.pt')

    def check_params(self):
        if len(self._path) > 0:
            return True
        else:
            return False
