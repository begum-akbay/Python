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


class ReceiptRequestInfo(object):
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
        'locale': 'str',
        'linewidth': 'int'
    }

    attribute_map = {
        'type': 'type',
        'locale': 'locale',
        'linewidth': 'linewidth'
    }

    def __init__(self, type=None, locale=None, linewidth=32):  # noqa: E501
        """ReceiptRequestInfo - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._locale = None
        self._linewidth = None
        self.discriminator = None

        self.type = type
        if locale is not None:
            self.locale = locale
        if linewidth is not None:
            self.linewidth = linewidth

    @property
    def type(self):
        """Gets the type of this ReceiptRequestInfo.  # noqa: E501

        Defines the consumer of the receipt (e.g. cardholder, merchant).  # noqa: E501

        :return: The type of this ReceiptRequestInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReceiptRequestInfo.

        Defines the consumer of the receipt (e.g. cardholder, merchant).  # noqa: E501

        :param type: The type of this ReceiptRequestInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["cardholder", "merchant"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def locale(self):
        """Gets the locale of this ReceiptRequestInfo.  # noqa: E501

        The locale of the receipt. The format has to be a well-formed BCP 47 language tag.  # noqa: E501

        :return: The locale of this ReceiptRequestInfo.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this ReceiptRequestInfo.

        The locale of the receipt. The format has to be a well-formed BCP 47 language tag.  # noqa: E501

        :param locale: The locale of this ReceiptRequestInfo.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def linewidth(self):
        """Gets the linewidth of this ReceiptRequestInfo.  # noqa: E501

        The line width of the receipt. Default will be 32 characters.  # noqa: E501

        :return: The linewidth of this ReceiptRequestInfo.  # noqa: E501
        :rtype: int
        """
        return self._linewidth

    @linewidth.setter
    def linewidth(self, linewidth):
        """Sets the linewidth of this ReceiptRequestInfo.

        The line width of the receipt. Default will be 32 characters.  # noqa: E501

        :param linewidth: The linewidth of this ReceiptRequestInfo.  # noqa: E501
        :type: int
        """

        self._linewidth = linewidth

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
        if not isinstance(other, ReceiptRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
