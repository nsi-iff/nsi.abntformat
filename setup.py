from setuptools import setup, find_packages

version = '0.1.0'
readme = open('README.rst').read()

setup(name='nsi.abntformat',
      version=version,
      description='Transforma objetos contendo metadados de documentos em referências bibliográficas no formato ABNT.',
      long_description=readme,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.4',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries',
      ],
      keywords='referencia bibliografica ABNT documento formato',
      author='Ruhan Ferreira Almeida',
      author_email='ruhanfa@gmail.com',
      url='https://github.com/nsi-iff/nsi.abntformat',
      license='GNU General Public License',
      packages=find_packages(),
      )

