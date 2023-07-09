from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-script',
    version='1.0.1',
    author='Santhosh Parthiban',
    author_email='santhoshparthiban2002@gmail.com',
    description='Django-Script is a Python package that automates the setup and configuration of Django applications.',
    keywords=['Django', 'script', 'setup', 'configuration', 'automation'],
    url = "https://pypi.org/project/django-script",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license = "MIT",
    packages=find_packages(),
    include_package_data=True,
    project_urls = {
        "Bug Tracker": "https://github.com/santhoshparthiban2002/Django-Script/issues",
    },
    entry_points={
        'console_scripts': [
            'django-script = master.main:djangoScript'
        ]
    },
    install_requires=['django','APScheduler'],
    classifiers=[
        'Topic :: Text Editors :: Text Processing',
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
    ],
)
