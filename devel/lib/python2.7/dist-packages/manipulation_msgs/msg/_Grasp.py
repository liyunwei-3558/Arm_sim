# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from manipulation_msgs/Grasp.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import manipulation_msgs.msg
import sensor_msgs.msg
import std_msgs.msg

class Grasp(genpy.Message):
  _md5sum = "83bd11da422ea1917259ee456c0e315a"
  _type = "manipulation_msgs/Grasp"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# A name for this grasp
string id

# The internal posture of the hand for the pre-grasp
# only positions are used
sensor_msgs/JointState pre_grasp_posture

# The internal posture of the hand for the grasp
# positions and efforts are used
sensor_msgs/JointState grasp_posture

# The position of the end-effector for the grasp 
geometry_msgs/PoseStamped grasp_pose

# The estimated probability of success for this grasp, or some other
# measure of how "good" it is.
float64 grasp_quality

# The approach motion
GripperTranslation approach

# The retreat motion
GripperTranslation retreat

# the maximum contact force to use while grasping (<=0 to disable)
float32 max_contact_force

# an optional list of obstacles that we have semantic information about
# and that can be touched/pushed/moved in the course of grasping
string[] allowed_touch_objects

================================================================================
MSG: sensor_msgs/JointState
# This is a message that holds data to describe the state of a set of torque controlled joints. 
#
# The state of each joint (revolute or prismatic) is defined by:
#  * the position of the joint (rad or m),
#  * the velocity of the joint (rad/s or m/s) and 
#  * the effort that is applied in the joint (Nm or N).
#
# Each joint is uniquely identified by its name
# The header specifies the time at which the joint states were recorded. All the joint states
# in one message have to be recorded at the same time.
#
# This message consists of a multiple arrays, one for each part of the joint state. 
# The goal is to make each of the fields optional. When e.g. your joints have no
# effort associated with them, you can leave the effort array empty. 
#
# All arrays in this message should have the same size, or be empty.
# This is the only way to uniquely associate the joint name with the correct
# states.


Header header

string[] name
float64[] position
float64[] velocity
float64[] effort

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: manipulation_msgs/GripperTranslation
# defines a translation for the gripper, used in pickup or place tasks
# for example for lifting an object off a table or approaching the table for placing

# the direction of the translation
geometry_msgs/Vector3Stamped direction

# the desired translation distance
float32 desired_distance

# the min distance that must be considered feasible before the
# grasp is even attempted
float32 min_distance

