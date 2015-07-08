from setuptools import setup, find_packages

setup(
    name='cygwin_twisted_clipboard',
    description="A twisted server which exposes cygwin's /dev/clipboard",
    version='1.0',
    author='Bob Williams',
    author_email='robertwilliams1985@gmail.com',
    packages=find_packages(),
    url='https://github.com/bobdoah/cygwin_twisted_clipboard',
    entry_points={
        'console_scripts' : [
            'cygwin-twisted-clipboard-server = cygwin_twisted_clipboard.server:main',
        ]
    },
    install_requires=['Twisted>=15.2.1', ]
)
