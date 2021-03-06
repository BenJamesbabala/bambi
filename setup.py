import sys
from setuptools import setup, find_packages
from os.path import join, dirname

__version__ = '0.0.3'

if len(set(('test', 'easy_install')).intersection(sys.argv)) > 0:
    import setuptools

requirements = ['numpy', 'pandas', 'patsy', 'statsmodels']
dependency_links = ['git://github.com/pymc-devs/pymc3.git#egg=pymc3']

tests_require = []
extra_setuptools_args = {}
if 'setuptools' in sys.modules:
    tests_require.append('nose')
    extra_setuptools_args = dict(
        test_suite='nose.collector',
        extras_require=dict(
            test='nose>=0.10.1')
    )

print(requirements)
setup(
    name="bambi",
    version=__version__,
    description="BAyesian Model Building Interface in Python",
    url='http://github.com/bambinos/bambi',
    download_url='https://github.com/bambinos/bambi/archive/%s.tar.gz' % __version__,
    install_requires=requirements,
    dependency_links=dependency_links,
    maintainer='Tal Yarkoni',
    maintainer_email='tyarkoni@gmail.com',
    packages=find_packages(exclude=['tests', 'test_*']),
    package_data={'bambi': ["config/*"]},
    tests_require=tests_require,
    license='MIT',
    **extra_setuptools_args
)
