from setuptools import setup

DEPENDENCIES = ['pytest', 'pytest-cov']

setup(name='trigrams',
      description="""Given a text file and a number of words,
      our function creates a new randomized story.""",
      version='0.1', author='Elyanil Liranzo-Castro, Carlos Cadena',
      author_email="yanil3500@gmail.com, cs.cadena@gmail.com", license="MIT",
      py_modules=['trigrams'], package_dir={'': 'src'},
      install_requires=DEPENDENCIES,
      entry_points={'console_scripts': ['trigrams = trigrams:main']}
      )
