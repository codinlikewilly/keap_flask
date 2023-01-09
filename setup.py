from setuptools import setup

setup(
    name='keap-flask',
    version='0.1.0',
    description='A Rest Client For Flask applications',
    author='will sexton',
    author_email='will@theapiguys.com',
    url='https://github.com/codinlikewilly/flask-keap',
    license='BSD 2-clause',
    packages=['flask-keap'],
    install_requires=['Flask',
                      'AuthLib',
                      'python-dateutil'
                      ],

    classifiers=[
        'License :: OSI Approved :: BSD License'
    ],
)
