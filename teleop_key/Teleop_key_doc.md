#  Creating a controller node that publishes to a topic

* Create a package
  
  `& catkin_create_pkg teleop_key std_msgs rospy`

  * Build the package in catkin workspace
  
    `$ cd ~/catkin_ws`

    `$ catkin_make`

  * Generate setup file to add the workspace to ROS environment

     `$ . ~/catkin_ws/devel/setup.bash` if you forget to type this command you will receive **"package not found"** error after that.

* Write the publisher node

  `$ roscd teleop_key` -> to change the directory to the created package

  * Create scripts folder 

    `$ mkdir scripts`

    `$ cd scripts`

  * Write the publisher code in the scripts folder and make it excutable
    
    `$ chmod +x teleop_key.py` -> you may receive an error **"operant not premitted"**, so try this command instead of the previous command `$ sudo chmod +x teleop_key.py`.

  * Run the code 
  
    `$ rosrun teleop_key teleop_key.py` -> the package name and the script file name. Make sure that `roscore` is running before type this command.

  
 ## Breaking the code down (teleop_key.py)

 * Prerequisites:
  
  * install getch library
  
    `$ pip install getch` you can try this `$ pip install https://pypi.python.org/packages/source/g/getch/getch-1.0-python2.tar.gz` if you receive errors from the previous command.

* Importing the necessary libraries

```python
    #!/usr/bin/python
    import getch
    import rospy
    from std_msgs.msg import String  
```
The first line is neccessary to check that your script is executed as a Python script.

* The core function 

```python
    def keys():
    pub = rospy.Publisher('teleop_key', String, queue_size = 10) 
    rospy.init_node('keypress', anonymous = True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        k = ord(getch.getch())
        dic = {115:"start", 113:"quit"}    
        try:
	        rospy.loginfo(dic[k])
	        pub.publish(dic[k]) 
        except KeyError:
		rospy.loginfo("key not fount !!")
                
if __name__=='__main__':
    try:
        keys()
    except rospy.ROSInterruptException as e:
        rospy.loginfo(e)
```
This function aim to convert the keypress into masseges published into the topic using this function `ord(getch.getch())`. Here, the topic name is "teleop_key" and the type of the published masseges is string.
Using dictionary to store the keys code and the corresponding order you desired `dic = {115:"start", 113:"quit"}`. Note that, key codes are numeric values that correspond to physical keys on the keyboard but do not necessarily correspond to a particular character.
Using try and except to handle some errors such as, if you press key that wasn't store in your dictionary it will print "key not fount !!" massage, and to handle ROS errors using `rospy.ROSInterruptException`.


