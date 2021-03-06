from distutils.core import setup

setup(
    name = "django-scripts",
    version = "0.1.0",
    description = "Store use python scripts from within django.",
    url = "https://github.com/thanos/django-scripts",
    author = "thanos vassilakis",
    author_email = "thanos@synatzo.com",
    packages = [
        "test_projects/scripts",
        
    ],
    classifiers = [
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
    install_requires=[
        "django-reversion",
    ],
)