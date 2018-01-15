try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    'description': 'A Practice Hello World Project',
    'author': 'JoeFly',
    'url': 'joefly.site',
    'download_url': 'joefly.site',
    'author_email': 'newitup@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['hello_world'],
    'scripts': [],
    'name': 'hello_world'
}

setup(**config)
