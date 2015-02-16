from setuptools import setup, find_packages

setup(
    name='cdeploy',
    version='1.1',
    description='A tool for managing Cassandra schema migrations',
    author='David McHoull',
    author_email='dmchoull@gmail.com',
    license='http://www.apache.org/licenses/LICENSE-2.0',
    url='https://github.com/rackerlabs/cdeploy',
    keywords=['cassandra', 'migrations'],
    packages=find_packages(),
    install_requires=['PyYAML', 'cassandra-driver'],
    tests_require=['mock'],
    test_suite="cdeploy.test",
    entry_points={
        'console_scripts': [
            'cdeploy = cdeploy.migrator:main'
        ]
    }
)
