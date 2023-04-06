import os
import sys
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    PX4_DIR = os.getenv('PX4_DIR')

    if PX4_DIR is not None:
        print(f'The value of PX4_DIR is {PX4_DIR}')
    else:
        print('PX4_DIR is not set')
        sys.exit(1)

    headless = LaunchConfiguration('headless')
    headless_launch_arg = DeclareLaunchArgument(
        'headless',
        default_value='0'
    )

    gz_model_name = LaunchConfiguration('gz_model_name')
    gz_model_name_launch_arg = DeclareLaunchArgument(
        'gz_model_name',
        default_value='x500'
    )

    px4_autostart_id = LaunchConfiguration('px4_autostart_id')
    px4_autostart_id_launch_arg = DeclareLaunchArgument(
        'px4_autostart_id',
        default_value='x500'
    )

    instance_id = LaunchConfiguration('instance_id')
    instance_id_launch_arg = DeclareLaunchArgument(
        'instance_id',
        default_value='0'
    )

    xpos = LaunchConfiguration('xpos')
    xpos_launch_arg = DeclareLaunchArgument(
        'xpos',
        default_value='0.0'
    )

    ypos = LaunchConfiguration('ypos')
    ypos_launch_arg = DeclareLaunchArgument(
        'ypos',
        default_value='0.0'
    )

    namespace = LaunchConfiguration('namespace')
    namespace_launch_arg = DeclareLaunchArgument(
        'namespace',
        default_value=''
    )

    zpos = LaunchConfiguration('zpos')
    zpos_launch_arg = DeclareLaunchArgument(
        'zpos',
        default_value='0.0'
    )

    cmd1_str="cd {} && ".format(PX4_DIR)
    cmd2_str="PX4_SYS_AUTOSTART={} PX4_GZ_MODEL={} PX4_MICRODDS_NS={} PX4_GZ_MODEL_POSE='{},{},{}' ./build/px4_sitl_default/bin/px4 -i {}".format(px4_autostart_id, gz_model_name, namespace, xpos,ypos,zpos, instance_id)
    cmd_str = cmd1_str+cmd2_str
    px4_sim_process = ExecuteProcess(
        cmd=[[
            cmd_str
        ]],
        shell=True
    )

    ld = LaunchDescription()

    ld.add_action(px4_sim_process)

    return ld