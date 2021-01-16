// Generated by gencpp from file household_objects_database_msgs/GetModelDescription.msg
// DO NOT EDIT!


#ifndef HOUSEHOLD_OBJECTS_DATABASE_MSGS_MESSAGE_GETMODELDESCRIPTION_H
#define HOUSEHOLD_OBJECTS_DATABASE_MSGS_MESSAGE_GETMODELDESCRIPTION_H

#include <ros/service_traits.h>


#include <household_objects_database_msgs/GetModelDescriptionRequest.h>
#include <household_objects_database_msgs/GetModelDescriptionResponse.h>


namespace household_objects_database_msgs
{

struct GetModelDescription
{

typedef GetModelDescriptionRequest Request;
typedef GetModelDescriptionResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetModelDescription
} // namespace household_objects_database_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::household_objects_database_msgs::GetModelDescription > {
  static const char* value()
  {
    return "1fee77e674730723af04cd39a4e3e0b1";
  }

  static const char* value(const ::household_objects_database_msgs::GetModelDescription&) { return value(); }
};

template<>
struct DataType< ::household_objects_database_msgs::GetModelDescription > {
  static const char* value()
  {
    return "household_objects_database_msgs/GetModelDescription";
  }

  static const char* value(const ::household_objects_database_msgs::GetModelDescription&) { return value(); }
};


// service_traits::MD5Sum< ::household_objects_database_msgs::GetModelDescriptionRequest> should match
// service_traits::MD5Sum< ::household_objects_database_msgs::GetModelDescription >
template<>
struct MD5Sum< ::household_objects_database_msgs::GetModelDescriptionRequest>
{
  static const char* value()
  {
    return MD5Sum< ::household_objects_database_msgs::GetModelDescription >::value();
  }
  static const char* value(const ::household_objects_database_msgs::GetModelDescriptionRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::household_objects_database_msgs::GetModelDescriptionRequest> should match
// service_traits::DataType< ::household_objects_database_msgs::GetModelDescription >
template<>
struct DataType< ::household_objects_database_msgs::GetModelDescriptionRequest>
{
  static const char* value()
  {
    return DataType< ::household_objects_database_msgs::GetModelDescription >::value();
  }
  static const char* value(const ::household_objects_database_msgs::GetModelDescriptionRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::household_objects_database_msgs::GetModelDescriptionResponse> should match
// service_traits::MD5Sum< ::household_objects_database_msgs::GetModelDescription >
template<>
struct MD5Sum< ::household_objects_database_msgs::GetModelDescriptionResponse>
{
  static const char* value()
  {
    return MD5Sum< ::household_objects_database_msgs::GetModelDescription >::value();
  }
  static const char* value(const ::household_objects_database_msgs::GetModelDescriptionResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::household_objects_database_msgs::GetModelDescriptionResponse> should match
// service_traits::DataType< ::household_objects_database_msgs::GetModelDescription >
template<>
struct DataType< ::household_objects_database_msgs::GetModelDescriptionResponse>
{
  static const char* value()
  {
    return DataType< ::household_objects_database_msgs::GetModelDescription >::value();
  }
  static const char* value(const ::household_objects_database_msgs::GetModelDescriptionResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // HOUSEHOLD_OBJECTS_DATABASE_MSGS_MESSAGE_GETMODELDESCRIPTION_H
