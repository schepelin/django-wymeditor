from setuptools import setup
from wymeditor import get_version
setup(
        name = 'django-wymeditor',
        version = __import__('wymeditor').get_version(limit=3),
        author = 'Maxim Schepelin',
        author_email = 'm.schepelin@gmail.com',
        description = 'WYSIWYG editor widget',
        long_description = open('README.rst').read(),
        license = 'GPL',
        keywords = 'editor WYSIWYG',
        url = 'http://github.com/schepelin/django-wymeditor',
        packages = ['wymeditor',]
    )
