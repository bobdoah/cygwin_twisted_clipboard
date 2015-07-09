from setuptools import setup, find_packages

setup(
    name='twisted_pyperclip',
    description="A twisted server which exposes the clipboard using the cross-platform pyperclip library",
    version='1.1',
    author='Bob Williams',
    author_email='robertwilliams1985@gmail.com',
    packages=find_packages(),
    url='https://github.com/bobdoah/twisted_pyperclip',
    entry_points={
        'console_scripts' : [
            'twisted-pyperclip-server = twisted_pyperclip.server:main',
        ]
    },
    install_requires=['Twisted>=15.2.1', 'pyperclip']
)
