# Create a sensor node as a publisher

Here, we will use a distorted_camera model as a sensor node.

## 1) Create Camera node

* Create a model directory 
  
  `$ mkdir -p ~/.gazebo/models/distorted_camera`

* Create a model config file
  
  `$ gedit ~/.gazebo/models/distorted_camera/Camera_model.config ` 

* Create a model sdf file
  
  `$ gedit ~/.gazebo/models/distorted_camera/Camer_model.sdf`

You can Create the config file and sdf file manually or from terminal too.

* Start Gazebo
  
  `$ gazebo`

* Insert the distorted camera model into the scene 
  
   * select insert from gazebo left bar 
   * choice Distorted Camera

* Show the camera image 

   * Drop obj on the camera FOV
   * Press Ctrl-T 
   * from "gazebo.msgs.ImageStamped" the topic name will be shown 
   * Click on the topic name then click "Ok" you will see the camera image data.

## Break the code down (Camera_model.sdf)

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

the interia element describes the mass and the rotational interia matrix we can change these value as our design need.

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

the collision element encapsulates a geometry which is used for collsion checking. Here, it is a simple box and it can be changed as we desire.

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

the visual element descride the shape of the element and it is an optional tag.

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
here, we descripte the specs of the used sensor and it will be different from sensor to other aslo, we can change the values of these coefficients as we desire.
the distored camera has 5 distortion coefficient k1, k2, k3, p1, p2. The coeffs k describe the radial components and the coeffs p describe the tangential component,to change the distortion we can change these values.

## 2) Using the camera node as a publisher