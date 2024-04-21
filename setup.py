import os
from glob import glob
from setuptools import setup

package_name = 'd2dtracker_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share', package_name), glob('rviz/*.rviz')),
        (os.path.join('share', package_name), glob('config/mavros/*.yaml')),
        (os.path.join('share', package_name), glob('config/kf/*.yaml')),
        (os.path.join('share', package_name), glob('config/geometric_controller/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mohamed Abdelkader',
    maintainer_email='mohamedashraf123@gmail.com',
    description='ROS 2 simulation packge of the D2DTracker system',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tf_node = d2dtracker_sim.tf_node:main',
            'offboard_control = d2dtracker_sim.offboard_control_node:main',
            'interceptor_offboard_control = d2dtracker_sim.interceptor_offboard_control_node:main',
            'gt_target_tf = d2dtracker_sim.gt_target_tf:main',
            'execute_random_trajectories = d2dtracker_sim.execute_random_trajectories_node:main',
            'gimbal_stabilizer = d2dtracker_sim.gimbal_stabilizer:main',

        ],

    },
)
