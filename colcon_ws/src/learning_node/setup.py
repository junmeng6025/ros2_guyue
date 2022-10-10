from setuptools import setup

package_name = 'learning_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jun',
    maintainer_email='mengjun6025@163.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ # <node_name> = <pkg_name>.<node_filename>:<func_name>
        'node_helloworld = learning_node.node_helloworld:main',
        'node_helloworld_oop = learning_node.node_helloworld_class:main'
        ],
    },
)
