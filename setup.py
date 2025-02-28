from setuptools import find_packages, setup
from glob import glob

package_name = 'rb3_utils'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Om Patil',
    maintainer_email='s4patil@ucsd.edu',
    description='A set of ROS utilities for the Qualcomm RB3',
    license='MIT',
    entry_points={
        'console_scripts': [
            'camera_viewer = rb3_utils.camera_viewer:main',
        ],
    },
)
