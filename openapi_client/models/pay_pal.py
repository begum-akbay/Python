# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    OpenAPI spec version: 6.6.0.20190329.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PayPal(object):
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
        'recipient_email': 'str'
    }

    attribute_map = {
        'recipient_email': 'recipientEmail'
    }

    def __init__(self, recipient_email=None):  # noqa: E501
        """PayPal - a model defined in OpenAPI"""  # noqa: E501

        self._recipient_email = None
        self.discriminator = None

        self.recipient_email = recipient_email

    @property
    def recipient_email(self):
        """Gets the recipient_email of this PayPal.  # noqa: E501

        Email address of the recipient.  # noqa: E501

        :return: The recipient_email of this PayPal.  # noqa: E501
        :rtype: str
        """
        return self._recipient_email

    @recipient_email.setter
    def recipient_email(self, recipient_email):
        """Sets the recipient_email of this PayPal.

        Email address of the recipient.  # noqa: E501

        :param recipient_email: The recipient_email of this PayPal.  # noqa: E501
        :type: str
        """
        if recipient_email is None:
            raise ValueError("Invalid value for `recipient_email`, must not be `None`")  # noqa: E501
        if recipient_email is not None and len(recipient_email) > 254:
            raise ValueError("Invalid value for `recipient_email`, length must be less than or equal to `254`")  # noqa: E501

        self._recipient_email = recipient_email

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
        if not isinstance(other, PayPal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
