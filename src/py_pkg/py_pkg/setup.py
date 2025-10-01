from setuptools import find_packages, setup

package_name = 'py_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robo',
    maintainer_email='robo@todo.todo',
    description='Simple example ROS 2 Python package (first_node).',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'py_node = py_pkg.py_node:main',
            "robot_news_publisher = py_pkg.robot_news_publisher:main",
            "robot_news_subscriber = py_pkg.robot_news_subscriber:main",
            "add_two_ints_server = py_pkg.add_two_ints_server:main",
            "add_two_ints_client = py_pkg.add_two_ints_client:main"
        ],
    },
)
