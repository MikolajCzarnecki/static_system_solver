from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='static_system_solver',
      version='0.0.1',
      description='All Python package to solve underdetermined, many rigid-body problems with static friciton.',
      url='https://github.com/MikolajCzarnecki/static_system_solver/',
      author='Mikolaj Czarnecki and Radost Waszkiewicz',
      author_email='mikolajczarnecki235@gmail.com',
      long_description=long_description,
      long_description_content_type='text/markdown',  # This is important!
      project_urls = {
#          'Documentation': 'https://packagename.readthedocs.io',
          'Source': 'https://github.com/MikolajCzarnecki/static_system_solver/'
      },
      license='MIT',
      packages=['static_system_solver'],
      zip_safe=False)

