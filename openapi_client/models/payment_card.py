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


class PaymentCard(object):
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
        'number': 'str',
        'expiry_date': 'Expiration',
        'security_code': 'str',
        'card_function': 'CardFunction',
        'cardholder_name': 'str',
        'bin': 'str',
        'last4': 'str',
        'brand': 'str'
    }

    attribute_map = {
        'number': 'number',
        'expiry_date': 'expiryDate',
        'security_code': 'securityCode',
        'card_function': 'cardFunction',
        'cardholder_name': 'cardholderName',
        'bin': 'bin',
        'last4': 'last4',
        'brand': 'brand'
    }

    def __init__(self, number=None, expiry_date=None, security_code=None, card_function=None, cardholder_name=None, bin=None, last4=None, brand=None):  # noqa: E501
        """PaymentCard - a model defined in OpenAPI"""  # noqa: E501

        self._number = None
        self._expiry_date = None
        self._security_code = None
        self._card_function = None
        self._cardholder_name = None
        self._bin = None
        self._last4 = None
        self._brand = None
        self.discriminator = None

        self.number = number
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if security_code is not None:
            self.security_code = security_code
        if card_function is not None:
            self.card_function = card_function
        if cardholder_name is not None:
            self.cardholder_name = cardholder_name
        if bin is not None:
            self.bin = bin
        if last4 is not None:
            self.last4 = last4
        if brand is not None:
            self.brand = brand

    @property
    def number(self):
        """Gets the number of this PaymentCard.  # noqa: E501

        Payment card number.  # noqa: E501

        :return: The number of this PaymentCard.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PaymentCard.

        Payment card number.  # noqa: E501

        :param number: The number of this PaymentCard.  # noqa: E501
        :type: str
        """
        # if number is None:
        #     raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501
        if number is not None and not re.search(r'[0-9]{13,19}', number):  # noqa: E501
            raise ValueError(r"Invalid value for `number`, must be a follow pattern or equal to `/[0-9]{13,19}/`")  # noqa: E501

        self._number = number

    @property
    def expiry_date(self):
        """Gets the expiry_date of this PaymentCard.  # noqa: E501


        :return: The expiry_date of this PaymentCard.  # noqa: E501
        :rtype: Expiration
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this PaymentCard.


        :param expiry_date: The expiry_date of this PaymentCard.  # noqa: E501
        :type: Expiration
        """

        self._expiry_date = expiry_date

    @property
    def security_code(self):
        """Gets the security_code of this PaymentCard.  # noqa: E501

        Card verification value/number.  # noqa: E501

        :return: The security_code of this PaymentCard.  # noqa: E501
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """Sets the security_code of this PaymentCard.

        Card verification value/number.  # noqa: E501

        :param security_code: The security_code of this PaymentCard.  # noqa: E501
        :type: str
        """
        if security_code is not None and len(security_code) > 4:
            raise ValueError("Invalid value for `security_code`, length must be less than or equal to `4`")  # noqa: E501
        if security_code is not None and len(security_code) < 3:
            raise ValueError("Invalid value for `security_code`, length must be greater than or equal to `3`")  # noqa: E501

        self._security_code = security_code

    @property
    def card_function(self):
        """Gets the card_function of this PaymentCard.  # noqa: E501


        :return: The card_function of this PaymentCard.  # noqa: E501
        :rtype: CardFunction
        """
        return self._card_function

    @card_function.setter
    def card_function(self, card_function):
        """Sets the card_function of this PaymentCard.


        :param card_function: The card_function of this PaymentCard.  # noqa: E501
        :type: CardFunction
        """

        self._card_function = card_function

    @property
    def cardholder_name(self):
        """Gets the cardholder_name of this PaymentCard.  # noqa: E501

        Name of the cardholder.  # noqa: E501

        :return: The cardholder_name of this PaymentCard.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        """Sets the cardholder_name of this PaymentCard.

        Name of the cardholder.  # noqa: E501

        :param cardholder_name: The cardholder_name of this PaymentCard.  # noqa: E501
        :type: str
        """
        if cardholder_name is not None and len(cardholder_name) > 96:
            raise ValueError("Invalid value for `cardholder_name`, length must be less than or equal to `96`")  # noqa: E501

        self._cardholder_name = cardholder_name

    @property
    def bin(self):
        """Gets the bin of this PaymentCard.  # noqa: E501

        The payment card BIN.  # noqa: E501

        :return: The bin of this PaymentCard.  # noqa: E501
        :rtype: str
        """
        return self._bin

    @bin.setter
    def bin(self, bin):
        """Sets the bin of this PaymentCard.

        The payment card BIN.  # noqa: E501

        :param bin: The bin of this PaymentCard.  # noqa: E501
        :type: str
        """

        self._bin = bin

    @property
    def last4(self):
        """Gets the last4 of this PaymentCard.  # noqa: E501

        The last 4 numbers of a payment card.  # noqa: E501

        :return: The last4 of this PaymentCard.  # noqa: E501
        :rtype: str
        """
        return self._last4

    @last4.setter
    def last4(self, last4):
        """Sets the last4 of this PaymentCard.

        The last 4 numbers of a payment card.  # noqa: E501

        :param last4: The last4 of this PaymentCard.  # noqa: E501
        :type: str
        """

        self._last4 = last4

    @property
    def brand(self):
        """Gets the brand of this PaymentCard.  # noqa: E501

        Required only if using dual branded card.  # noqa: E501

        :return: The brand of this PaymentCard.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PaymentCard.

        Required only if using dual branded card.  # noqa: E501

        :param brand: The brand of this PaymentCard.  # noqa: E501
        :type: str
        """

        self._brand = brand

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
        if not isinstance(other, PaymentCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
