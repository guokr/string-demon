from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='string_demon',
      version='0.2',
      description='String Feature Extraction',
      url='http://github.com/guokr/string-demon',
      author='Jinyang Zhou',
      author_email='jinyang.zhou@guokr.com',
      license='MIT',
      packages=['string_demon'],
      zip_safe=False)
