# Arm_sim 
cd Arm_sim
source ./devel/setup.bash
roslaunch mainarm_moveit_config demo.launch

#New Terminal
source ./devel/setup.bash
rosrun mainarm_moveit_config mainarm_planning_node

