from django.forms import Textarea
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.conf import settings

from conf import settings as wym_settings 

def get_setting(setting_name):
    if hasattr(wym_settings, setting_name):
        return mark_safe(getattr(wym_settings, setting_name))
    else:
        return ""

class WYMEditor(Textarea):
    class Media:
        js = [
            '//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.js',
            settings.STATIC_URL + 'wymeditor/wymeditor/jquery.wymeditor.js',
        ]

    def __init__(self, attrs=None, skin='django'):
        self.attrs = {'class': 'wymeditor'}
        self.skin = skin
        if attrs:
            self.attrs.update(attrs)
        super(WYMEditor, self).__init__(attrs)

    def render_textarea(self, name, value, attrs=None):
        return super(WYMEditor, self).render(name, value, attrs)

    def render_additions(self, name, value, attrs=None):
        language = settings.LANGUAGE_CODE[:2]
        context = {
            'name': name,
            'language': language,
            'skin': self.skin,
            'STATIC_URL': settings.STATIC_URL,
            'WYM_TOOLS': get_setting('WYM_TOOLS'),
            'WYM_CONTAINERS': get_setting('WYM_CONTAINERS'),
            'WYM_CLASSES': get_setting('WYM_CLASSES'),
            'WYM_STYLES': get_setting('WYM_STYLES'),
            'WYM_STYLESHEET': get_setting('WYM_STYLESHEET'),
        }
        return mark_safe(render_to_string(
            'widgets/wymeditor.html', context))

    def render(self, name, value, attrs=None):
        return self.render_textarea(name, value, attrs) + \
            self.render_additions(name, value, attrs)