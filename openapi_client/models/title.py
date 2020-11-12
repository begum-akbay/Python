# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.14.0.20201015.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Title(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'color': 'str'
    }

    attribute_map = {
        'color': 'color'
    }

    def __init__(self, color=None):  # noqa: E501
        """Title - a model defined in OpenAPI"""  # noqa: E501

        self._color = None
        self.discriminator = None

        if color is not None:
            self.color = color

    @property
    def color(self):
        """Gets the color of this Title.  # noqa: E501

        Hexadecimal color value.  # noqa: E501

        :return: The color of this Title.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Title.

        Hexadecimal color value.  # noqa: E501

        :param color: The color of this Title.  # noqa: E501
        :type: str
        """
        if color is not None and not re.search(r'(^(0[xX]){1}[A-Fa-f0-9]+$)|(^#[A-Fa-f0-9]{6}$)', color):  # noqa: E501
            raise ValueError(r"Invalid value for `color`, must be a follow pattern or equal to `/(^(0[xX]){1}[A-Fa-f0-9]+$)|(^#[A-Fa-f0-9]{6}$)/`")  # noqa: E501

        self._color = color

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Title):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
