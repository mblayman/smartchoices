from setuptools import setup


setup(
    name='smartchoices',
    version='1.1',
    description='A smart choices interface for Django apps',
    author='Paul Hummer',
    author_email='paul@eventuallyanyway.com',
    url='https://github.com/rockstar/smartchoices',
    license='MIT',
    py_modules=('smartchoices',),
    install_requires=[
        'six',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
