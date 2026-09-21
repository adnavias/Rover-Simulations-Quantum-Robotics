===============================================================================
Graficas
------------------------------------------------------------------------------
Terminal Graficas:
ros2 run plotjuggler plotjuggler

===============================================================================
SIMULACION
-------------------------------------------------------------------
Actualizar
cd ~/ros2_ws
source install/setup.bash

-----------------------------------------------------------
Terminal 1:Lanzar el Simulador 3D

ros2 launch mi_rover_description gazebo.launch.py

===============================================================================

Terminal 2:Lanzar el Puente Total (Doble Vía Sincronizada)

ros2 run ros_gz_bridge parameter_bridge \
/world/empty/model/mi_rover/joint_state@sensor_msgs/msg/JointState[gz.msgs.Model \
/model/mi_rover/joint/Joint_1/cmd_force@std_msgs/msg/Float64]gz.msgs.Double \
/model/mi_rover/joint/Joint_2/cmd_force@std_msgs/msg/Float64]gz.msgs.Double \
/model/mi_rover/joint/Joint_3/cmd_force@std_msgs/msg/Float64]gz.msgs.Double \*p
/model/mi_rover/joint/Joint_4/cmd_force@std_msgs/msg/Float64]gz.msgs.Double \
/model/mi_rover/joint/Joint_5/cmd_force@std_msgs/msg/Float64]gz.msgs.Double \
/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist

===================================================================================
CONTROL PYTON 
----------------------------------------------------------------------------------
TERMINAL 3: Despertar el Nodo de Control (Python)

ros2 run control_adrc_rover adrc_node
----------------------------------------------------------------------------------
Compilar codigo 

cd ~/ros2_ws
colcon build --packages-select control_adrc_rover
source install/setup.bash
----------------------------------------------------------------------------------
Abrir Codigo Control

cd ~/ros2_ws/src/control_adrc_rover/control_adrc_rover
nano adrc_node.py

===================================================================================
CONTROL C++
----------------------------------------------------------------------------------
TERMINAL 3: Despertar el Nodo de Control (C++)

ros2 run control_adrc_rover_cpp rover_arm_full_adrc
----------------------------------------------------------------------------------
Compilar codigo 

cd ~/ros2_ws
colcon build --packages-select control_adrc_rover_cpp
source install/setup.bash
----------------------------------------------------------------------------------
Abrir Codigo Control

cd ~/ros2_ws/src/control_adrc_rover_cpp/src
nano rover_arm_full_adrc.cpp
--------------------------------------------------------------------------------
CORRER CODIGO

ros2 topic pub --once /target_joint_states sensor_msgs/msg/JointState "{name: ['Joint_1', 'Joint_2', 'Joint_3', 'Joint_4', 'Joint_5'], position: [0.0, 0.0, 0.0, 0.0, 0.0]}"


=======================================================================
Poses

cd test
python3 rover_commander.py

===================================================================================
CONTROL LLANTAS 
----------------------------------------------------------------------------------
TERMINAL Control Remoto por Teclado (Llantas)

ros2 run teleop_twist_keyboard teleop_twist_keyboard
