try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Screenshot',
    'version': '0.1',
    'packages': ['screenshot', 'screenshot.lib'],
    'scripts': [],
    'name': 'screenshot',
    'entry_points': {
        'console_scripts': [
            'screenshot = screenshot.__main__:main'
        ]
    },
}

setup(**config)
