#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <moveit_msgs/AttachedCollisionObject.h>
#include <moveit_msgs/CollisionObject.h>
#include <std_msgs/String.h>
#include <string.h>
#define Cy_h  0.17
#define Cy_r  0.025
#define Cy_z  0.08
#define Interval_X  0.35
#define Interval_Y 0.1

std::string GetName(int a)
{
    std::string s = "arm_cylinder";
    s+=(char)(a-'0');
    return s;
}

moveit_msgs::CollisionObject Construct_Cy(int x,int y,int ind)
{
    moveit_msgs::CollisionObject cylinder;
    cylinder.header.frame_id = "base_link";
    cylinder.id = GetName(ind) ;
    std::cout<<cylinder.id<<std::endl;
    //shape
    shape_msgs::SolidPrimitive prim;
    prim.type = prim.CYLINDER;
    prim.dimensions.resize(3);
    prim.dimensions[0] = Cy_h;
    prim.dimensions[1] = Cy_r;

     geometry_msgs::Pose pose;
    pose.orientation.w = 1.0;
    pose.position.y =  Interval_X*x;
    pose.position.x = Interval_Y*y;
    pose.position.z =  Cy_z;
    cylinder.primitives.push_back(prim);
    cylinder.primitive_poses.push_back(pose);
    cylinder.operation = cylinder.ADD;

    return cylinder;
}

void BuildScene()
{
    moveit::planning_interface::PlanningSceneInterface current_scene;
    sleep(5.0);
    std::vector<moveit_msgs::CollisionObject> collision_objects;
    int index = 0;
    for(int i = -1;i<=1;i++)
    {
        if(!i) continue;
        for(int j = -2;j<=2;j++)
        {
            ROS_INFO("%d",index);
            std::cout<<i<<' '<<j<<std::endl;
           moveit_msgs::CollisionObject nowcy =  Construct_Cy(i,j,++index);
           collision_objects.push_back(nowcy);
        }
    }
    current_scene.addCollisionObjects(collision_objects);
  sleep(5.0);
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "mainarm_planning");
    ros::NodeHandle nh;
    ros::AsyncSpinner spin(1);
    spin.start();

    BuildScene();
    //PlanExcTrj();

    ROS_INFO("Completed.\n");
    ros::shutdown();

    return 0;
}