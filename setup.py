from setuptools import setup

setup(
    name='snapshotalyzer-3000',
    version='0.1',
    author="Tee Josh",
    author_email= 'insanebreed@gmail.com',
    description="Snapshotalyzer 3000 is a toll to manage AWS EC2 snapshots",
    license= "GPLV3+",
    packages=['shotty'],
    url="https://github.com/Teejsh/snapshotalyzer-3000",
    install_requires=['click', 'boto3'],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''
    )
