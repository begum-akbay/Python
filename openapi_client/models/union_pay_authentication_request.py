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


class UnionPayAuthenticationRequest(object):
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
        'authentication_type': 'str',
        'sms_phone_number': 'str'
    }

    attribute_map = {
        'authentication_type': 'authenticationType',
        'sms_phone_number': 'smsPhoneNumber'
    }

    def __init__(self, authentication_type=None, sms_phone_number=None):  # noqa: E501
        """UnionPayAuthenticationRequest - a model defined in OpenAPI"""  # noqa: E501

        self._authentication_type = None
        self._sms_phone_number = None
        self.discriminator = None

        if authentication_type is not None:
            self.authentication_type = authentication_type
        self.sms_phone_number = sms_phone_number

    @property
    def authentication_type(self):
        """Gets the authentication_type of this UnionPayAuthenticationRequest.  # noqa: E501

        Indicates what kind of authentication scheme the merchant wants to use on the card.  # noqa: E501

        :return: The authentication_type of this UnionPayAuthenticationRequest.  # noqa: E501
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this UnionPayAuthenticationRequest.

        Indicates what kind of authentication scheme the merchant wants to use on the card.  # noqa: E501

        :param authentication_type: The authentication_type of this UnionPayAuthenticationRequest.  # noqa: E501
        :type: str
        """

        self._authentication_type = authentication_type

    @property
    def sms_phone_number(self):
        """Gets the sms_phone_number of this UnionPayAuthenticationRequest.  # noqa: E501

        Mobile number for SMS verification.  # noqa: E501

        :return: The sms_phone_number of this UnionPayAuthenticationRequest.  # noqa: E501
        :rtype: str
        """
        return self._sms_phone_number

    @sms_phone_number.setter
    def sms_phone_number(self, sms_phone_number):
        """Sets the sms_phone_number of this UnionPayAuthenticationRequest.

        Mobile number for SMS verification.  # noqa: E501

        :param sms_phone_number: The sms_phone_number of this UnionPayAuthenticationRequest.  # noqa: E501
        :type: str
        """
        if sms_phone_number is None:
            raise ValueError("Invalid value for `sms_phone_number`, must not be `None`")  # noqa: E501
        if sms_phone_number is not None and len(sms_phone_number) < 7:
            raise ValueError("Invalid value for `sms_phone_number`, length must be greater than or equal to `7`")  # noqa: E501
        if sms_phone_number is not None and not re.search(r'^(?!\s*$).+', sms_phone_number):  # noqa: E501
            raise ValueError(r"Invalid value for `sms_phone_number`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._sms_phone_number = sms_phone_number

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
        if not isinstance(other, UnionPayAuthenticationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
