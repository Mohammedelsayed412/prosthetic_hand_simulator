# Creating a sensor node as a publisher

## USing Distorted_Camera Sensor

### Creating camera model in Gazebo 

* Create a model directory 
  
  `$ mkdir -p ~/.gazebo/models/distorted_camera`

* Create a model config file
  
  `$ gedit ~/.gazebo/models/distorted_camera/Camera_model.config ` 

* Create a model sdf file
  
  `$ gedit ~/.gazebo/models/distorted_camera/Camer_model.sdf`

You can create the config file and sdf file manually or from the terminal by `sudo nano file_name.sdf`.

* Start Gazebo
  
  `$ gazebo`

* Insert the distorted camera model into the scene 
  
   * Select **insert** from the left bar in gazebo 
   * Select **Distorted Camera**

* Show the camera image 

   * Drop any obj in front of the camera FOV
   * Press **Ctrl-T** 
   * from "gazebo.msgs.ImageStamped" the topic name will be shown 
   * Click on the topic name then click **"Ok"** you will see the camera image data.

### Breaking the code down (Camera_model.sdf)

The link tag contains 4 main tags (interia, collision, visual, sensor)

**Interia**

```xml
      <inertial>
        <mass>0.1</mass>
        <inertia>
          <ixx>0.000166667</ixx>
          <iyy>0.000166667</iyy>
          <izz>0.000166667</izz>
        </inertia>
      </inertial>

```

The interia element describes the mass and the rotational inertia matrix, you can change these values as your design need.

**Collision**

```xml
<collision name="collision">
        <geometry>
          <box>
            <size>0.1 0.1 0.1</size>
          </box>
        </geometry>
      </collision>
```

The collision element encapsulates a geometry which is used for collision checking. Here, it is a simple box and it can be any other shape.

**Visual**

```xml
<visual name="visual">
        <geometry>
          <box>
            <size>0.1 0.1 0.1</size>
          </box>
        </geometry>
      </visual>
```

The visual tag descride the visual elements which describe the shape of the model.

**Sensor**

```xml
<sensor name="camera" type="camera">
        <camera>
          <horizontal_fov>1.047</horizontal_fov>
          <image>
            <width>320</width>
            <height>240</height>
          </image>
          <clip>
            <near>0.1</near>
            <far>100</far>
          </clip>
          <distortion>
            <k1>-0.25</k1>
            <k2>0.12</k2>
            <k3>0.0</k3>
            <p1>-0.00028</p1>
            <p2>-0.00005</p2>
            <center>0.5 0.5</center>
          </distortion>
        </camera>
        <plugin name="camera_controller" filename="libgazebo_ros_camera.so">>
          <imageTopicName>camera_img</imageTopicName>
          <cameraInfoTopicName>camera_info</cameraInfoTopicName>
          <always_on>1</always_on>
          <update_rate>30</update_rate>
          <visualize>true</visualize>
          </plugin>
      </sensor>
```
Here, we describe the specifications of the distorted_camera sensor and it differs from sensor to another aslo, you can change the values of these coefficients as you desire.
The distored camera has 5 distortion coefficient k1, k2, k3, p1, p2. The coeffs k describe the radial components and the coeffs p describe the tangential component,to change the distortion of the image you can change these values.
The camera ROS plugin provides the ROS interface for simulating cameras,The ROS camera plugin is `libgazebo_ros_camera.so`. Each sensor has each own plugin.

### Connecting Gazebo with ROS

* install gazebo_ros_pkgs
  
`$ sudo apt-get install ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control`

* Launch empty world on Gazebo from ros
  
  `$ roslaunch gazebo_ros empty_world.launch`

* Spawn the model in the simulation 
  
  `$ rosrun gazebo_ros spawn_model -file <file_path> -sdf -model <model_name>`

  now the distorted camera sensor appears in the simulation. 
  **To check that everything is working well**

  `$ sudo apt-get install ros-melodic-rqt` 
  `$ sudo apt-get install ros-meodic-rqt-common-plugins`
  `$ rosrun rqt_graph rqt_graph`

* Show the published data on your topic
  
  `$ rostopic echo [topic]` replace [topic] with the topic name
 




  
