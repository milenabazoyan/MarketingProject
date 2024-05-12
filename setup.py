from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    author='Anahit Manukyan, Milena Bazoyan, Lusine Torosyan, Sate Antaranyan',
    author_email='info@fashiontrendforecasting.com',
    description='A package for predicting fashion trends',
    long_description=long_description,
    long_description_content_type="text/markdown",
    name='FashionTrendForecasting',
    version='0.1.0',
    packages=find_packages(include=['FashionTrendForecasting', 'FashionTrendForecasting.*']),
    install_requires=[
        'numpy>=1.26.4',             
        'pandas>=2.2.1',             
        'scikit-learn>=1.4.2',      
        'matplotlib>=3.9.0',         
        'sqlalchemy>=2.0.29',        
        'fastapi>=0.110.0',          
        'uvicorn>=0.29.0',           
    ],
    python_requires='>=3.10',      
    classifiers=[
        'Development Status :: 4 - Beta',  # package is in the beta stage
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    license="MIT license",
    keywords='fashion trend forecasting machine learning',
    zip_safe=False,
)
