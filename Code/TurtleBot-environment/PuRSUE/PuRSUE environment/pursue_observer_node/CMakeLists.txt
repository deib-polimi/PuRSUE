cmake_minimum_required(VERSION 2.8.3)
project(pursue_observer_node)

find_package(catkin REQUIRED 
					COMPONENTS 
					rospy 
					roscpp
					actionlib_msgs 
					actionlib
					#transitions
					)

find_package(catkin REQUIRED)


catkin_package(	 # REQUIRED COMPONENTS transitions 
	)

include_directories(${catkin_INCLUDE_DIRS} )

add_message_files()


catkin_python_setup()
