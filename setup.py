from setuptools import setup, find_packages


setup(
    name='cohesion_measurement',
    version='0.1',
    license='MIT',
    author="Tom,Eden,Asaf",
    author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'Cohesion'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='cohesion, coherence',
    install_requires=[
          'scikit-learn',
      ],

)