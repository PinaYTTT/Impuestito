from setuptools import setup, find_packages

readme = open("./README.md", "r")


setup(
    name='impuestito',
    packages=['impuestito'],  # this must be the same as the name above
    version='0.4Beta',
    description='Impuestito es una API local para calcular impuestos al hacer compras al exterior,',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='PinaYT',
    author_email='contacto.pinayt@gmail.com',
    # use the URL to the github repo
    url='https://github.com/PinaYTTT/impuestito',
    download_url='https://github.com/PinaYTTT/impuestito',
    install_requires=['requests'],
    keywords=['impuestos', 'argentina', 'dolar'],
    classifiers=[ ],
    license='MIT',
    include_package_data=True
)