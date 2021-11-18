import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "QWindowButtons\\README.md").read_text()
setup(
	name='QWindowButtons',
	version='1.0.0',
	description='desc',
	long_description=README,
	long_description_content_type="text/markdown",
	url='https://github.com/Prx001/QWindowButtons',
	author='Parsa.py',
	author_email='munichbayern2005@gmail.com',
	license='MIT License',
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: Implementation :: CPython"
	],
	packages=['QWindowButtons'],
	include_package_data=True,
	install_requires=["PyQt5"]
)
