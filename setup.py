from setuptools import setup

def parse_requirements(requirements):
    with open(requirements) as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]

reqs = parse_requirements('./requirements.txt')
print(reqs)
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

print(type(long_description))


setup(
    name='korean_word_relay',
    version='0.0.5',
    author='5yearsKim',
    author_email='hypothesis22@gmail.com',
    url='https://github.com/5yearsKim/korean_word_relay',
    project_url='https://pypi.org/project/korean-word-relay/',
    description='끝말잇기 package for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['korean_word_relay'],
    install_requires=reqs,
    package_data={
      '': ['data/*']
    }
)