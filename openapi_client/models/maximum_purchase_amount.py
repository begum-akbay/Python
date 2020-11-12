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


class MaximumPurchaseAmount(object):
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
        'currency': 'str',
        'max_amount': 'str'
    }

    attribute_map = {
        'currency': 'currency',
        'max_amount': 'maxAmount'
    }

    def __init__(self, currency=None, max_amount=None):  # noqa: E501
        """MaximumPurchaseAmount - a model defined in OpenAPI"""  # noqa: E501

        self._currency = None
        self._max_amount = None
        self.discriminator = None

        self.currency = currency
        self.max_amount = max_amount

    @property
    def currency(self):
        """Gets the currency of this MaximumPurchaseAmount.  # noqa: E501

        Currency in alphabetic ISO 4217 currency code format.  # noqa: E501

        :return: The currency of this MaximumPurchaseAmount.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this MaximumPurchaseAmount.

        Currency in alphabetic ISO 4217 currency code format.  # noqa: E501

        :param currency: The currency of this MaximumPurchaseAmount.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def max_amount(self):
        """Gets the max_amount of this MaximumPurchaseAmount.  # noqa: E501

        Maximum purchase amount limit.  # noqa: E501

        :return: The max_amount of this MaximumPurchaseAmount.  # noqa: E501
        :rtype: str
        """
        return self._max_amount

    @max_amount.setter
    def max_amount(self, max_amount):
        """Sets the max_amount of this MaximumPurchaseAmount.

        Maximum purchase amount limit.  # noqa: E501

        :param max_amount: The max_amount of this MaximumPurchaseAmount.  # noqa: E501
        :type: str
        """
        if max_amount is None:
            raise ValueError("Invalid value for `max_amount`, must not be `None`")  # noqa: E501

        self._max_amount = max_amount

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
        if not isinstance(other, MaximumPurchaseAmount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
