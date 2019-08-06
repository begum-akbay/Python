# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.6.0.20190507.002
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BillingAddressPhone(object):
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
        'type': 'str',
        'number': 'str'
    }

    attribute_map = {
        'type': 'type',
        'number': 'number'
    }

    def __init__(self, type=None, number=None):  # noqa: E501
        """BillingAddressPhone - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._number = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if number is not None:
            self.number = number

    @property
    def type(self):
        """Gets the type of this BillingAddressPhone.  # noqa: E501

        Type of phone.  # noqa: E501

        :return: The type of this BillingAddressPhone.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BillingAddressPhone.

        Type of phone.  # noqa: E501

        :param type: The type of this BillingAddressPhone.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def number(self):
        """Gets the number of this BillingAddressPhone.  # noqa: E501

        Free-form phone number.  # noqa: E501

        :return: The number of this BillingAddressPhone.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this BillingAddressPhone.

        Free-form phone number.  # noqa: E501

        :param number: The number of this BillingAddressPhone.  # noqa: E501
        :type: str
        """

        self._number = number

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
        if not isinstance(other, BillingAddressPhone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
