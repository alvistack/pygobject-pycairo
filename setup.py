# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cairo']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pycairo',
    'version': '1.27.0',
    'description': 'Python interface for cairo',
    'long_description': 'None',
    'author': 'Christoph Reiter',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
