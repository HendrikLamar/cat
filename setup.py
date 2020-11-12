from setuptools import setup

setup(name='claws-analysis-toolkit',
      version='0.1.1',
      description='Framework to handle the Claws data',
      url='https://github.com/HendrikLamar/cat',
      author='Hendrik Windel',
      author_email='hwindel@mpp.mpg.de',
      license='GPL-3.0',
      packages=['cat'],
      install_requires=['pandas', 'configparser'],
      zip_safe=False)

