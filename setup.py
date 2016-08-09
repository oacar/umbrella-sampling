from setuptools import setup

long_description = r"""
...
"""

setup(
    name='umbrella_sampling',
    version='0.0.0',
    description='...',
    long_description=long_description,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics'],
    keywords=['umbrella sampling'],
    url='https://github.com/oacar/umbrella-sampling',
    maintainer='',
    maintainer_email='',
    license='GPLv3+',
    setup_requires=[
        'numpy>=1.7',
        'setuptools>=0.6'],
    tests_require=[
        'numpy>=1.7',
        'nose>=1.3'],
    install_requires=[
        'numpy>=1.7',],
    packages=['umbrella_sampling'],
    test_suite='nose.collector',
    scripts=[]
)
