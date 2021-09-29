from setuptools import find_packages, setup, find_namespace_packages
setup(
    name='PyZoo',

    include_package_data=True,
    python_requires='>=3',

    packages=find_packages(include=['PyZoo', 'PyZoo.*']),
    
    data_files=[
        ('PyZoo', ['PyZoo/formatter/templates/DefaultMessages.json']),
        ('PyZoo', ['PyZoo/formatter/templates/DefaultVariables.json']),
    ],
    

    version='0.1.0',
    description='Python library for data validation',
    author='Alan Franzin',
    author_email='alan.franzin2011@gmail.com',
    license='MIT',
    install_requires = [], 
    setup_requires = ['pytest-runner'], 
    tests_require = ['pytest == 4.4.1'], 
    test_suite = 'tests', 


    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)