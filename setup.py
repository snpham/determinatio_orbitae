from setuptools import setup, find_packages

setup(
    name='determinatio',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Son Pham',
    author_email='snpham02@gmail.com',
    description='Orbit determination package for ASEN 5044',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/snpham/determinatio_orbitae',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)