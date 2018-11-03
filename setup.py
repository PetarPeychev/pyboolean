import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='pyboolean',
      version='0.1.post-3',
      description='Parse infix boolean expressions to RPN, evaluate and generate truth tables.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/PetarPeychev/pyboolean',
      author='PetarPeychev',
      author_email='petarpeychev98@gmail.com',
      packages=setuptools.find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: Public Domain",
          "Operating System :: OS Independent",
       ],)
