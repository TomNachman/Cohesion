from setuptools import setup, find_packages

# TODO run 'python setup.py sdist' in-order to create the
#  source distribution of the package after finished the code
setup(
    name='cohesion_measurement',
    version='0.1',
    license='MIT',
    author="Tom,Eden,Asaf",
    author_email='nachmant@post.bgu.ac.il',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/TomNachman/Cohesion',
    keywords='cohesion, coherence',
    install_requires=[
        'pandas', 'nltk', 'scikit-learn', 'numpy', 'transformers', 'setuptools', 'scipy', 'gensim'
    ],
)
