# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.1.0.20210122.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AuthenticationResult(object):
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
        'authentication_type': 'str'
    }

    attribute_map = {
        'authentication_type': 'authenticationType'
    }

    discriminator_value_class_map = {
        'Secure3DAuthenticationResult': 'Secure3DAuthenticationResult',
        'Secure3D10AuthenticationResult': 'Secure3D10AuthenticationResult',
        'Secure3D21AuthenticationResult': 'Secure3D21AuthenticationResult'
    }

    def __init__(self, authentication_type=None):  # noqa: E501
        """AuthenticationResult - a model defined in OpenAPI"""  # noqa: E501

        self._authentication_type = None
        self.discriminator = 'authentication_type'

        self.authentication_type = authentication_type

    @property
    def authentication_type(self):
        """Gets the authentication_type of this AuthenticationResult.  # noqa: E501

        Specifies the version of 3DS to be used where authentication was managed outside of the gateway.  # noqa: E501

        :return: The authentication_type of this AuthenticationResult.  # noqa: E501
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this AuthenticationResult.

        Specifies the version of 3DS to be used where authentication was managed outside of the gateway.  # noqa: E501

        :param authentication_type: The authentication_type of this AuthenticationResult.  # noqa: E501
        :type: str
        """
        if authentication_type is None:
            raise ValueError("Invalid value for `authentication_type`, must not be `None`")  # noqa: E501

        self._authentication_type = authentication_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, AuthenticationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
