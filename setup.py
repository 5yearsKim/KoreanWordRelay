from setuptools import setup


def parse_requirements(requirements):
    with open(requirements) as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]

reqs = parse_requirements('./requirements.txt')

setup(
    name='korean_word_relay',
    version='0.0.1',
    author='5yearsKim',
    author_email='hypothesis22@gmail.com',
    description='python implementation for korean word playing game',
    packages=['korean_word_relay'],
    install_requires=reqs,
    package_data={
      '': ['data/*']
    }
)