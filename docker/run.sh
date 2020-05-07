docker run -it --rm -p 8080:8080 -p 7681:7681 -v $(pwd)/..:/data --name ros_gazebo_web  cairoceslab/prosthetic_hand_simulator:latest /bin/bash