================================================================================
MSG: geometry_msgs/Vector3Stamped
# This represents a Vector3 with reference coordinate frame and timestamp
Header header
Vector3 vector

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['id','pre_grasp_posture','grasp_posture','grasp_pose','grasp_quality','approach','retreat','max_contact_force','allowed_touch_objects']
  _slot_types = ['string','sensor_msgs/JointState','sensor_msgs/JointState','geometry_msgs/PoseStamped','float64','manipulation_msgs/GripperTranslation','manipulation_msgs/GripperTranslation','float32','string[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,pre_grasp_posture,grasp_posture,grasp_pose,grasp_quality,approach,retreat,max_contact_force,allowed_touch_objects

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Grasp, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = ''
      if self.pre_grasp_posture is None:
        self.pre_grasp_posture = sensor_msgs.msg.JointState()
      if self.grasp_posture is None:
        self.grasp_posture = sensor_msgs.msg.JointState()
      if self.grasp_pose is None:
        self.grasp_pose = geometry_msgs.msg.PoseStamped()
      if self.grasp_quality is None:
        self.grasp_quality = 0.
      if self.approach is None:
        self.approach = manipulation_msgs.msg.GripperTranslation()
      if self.retreat is None:
        self.retreat = manipulation_msgs.msg.GripperTranslation()
      if self.max_contact_force is None:
        self.max_contact_force = 0.
      if self.allowed_touch_objects is None:
        self.allowed_touch_objects = []
    else:
      self.id = ''
      self.pre_grasp_posture = sensor_msgs.msg.JointState()
      self.grasp_posture = sensor_msgs.msg.JointState()
      self.grasp_pose = geometry_msgs.msg.PoseStamped()
      self.grasp_quality = 0.
      self.approach = manipulation_msgs.msg.GripperTranslation()
      self.retreat = manipulation_msgs.msg.GripperTranslation()
      self.max_contact_force = 0.
      self.allowed_touch_objects = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.pre_grasp_posture.header.seq, _x.pre_grasp_posture.header.stamp.secs, _x.pre_grasp_posture.header.stamp.nsecs))
      _x = self.pre_grasp_posture.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.pre_grasp_posture.name)
      buff.write(_struct_I.pack(length))
      for val1 in self.pre_grasp_posture.name:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.pre_grasp_posture.position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.pre_grasp_posture.position))
      length = len(self.pre_grasp_posture.velocity)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.pre_grasp_posture.velocity))
      length = len(self.pre_grasp_posture.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.pre_grasp_posture.effort))
      _x = self
      buff.write(_get_struct_3I().pack(_x.grasp_posture.header.seq, _x.grasp_posture.header.stamp.secs, _x.grasp_posture.header.stamp.nsecs))
      _x = self.grasp_posture.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.grasp_posture.name)
      buff.write(_struct_I.pack(length))
      for val1 in self.grasp_posture.name:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.grasp_posture.position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.grasp_posture.position))
      length = len(self.grasp_posture.velocity)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.grasp_posture.velocity))
      length = len(self.grasp_posture.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.grasp_posture.effort))
      _x = self
      buff.write(_get_struct_3I().pack(_x.grasp_pose.header.seq, _x.grasp_pose.header.stamp.secs, _x.grasp_pose.header.stamp.nsecs))
      _x = self.grasp_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_8d3I().pack(_x.grasp_pose.pose.position.x, _x.grasp_pose.pose.position.y, _x.grasp_pose.pose.position.z, _x.grasp_pose.pose.orientation.x, _x.grasp_pose.pose.orientation.y, _x.grasp_pose.pose.orientation.z, _x.grasp_pose.pose.orientation.w, _x.grasp_quality, _x.approach.direction.header.seq, _x.approach.direction.header.stamp.secs, _x.approach.direction.header.stamp.nsecs))
      _x = self.approach.direction.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3d2f3I().pack(_x.approach.direction.vector.x, _x.approach.direction.vector.y, _x.approach.direction.vector.z, _x.approach.desired_distance, _x.approach.min_distance, _x.retreat.direction.header.seq, _x.retreat.direction.header.stamp.secs, _x.retreat.direction.header.stamp.nsecs))
      _x = self.retreat.direction.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3d3f().pack(_x.retreat.direction.vector.x, _x.retreat.direction.vector.y, _x.retreat.direction.vector.z, _x.retreat.desired_distance, _x.retreat.min_distance, _x.max_contact_force))
      length = len(self.allowed_touch_objects)
      buff.write(_struct_I.pack(length))
      for val1 in self.allowed_touch_objects:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.pre_grasp_posture is None:
        self.pre_grasp_posture = sensor_msgs.msg.JointState()
      if self.grasp_posture is None:
        self.grasp_posture = sensor_msgs.msg.JointState()
      if self.grasp_pose is None:
        self.grasp_pose = geometry_msgs.msg.PoseStamped()
      if self.approach is None:
        self.approach = manipulation_msgs.msg.GripperTranslation()
      if self.retreat is None:
        self.retreat = manipulation_msgs.msg.GripperTranslation()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.pre_grasp_posture.header.seq, _x.pre_grasp_posture.header.stamp.secs, _x.pre_grasp_posture.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pre_grasp_posture.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.pre_grasp_posture.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pre_grasp_posture.name = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.pre_grasp_posture.name.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.pre_grasp_posture.position = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.pre_grasp_posture.velocity = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.pre_grasp_posture.effort = s.unpack(str[start:end])
      _x = self
      start = end
      end += 12
      (_x.grasp_posture.header.seq, _x.grasp_posture.header.stamp.secs, _x.grasp_posture.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.grasp_posture.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.grasp_posture.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grasp_posture.name = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.grasp_posture.name.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.grasp_posture.position = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.grasp_posture.velocity = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.grasp_posture.effort = s.unpack(str[start:end])
      _x = self
      start = end
      end += 12
      (_x.grasp_pose.header.seq, _x.grasp_pose.header.stamp.secs, _x.grasp_pose.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.grasp_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.grasp_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 76
      (_x.grasp_pose.pose.position.x, _x.grasp_pose.pose.position.y, _x.grasp_pose.pose.position.z, _x.grasp_pose.pose.orientation.x, _x.grasp_pose.pose.orientation.y, _x.grasp_pose.pose.orientation.z, _x.grasp_pose.pose.orientation.w, _x.grasp_quality, _x.approach.direction.header.seq, _x.approach.direction.header.stamp.secs, _x.approach.direction.header.stamp.nsecs,) = _get_struct_8d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.approach.direction.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.approach.direction.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 44
      (_x.approach.direction.vector.x, _x.approach.direction.vector.y, _x.approach.direction.vector.z, _x.approach.desired_distance, _x.approach.min_distance, _x.retreat.direction.header.seq, _x.retreat.direction.header.stamp.secs, _x.retreat.direction.header.stamp.nsecs,) = _get_struct_3d2f3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.retreat.direction.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.retreat.direction.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 36
      (_x.retreat.direction.vector.x, _x.retreat.direction.vector.y, _x.retreat.direction.vector.z, _x.retreat.desired_distance, _x.retreat.min_distance, _x.max_contact_force,) = _get_struct_3d3f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.allowed_touch_objects = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.allowed_touch_objects.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.pre_grasp_posture.header.seq, _x.pre_grasp_posture.header.stamp.secs, _x.pre_grasp_posture.header.stamp.nsecs))
      _x = self.pre_grasp_posture.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.pre_grasp_posture.name)
      buff.write(_struct_I.pack(length))
      for val1 in self.pre_grasp_posture.name:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.pre_grasp_posture.position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.pre_grasp_posture.position.tostring())
      length = len(self.pre_grasp_posture.velocity)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.pre_grasp_posture.velocity.tostring())
      length = len(self.pre_grasp_posture.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.pre_grasp_posture.effort.tostring())
      _x = self
      buff.write(_get_struct_3I().pack(_x.grasp_posture.header.seq, _x.grasp_posture.header.stamp.secs, _x.grasp_posture.header.stamp.nsecs))
      _x = self.grasp_posture.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.grasp_posture.name)
      buff.write(_struct_I.pack(length))
      for val1 in self.grasp_posture.name:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.grasp_posture.position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.grasp_posture.position.tostring())
      length = len(self.grasp_posture.velocity)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.grasp_posture.velocity.tostring())
      length = len(self.grasp_posture.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.grasp_posture.effort.tostring())
      _x = self
      buff.write(_get_struct_3I().pack(_x.grasp_pose.header.seq, _x.grasp_pose.header.stamp.secs, _x.grasp_pose.header.stamp.nsecs))
      _x = self.grasp_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_8d3I().pack(_x.grasp_pose.pose.position.x, _x.grasp_pose.pose.position.y, _x.grasp_pose.pose.position.z, _x.grasp_pose.pose.orientation.x, _x.grasp_pose.pose.orientation.y, _x.grasp_pose.pose.orientation.z, _x.grasp_pose.pose.orientation.w, _x.grasp_quality, _x.approach.direction.header.seq, _x.approach.direction.header.stamp.secs, _x.approach.direction.header.stamp.nsecs))
      _x = self.approach.direction.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3d2f3I().pack(_x.approach.direction.vector.x, _x.approach.direction.vector.y, _x.approach.direction.vector.z, _x.approach.desired_distance, _x.approach.min_distance, _x.retreat.direction.header.seq, _x.retreat.direction.header.stamp.secs, _x.retreat.direction.header.stamp.nsecs))
      _x = self.retreat.direction.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3d3f().pack(_x.retreat.direction.vector.x, _x.retreat.direction.vector.y, _x.retreat.direction.vector.z, _x.retreat.desired_distance, _x.retreat.min_distance, _x.max_contact_force))
      length = len(self.allowed_touch_objects)
      buff.write(_struct_I.pack(length))
      for val1 in self.allowed_touch_objects:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.pre_grasp_posture is None:
        self.pre_grasp_posture = sensor_msgs.msg.JointState()
      if self.grasp_posture is None:
        self.grasp_posture = sensor_msgs.msg.JointState()
      if self.grasp_pose is None:
        self.grasp_pose = geometry_msgs.msg.PoseStamped()
      if self.approach is None:
        self.approach = manipulation_msgs.msg.GripperTranslation()
      if self.retreat is None:
        self.retreat = manipulation_msgs.msg.GripperTranslation()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.pre_grasp_posture.header.seq, _x.pre_grasp_posture.header.stamp.secs, _x.pre_grasp_posture.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pre_grasp_posture.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.pre_grasp_posture.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pre_grasp_posture.name = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.pre_grasp_posture.name.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.pre_grasp_posture.position = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.pre_grasp_posture.velocity = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.pre_grasp_posture.effort = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 12
      (_x.grasp_posture.header.seq, _x.grasp_posture.header.stamp.secs, _x.grasp_posture.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.grasp_posture.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.grasp_posture.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grasp_posture.name = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.grasp_posture.name.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.grasp_posture.position = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.grasp_posture.velocity = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.grasp_posture.effort = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 12
      (_x.grasp_pose.header.seq, _x.grasp_pose.header.stamp.secs, _x.grasp_pose.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.grasp_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.grasp_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 76
      (_x.grasp_pose.pose.position.x, _x.grasp_pose.pose.position.y, _x.grasp_pose.pose.position.z, _x.grasp_pose.pose.orientation.x, _x.grasp_pose.pose.orientation.y, _x.grasp_pose.pose.orientation.z, _x.grasp_pose.pose.orientation.w, _x.grasp_quality, _x.approach.direction.header.seq, _x.approach.direction.header.stamp.secs, _x.approach.direction.header.stamp.nsecs,) = _get_struct_8d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.approach.direction.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.approach.direction.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 44
      (_x.approach.direction.vector.x, _x.approach.direction.vector.y, _x.approach.direction.vector.z, _x.approach.desired_distance, _x.approach.min_distance, _x.retreat.direction.header.seq, _x.retreat.direction.header.stamp.secs, _x.retreat.direction.header.stamp.nsecs,) = _get_struct_3d2f3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.retreat.direction.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.retreat.direction.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 36
      (_x.retreat.direction.vector.x, _x.retreat.direction.vector.y, _x.retreat.direction.vector.z, _x.retreat.desired_distance, _x.retreat.min_distance, _x.max_contact_force,) = _get_struct_3d3f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.allowed_touch_objects = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.allowed_touch_objects.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d2f3I = None
def _get_struct_3d2f3I():
    global _struct_3d2f3I
    if _struct_3d2f3I is None:
        _struct_3d2f3I = struct.Struct("<3d2f3I")
    return _struct_3d2f3I
_struct_3d3f = None
def _get_struct_3d3f():
    global _struct_3d3f
    if _struct_3d3f is None:
        _struct_3d3f = struct.Struct("<3d3f")
    return _struct_3d3f
_struct_8d3I = None
def _get_struct_8d3I():
    global _struct_8d3I
    if _struct_8d3I is None:
        _struct_8d3I = struct.Struct("<8d3I")
    return _struct_8d3I
