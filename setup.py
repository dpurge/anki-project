from setuptools import setup, find_packages

setup(
    name = 'ankiproject',
    version = '0.0.1',
    description = 'Build Anki packages from data',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    install_requires = [
       "genanki",
       "Jinja2",
       "PyYAML",
       "Markdown"
    ]
)