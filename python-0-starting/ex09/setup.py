from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    url='https://github.com/folim/ft_package',
    author='folim',
    author_email='folim@student.42kl.edu.my',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    classifiers=[],
    entry_points={
        'console_scripts': [],
    },
)

# [build-system]
# requires = ["hatchling"]
# build-backend = "hatchling.build"

# [project]
# name = "ft_package"
# version = "0.0.1"
# authors = [{ name="folim" }, { email="folim@student.42kl.edu.my" }]
# description = "A sample test package"
# readme = "README.md"
# requires-python = ">=3.10"

# [project.urls]
# Homepage = 'https://github.com/folim/ft_package'
