from setuptools import setup, find_packages

setup(
    name='blueproximity',
    version='1.2.5-1',
    description='Add security to your desktop by automatically locking and unlocking the screen when you and your phone leave/enter the desk.',
    license='GPL',
    packages=find_packages(),
    package_data={
        'blueproximity': [
            'proximity.glade',
            '*.svg',
        ],
    },
    entry_points={
        'console_scripts': [
            'blueproximity=blueproximity.proximity:main',
        ],
    },
)

