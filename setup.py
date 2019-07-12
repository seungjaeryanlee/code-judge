from setuptools import setup


setup(
    name='code-judge',
    version='0.0.0',
    description='Offline code judge system for coding interview questions',
    url='https://github.com/seungjaeryanlee/code-judge',
    author='Seungjae Ryan Lee',
    author_email='seungjaeryanlee@gmail.com',
    license='MIT',
    packages=['cj'],
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'judge = cj.command_line:judge',
        ],
    },
)
