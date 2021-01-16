// 包含miveit的API头文件
#include <moveit/move_group_interface/move_group_interface.h>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "moveit_custom_demo");
  ros::NodeHandle node_handle; 
  ros::AsyncSpinner spinner(1);
  spinner.start();

  moveit::planning_interface::MoveGroupInterface group("arm");
  ROS_INFO("Reference frame: %s", group.getPlanningFrame().c_str());
  // 设置机器人终端的目标位置
  geometry_msgs::Pose target_pose1;
  // target_pose1.orientation.w = -0.57057;
  // target_pose1.orientation.x= 0.39171;
  // target_pose1.orientation.y = 0.24965;
  // target_pose1.orientation.z = 0.67726;

  target_pose1.position.x = 0.38;
  target_pose1.position.y = -0.0964;
  target_pose1.position.z = 0.1860;
group.setGoalPositionTolerance(0.01);
       group.setGoalOrientationTolerance(0.01);
    group.setPoseTarget(target_pose1);
  //进行运动规划，计算机器人移动到目标的运动轨迹，此时只是计算出轨迹，并不会控制机械臂运动
  moveit::planning_interface::MoveGroupInterface::Plan my_plan;
  moveit::planning_interface::MoveItErrorCode success = group.plan(my_plan);

  ROS_INFO("Visualizing plan 1 (pose goal) %s",success?"":"FAILED");   
  sleep(1.0);
  //让机械臂按照规划的轨迹开始运动。
  if(success)
      group.execute(my_plan);

  //group.move();
  ros::shutdown(); 
  return 0;
}
