from setuptools import setup

setup(name='funniest99',
      version='0.2',
      description='The funniest joke in the world',
      long_description=readme()
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['funniest'],
      install_requires=['markdown'],
      zip_safe=False)
