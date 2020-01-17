from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='zstat-cli',
    version='0.1.0',
    description='Bone-simple tool for generating basic numerical stats from stdin',
    long_description_content_type="text/markdown",
    long_description=readme,
    author='Zachary Wolfe',
    author_email='wolfe.zach@gmail.com',
    url='https://github.com/zdwolfe/zstat',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': ['zstat=zstat.command_line:main'],
    }
)

