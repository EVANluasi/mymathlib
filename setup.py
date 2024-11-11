from setuptools import setup, find_packages

setup(
    name='mymathlib',
    version='0.1',
    packages=find_packages(),
    description='Coba-coba bikin library. Library ini dielengkapi Fitur Aljabar, Kalkulus, Statistik, dan Optimasi',
    author='Kei',
    author_email='fvan9318@gmail.com',
    url='https://github.com/EVANluasi/mymathlib.git',
    install_requires=[
        'numpy', 
        'scipy'
    ],
)
