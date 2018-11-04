from setuptools import setup, find_packages

setup(
    name='nemo',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
