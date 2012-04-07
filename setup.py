from setuptools import find_packages
from setuptools import setup
import os

VERSION = '0.3.0'


setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    classifiers=[
      "Framework :: Plone",
      "Programming Language :: Python",
      ],
    description="A tool to mock up ad hoc forms in Plone",
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
    keywords='html form marshall zope',
    license='GPL',
    long_description=(
        open("README.rst").read() +
        open(os.path.join("docs", "INSTALL.txt")).read() +
        open(os.path.join("docs", "HISTORY.txt")).read()
    ),
    namespace_packages=[
        'collective'
    ],
    name='collective.formtoy',
    packages=find_packages(),
    url='http://svn.plone.org/svn/collective/',
    version=VERSION,
    zip_safe=False,
)
