from setuptools import setup, find_packages
setup(
    author = 'Anahit Manukyan, Milena Bazoyan, Lusine Torosyan, Sate Antaranyan',
    description= 'A package for predicting fashion trends',
    name = 'EcoTrendz',
    version = '0.1.0',
    packages = find_packages(include = ['FashionTrendForecasting', 'FashionTrendForecasting.*'])
)
