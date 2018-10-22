# coding: utf-8

"""
    Payment Gateway API Specification

    Payment Gateway API for payment processing.   # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AirlineAncillaryServiceCategory(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'service_category': 'str'
    }

    attribute_map = {
        'service_category': 'serviceCategory'
    }

    def __init__(self, service_category=None):  # noqa: E501
        """AirlineAncillaryServiceCategory - a model defined in Swagger"""  # noqa: E501

        self._service_category = None
        self.discriminator = None

        if service_category is not None:
            self.service_category = service_category

    @property
    def service_category(self):
        """Gets the service_category of this AirlineAncillaryServiceCategory.  # noqa: E501


        :return: The service_category of this AirlineAncillaryServiceCategory.  # noqa: E501
        :rtype: str
        """
        return self._service_category

    @service_category.setter
    def service_category(self, service_category):
        """Sets the service_category of this AirlineAncillaryServiceCategory.


        :param service_category: The service_category of this AirlineAncillaryServiceCategory.  # noqa: E501
        :type: str
        """
        allowed_values = ["BUNDLED_SERVICE", "BAGGAGE_FEE", "CHANGE_FEE", "CARGO", "CARBON_OFFSET", "FREQUENT_FLYER", "GIFT_CARD", "GROUND_TRANSPORT", "IN_FLIGHT_ENTERTAINMENT", "LOUNGE", "MEDICAL", "MEAL_BEVERAGE", "OTHER", "PASSENGER_ASSIST_FEE", "PETS", "SEAT_FEES", "STANDBY", "SERVICE_FEE", "STORE", "TRAVEL_SERVICE", "UNACCOMPANIED_TRAVEL", "UPGRADES", "WI_FI"]  # noqa: E501
        if service_category not in allowed_values:
            raise ValueError(
                "Invalid value for `service_category` ({0}), must be one of {1}"  # noqa: E501
                .format(service_category, allowed_values)
            )

        self._service_category = service_category

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AirlineAncillaryServiceCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
