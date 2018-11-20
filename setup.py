from setuptools import setup
import os
from distutils.util import convert_path

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.


def extract_version():
    version = None
    fnme = os.path.join(here, 'lib', 'best_route', '__init__.py')
    with open(fnme) as fd:
        for line in fd:
            if (line.startswith('__version__')):
                _, version = line.split('=')
                version = version.strip()[1:-1]  # Remove quotation characters
                break
    return version


def pip_requirements(name):
    fname = os.path.join(here, 'requirements', '{}.txt'.format(name))
    if not os.path.exists(fname):
        raise RuntimeError('Unable to find the {} requirements file at {}'
                           ''.format(name, fname))
    reqs = []
    with open(fname, 'r') as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            reqs.append(line)
    return reqs


# Returns the package and all its sub-packages
def find_package_tree(root_path, root_package):
    root_path = root_path.replace('/', os.path.sep)
    packages = [root_package]
    root_count = len(root_path.split(os.path.sep))
    for (dir_path, dir_names, file_names) in os.walk(convert_path(root_path)):
        # Prune dir_names *in-place* to prevent unwanted directory recursion
        for dir_name in list(dir_names):
            contains_init_file = os.path.isfile(os.path.join(dir_path,
                                                             dir_name,
                                                             '__init__.py'))
            if not contains_init_file:
                dir_names.remove(dir_name)
            # Exclude compiled PyKE rules, but keep associated unit tests.
            if dir_name == 'compiled_krb' and 'tests' not in dir_path:
                dir_names.remove(dir_name)
        if dir_names:
            prefix = dir_path.split(os.path.sep)[root_count:]
            packages.extend(['.'.join([root_package] + prefix + [dir_name])
                             for dir_name in dir_names])
    return packages


pypi_name = 'best_route'


with open(os.path.join(here, 'README.md'), 'r') as fh:
    description = ''.join(fh.readlines())


setup(
    name=pypi_name,
    version=extract_version(),
    description='A command-line tool for finding the shortest route '
                'between two given locations.',
    long_description=description,
    long_description_content_type='text/markdown',
    # url='',
    author='Corinne Bosley',
    author_email='corinne.e.bosley@gmail.com',
    packages=find_package_tree('lib/best_route', 'best_route'),
    package_dir={'': 'lib'},
    include_package_data=True,
    install_requires=pip_requirements('setup'),
    tests_require=['{}[test]'.format(pypi_name)],
    extras_require={'test': pip_requirements('test'),
                    'all': pip_requirements('all'),
                    },
    entry_points={'console_scripts': ['best_route=best_route.find:main']},
)