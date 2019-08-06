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


class UsePaymentToken(object):
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
        'value': 'str',
        'function': 'CardFunction',
        'security_code': 'str'
    }

    attribute_map = {
        'value': 'value',
        'function': 'function',
        'security_code': 'securityCode'
    }

    def __init__(self, value=None, function=None, security_code=None):  # noqa: E501
        """UsePaymentToken - a model defined in OpenAPI"""  # noqa: E501

        self._value = None
        self._function = None
        self._security_code = None
        self.discriminator = None

        self.value = value
        if function is not None:
            self.function = function
        if security_code is not None:
            self.security_code = security_code

    @property
    def value(self):
        """Gets the value of this UsePaymentToken.  # noqa: E501

        Client-supplied payment token value.  # noqa: E501

        :return: The value of this UsePaymentToken.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UsePaymentToken.

        Client-supplied payment token value.  # noqa: E501

        :param value: The value of this UsePaymentToken.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if value is not None and not re.search(r'^(?!\s*$).+', value):  # noqa: E501
            raise ValueError(r"Invalid value for `value`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._value = value

    @property
    def function(self):
        """Gets the function of this UsePaymentToken.  # noqa: E501


        :return: The function of this UsePaymentToken.  # noqa: E501
        :rtype: CardFunction
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this UsePaymentToken.


        :param function: The function of this UsePaymentToken.  # noqa: E501
        :type: CardFunction
        """

        self._function = function

    @property
    def security_code(self):
        """Gets the security_code of this UsePaymentToken.  # noqa: E501

        Card verification value/number.  # noqa: E501

        :return: The security_code of this UsePaymentToken.  # noqa: E501
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """Sets the security_code of this UsePaymentToken.

        Card verification value/number.  # noqa: E501

        :param security_code: The security_code of this UsePaymentToken.  # noqa: E501
        :type: str
        """
        if security_code is not None and len(security_code) > 4:
            raise ValueError("Invalid value for `security_code`, length must be less than or equal to `4`")  # noqa: E501
        if security_code is not None and len(security_code) < 3:
            raise ValueError("Invalid value for `security_code`, length must be greater than or equal to `3`")  # noqa: E501

        self._security_code = security_code

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
        if not isinstance(other, UsePaymentToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
