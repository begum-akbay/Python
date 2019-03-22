# coding: utf-8

"""
    Payment Gateway API Specification.

    Payment Gateway API for payment processing. Version 6.4.0.20181018.001   # noqa: E501

    OpenAPI spec version: 6.4.0.20181018.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ExchangeRateRequest(object):
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
        'store_id': 'str',
        'bin': 'str',
        'base_amount': 'float',
        'foreign_currency': 'str'
    }

    attribute_map = {
        'type': 'type',
        'store_id': 'storeId',
        'bin': 'bin',
        'base_amount': 'baseAmount',
        'foreign_currency': 'foreignCurrency'
    }

    def __init__(self, type=None, store_id=None, bin=None, base_amount=None, foreign_currency=None):  # noqa: E501
        """ExchangeRateRequest - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._store_id = None
        self._bin = None
        self._base_amount = None
        self._foreign_currency = None
        self.discriminator = None

        self.type = type
        if store_id is not None:
            self.store_id = store_id
        if bin is not None:
            self.bin = bin
        self.base_amount = base_amount
        if foreign_currency is not None:
            self.foreign_currency = foreign_currency

    @property
    def type(self):
        """Gets the type of this ExchangeRateRequest.  # noqa: E501

        Type of exchange rate inquiry. Valid values are 'DCC' and 'DYNAMIC_PRICING'.  # noqa: E501

        :return: The type of this ExchangeRateRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExchangeRateRequest.

        Type of exchange rate inquiry. Valid values are 'DCC' and 'DYNAMIC_PRICING'.  # noqa: E501

        :param type: The type of this ExchangeRateRequest.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["DCC", "DYNAMIC_PRICING"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def store_id(self):
        """Gets the store_id of this ExchangeRateRequest.  # noqa: E501

        An optional Outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :return: The store_id of this ExchangeRateRequest.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this ExchangeRateRequest.

        An optional Outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :param store_id: The store_id of this ExchangeRateRequest.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def bin(self):
        """Gets the bin of this ExchangeRateRequest.  # noqa: E501

        A bank identification number (BIN) of the card to be used for DCC.  # noqa: E501

        :return: The bin of this ExchangeRateRequest.  # noqa: E501
        :rtype: str
        """
        return self._bin

    @bin.setter
    def bin(self, bin):
        """Sets the bin of this ExchangeRateRequest.

        A bank identification number (BIN) of the card to be used for DCC.  # noqa: E501

        :param bin: The bin of this ExchangeRateRequest.  # noqa: E501
        :type: str
        """
        if bin is not None and len(bin) > 6:
            raise ValueError("Invalid value for `bin`, length must be less than or equal to `6`")  # noqa: E501
        if bin is not None and not re.search(r'[0-9]{6}', bin):  # noqa: E501
            raise ValueError(r"Invalid value for `bin`, must be a follow pattern or equal to `/[0-9]{6}/`")  # noqa: E501

        self._bin = bin

    @property
    def base_amount(self):
        """Gets the base_amount of this ExchangeRateRequest.  # noqa: E501

        The original amount of the merchant currency for calculation.  # noqa: E501

        :return: The base_amount of this ExchangeRateRequest.  # noqa: E501
        :rtype: float
        """
        return self._base_amount

    @base_amount.setter
    def base_amount(self, base_amount):
        """Sets the base_amount of this ExchangeRateRequest.

        The original amount of the merchant currency for calculation.  # noqa: E501

        :param base_amount: The base_amount of this ExchangeRateRequest.  # noqa: E501
        :type: float
        """
        if base_amount is None:
            raise ValueError("Invalid value for `base_amount`, must not be `None`")  # noqa: E501

        self._base_amount = base_amount

    @property
    def foreign_currency(self):
        """Gets the foreign_currency of this ExchangeRateRequest.  # noqa: E501

        The currency code to convert for Dynamic Pricing.  # noqa: E501

        :return: The foreign_currency of this ExchangeRateRequest.  # noqa: E501
        :rtype: str
        """
        return self._foreign_currency

    @foreign_currency.setter
    def foreign_currency(self, foreign_currency):
        """Sets the foreign_currency of this ExchangeRateRequest.

        The currency code to convert for Dynamic Pricing.  # noqa: E501

        :param foreign_currency: The foreign_currency of this ExchangeRateRequest.  # noqa: E501
        :type: str
        """

        self._foreign_currency = foreign_currency

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
        if not isinstance(other, ExchangeRateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
