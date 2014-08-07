try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
    'description':'Network Tests',
    'author':'Luis B',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'lmbeccaria@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['network_connection'],
    'scripts': [],
    'name': 'network_connection'
    }

setup(**config)
