from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
    "distribute",
]


setup(name='checksum',
    version=version,
    description="Checksum utilities.",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      'Programming Language :: Python',
      'Development Status :: 2 - Pre-Alpha',
      'Topic :: Security',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
    ],
    keywords='',
    author='Eemil V\xc3\xa4is\xc3\xa4nen',
    author_email='eemil.vaisanen@gmail.com',
    url='https://github.com/vaiski/checksum',
    license='MIT',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    test_suite="checksum.test.test_all",
    entry_points={
    }
)
