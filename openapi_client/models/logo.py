# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.10.1.20200226.002
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Logo(object):
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
        'position': 'str',
        'filename': 'str',
        'data': 'str'
    }

    attribute_map = {
        'position': 'position',
        'filename': 'filename',
        'data': 'data'
    }

    def __init__(self, position=None, filename=None, data=None):  # noqa: E501
        """Logo - a model defined in OpenAPI"""  # noqa: E501

        self._position = None
        self._filename = None
        self._data = None
        self.discriminator = None

        self.position = position
        self.filename = filename
        self.data = data

    @property
    def position(self):
        """Gets the position of this Logo.  # noqa: E501

        Define position of logo.  # noqa: E501

        :return: The position of this Logo.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Logo.

        Define position of logo.  # noqa: E501

        :param position: The position of this Logo.  # noqa: E501
        :type: str
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501
        allowed_values = ["TOP", "BOTTOM"]  # noqa: E501
        if position not in allowed_values:
            raise ValueError(
                "Invalid value for `position` ({0}), must be one of {1}"  # noqa: E501
                .format(position, allowed_values)
            )

        self._position = position

    @property
    def filename(self):
        """Gets the filename of this Logo.  # noqa: E501

        The filename of the uploaded logo.  # noqa: E501

        :return: The filename of this Logo.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Logo.

        The filename of the uploaded logo.  # noqa: E501

        :param filename: The filename of this Logo.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def data(self):
        """Gets the data of this Logo.  # noqa: E501

        Base64 image data.  # noqa: E501

        :return: The data of this Logo.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Logo.

        Base64 image data.  # noqa: E501

        :param data: The data of this Logo.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if not isinstance(other, Logo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
