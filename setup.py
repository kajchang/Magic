from setuptools import setup

setup(
	name='st4ck',
	packages=['st4ck'],
	install_requires=[
		'requests',
		'bs4',
		'plotly',
		'matplotlib'
	],
	entry_points={
		'console_scripts': [
			'st4ck = st4ck.__main__:main']
	}
)
