from setuptools import setup, find_packages

classifiers = [
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='wikipedia_tool',
  version='1.0.0',
  description='API wrapper',
  long_description=open('README.md').read(),
  url='https://github.com/spy404/wikipedia_tool',  
  author='spy404',
  author_email='tahadaneshmand.2009@proton.me',
  license='MIT', 
  classifiers=classifiers,
  keywords=['wikipedia', 'api', 'tool', 'spy404'], 
  packages=find_packages(),
  install_requires=['requests'] 
)
