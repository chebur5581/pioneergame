from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='pioneergame',
    version='0.0.1',
    author='chebur5581',
    author_email='chebur5581@gmail.com',
    description='Simple Pygame plugin for small kids',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='your_url',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='files speedfiles ',
    project_urls={
        'GitHub': 'your_github'
    },
    python_requires='>=3.6'
)
