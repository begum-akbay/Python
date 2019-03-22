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


class PaymentTokenization(object):
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
        'value': 'str',
        'reusable': 'bool',
        'decline_duplicates': 'bool',
        'last4': 'str',
        'brand': 'str',
        'country': 'str',
        'account_verification': 'bool',
        'security_code': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'reusable': 'reusable',
        'decline_duplicates': 'declineDuplicates',
        'last4': 'last4',
        'brand': 'brand',
        'country': 'country',
        'account_verification': 'accountVerification',
        'security_code': 'securityCode'
    }

    def __init__(self, type=None, value=None, reusable=True, decline_duplicates=False, last4=None, brand=None, country=None, account_verification=False, security_code=None):  # noqa: E501
        """PaymentTokenization - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._value = None
        self._reusable = None
        self._decline_duplicates = None
        self._last4 = None
        self._brand = None
        self._country = None
        self._account_verification = None
        self._security_code = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if reusable is not None:
            self.reusable = reusable
        if decline_duplicates is not None:
            self.decline_duplicates = decline_duplicates
        if last4 is not None:
            self.last4 = last4
        if brand is not None:
            self.brand = brand
        if country is not None:
            self.country = country
        if account_verification is not None:
            self.account_verification = account_verification
        if security_code is not None:
            self.security_code = security_code

    @property
    def type(self):
        """Gets the type of this PaymentTokenization.  # noqa: E501


        :return: The type of this PaymentTokenization.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PaymentTokenization.


        :param type: The type of this PaymentTokenization.  # noqa: E501
        :type: str
        """
        allowed_values = ["PAYMENT_CARD"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this PaymentTokenization.  # noqa: E501

        Client supplied Payment Token value  # noqa: E501

        :return: The value of this PaymentTokenization.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PaymentTokenization.

        Client supplied Payment Token value  # noqa: E501

        :param value: The value of this PaymentTokenization.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def reusable(self):
        """Gets the reusable of this PaymentTokenization.  # noqa: E501

        One time or reusable token  # noqa: E501

        :return: The reusable of this PaymentTokenization.  # noqa: E501
        :rtype: bool
        """
        return self._reusable

    @reusable.setter
    def reusable(self, reusable):
        """Sets the reusable of this PaymentTokenization.

        One time or reusable token  # noqa: E501

        :param reusable: The reusable of this PaymentTokenization.  # noqa: E501
        :type: bool
        """

        self._reusable = reusable

    @property
    def decline_duplicates(self):
        """Gets the decline_duplicates of this PaymentTokenization.  # noqa: E501

        Decline duplicate payment info if client token is supplied  # noqa: E501

        :return: The decline_duplicates of this PaymentTokenization.  # noqa: E501
        :rtype: bool
        """
        return self._decline_duplicates

    @decline_duplicates.setter
    def decline_duplicates(self, decline_duplicates):
        """Sets the decline_duplicates of this PaymentTokenization.

        Decline duplicate payment info if client token is supplied  # noqa: E501

        :param decline_duplicates: The decline_duplicates of this PaymentTokenization.  # noqa: E501
        :type: bool
        """

        self._decline_duplicates = decline_duplicates

    @property
    def last4(self):
        """Gets the last4 of this PaymentTokenization.  # noqa: E501

        The last 4 payment card numbers  # noqa: E501

        :return: The last4 of this PaymentTokenization.  # noqa: E501
        :rtype: str
        """
        return self._last4

    @last4.setter
    def last4(self, last4):
        """Sets the last4 of this PaymentTokenization.

        The last 4 payment card numbers  # noqa: E501

        :param last4: The last4 of this PaymentTokenization.  # noqa: E501
        :type: str
        """

        self._last4 = last4

    @property
    def brand(self):
        """Gets the brand of this PaymentTokenization.  # noqa: E501

        Only for tokenization with payment  # noqa: E501

        :return: The brand of this PaymentTokenization.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PaymentTokenization.

        Only for tokenization with payment  # noqa: E501

        :param brand: The brand of this PaymentTokenization.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def country(self):
        """Gets the country of this PaymentTokenization.  # noqa: E501

        Only for tokenization with payment  # noqa: E501

        :return: The country of this PaymentTokenization.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PaymentTokenization.

        Only for tokenization with payment  # noqa: E501

        :param country: The country of this PaymentTokenization.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def account_verification(self):
        """Gets the account_verification of this PaymentTokenization.  # noqa: E501


        :return: The account_verification of this PaymentTokenization.  # noqa: E501
        :rtype: bool
        """
        return self._account_verification

    @account_verification.setter
    def account_verification(self, account_verification):
        """Sets the account_verification of this PaymentTokenization.


        :param account_verification: The account_verification of this PaymentTokenization.  # noqa: E501
        :type: bool
        """

        self._account_verification = account_verification

    @property
    def security_code(self):
        """Gets the security_code of this PaymentTokenization.  # noqa: E501

        Card Verification Value/Number  # noqa: E501

        :return: The security_code of this PaymentTokenization.  # noqa: E501
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """Sets the security_code of this PaymentTokenization.

        Card Verification Value/Number  # noqa: E501

        :param security_code: The security_code of this PaymentTokenization.  # noqa: E501
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
        if not isinstance(other, PaymentTokenization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
