from setuptools import setup;

setup(
    name='bagoftools-core',
    version='0.1',
    packages=['src'],
    include_package_data=True,
    install_requires=[
        'Click',
        'nltk'
    ],
    entry_points='''
        [console_scripts]
        bagoftools=src.__main__:cli
    ''',
)