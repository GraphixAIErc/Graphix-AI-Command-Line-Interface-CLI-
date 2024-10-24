from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='graphix-cli',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'click==8.1.7',
        'requests==2.31.0',
        'colorama==0.4.6',
        'psutil==5.9.8',
        'python-socketio[client]==5.11.2',
        'keyring==25.2.0',
        'keyrings.alt==5.0.1',
        'speedtest-cli==2.1.3',
        'pandas==2.2.2',
        'transformers==4.40.2',
        'datasets==2.19.1',
        'py3nvml==0.2.7'
    ],
    entry_points={
        'console_scripts': [
            'graphix=graphix.cli:main'
        ]
    },
    author='Graphix AI',
    author_email='tech@graphix-ai.io',
    description='Graphix AI CLI Tool For GPU Lending',
    license='MIT',
    keywords='graphix cli gpu lending',
    url='https://www.graphix-ai.io',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
)