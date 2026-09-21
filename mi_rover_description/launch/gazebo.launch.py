import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, AppendEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    pkg_name = 'mi_rover_description'
    pkg_share = get_package_share_directory(pkg_name)

    # 1. EL MAPA PARA GAZEBO: Le decimos dónde están tus archivos STL
    set_env_vars_resources = AppendEnvironmentVariable(
        'GZ_SIM_RESOURCE_PATH',
        os.path.join(pkg_share, '..')
    )

    # 2. Procesar el archivo Xacro maestro
    xacro_file = os.path.join(pkg_share, 'urdf', 'rover_completo.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    robot_description = {'robot_description': robot_description_config.toxml()}

    # 3. Nodo para publicar el estado del robot
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description]
    )

    # 4. Incluir el launch base de Gazebo (Harmonic)
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
        launch_arguments={'gz_args': 'empty.sdf -r'}.items()
    )

    # 5. Nodo para "aparecer" el robot desde 50 cm de altura
    spawn_entity = Node(package='ros_gz_sim', executable='create',
                        arguments=['-topic', 'robot_description',
                                   '-name', 'mi_rover',
                                   '-z', '0.0'], 
                        output='screen')

    return LaunchDescription([
        set_env_vars_resources, # Cargamos el mapa aquí
        node_robot_state_publisher,
        gazebo,
        spawn_entity
    ])
