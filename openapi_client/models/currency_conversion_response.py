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


class CurrencyConversionResponse(object):
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
        'dcc_applied': 'bool',
        'exchange_rate_details': 'ExchangeRateDetails'
    }

    attribute_map = {
        'dcc_applied': 'dccApplied',
        'exchange_rate_details': 'exchangeRateDetails'
    }

    def __init__(self, dcc_applied=None, exchange_rate_details=None):  # noqa: E501
        """CurrencyConversionResponse - a model defined in OpenAPI"""  # noqa: E501

        self._dcc_applied = None
        self._exchange_rate_details = None
        self.discriminator = None

        if dcc_applied is not None:
            self.dcc_applied = dcc_applied
        if exchange_rate_details is not None:
            self.exchange_rate_details = exchange_rate_details

    @property
    def dcc_applied(self):
        """Gets the dcc_applied of this CurrencyConversionResponse.  # noqa: E501

        Dynamic Currency Conversion Applied.  # noqa: E501

        :return: The dcc_applied of this CurrencyConversionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._dcc_applied

    @dcc_applied.setter
    def dcc_applied(self, dcc_applied):
        """Sets the dcc_applied of this CurrencyConversionResponse.

        Dynamic Currency Conversion Applied.  # noqa: E501

        :param dcc_applied: The dcc_applied of this CurrencyConversionResponse.  # noqa: E501
        :type: bool
        """

        self._dcc_applied = dcc_applied

    @property
    def exchange_rate_details(self):
        """Gets the exchange_rate_details of this CurrencyConversionResponse.  # noqa: E501


        :return: The exchange_rate_details of this CurrencyConversionResponse.  # noqa: E501
        :rtype: ExchangeRateDetails
        """
        return self._exchange_rate_details

    @exchange_rate_details.setter
    def exchange_rate_details(self, exchange_rate_details):
        """Sets the exchange_rate_details of this CurrencyConversionResponse.


        :param exchange_rate_details: The exchange_rate_details of this CurrencyConversionResponse.  # noqa: E501
        :type: ExchangeRateDetails
        """

        self._exchange_rate_details = exchange_rate_details

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
        if not isinstance(other, CurrencyConversionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
