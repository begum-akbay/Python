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


class PaymentDevice(object):
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
        'device_type': 'str',
        'data': 'str',
        'security_code': 'str',
        'cardholder_name': 'str',
        'card_function': 'CardFunction',
        'brand': 'str'
    }

    attribute_map = {
        'device_type': 'deviceType',
        'data': 'data',
        'security_code': 'securityCode',
        'cardholder_name': 'cardholderName',
        'card_function': 'cardFunction',
        'brand': 'brand'
    }

    def __init__(self, device_type=None, data=None, security_code=None, cardholder_name=None, card_function=None, brand=None):  # noqa: E501
        """PaymentDevice - a model defined in OpenAPI"""  # noqa: E501

        self._device_type = None
        self._data = None
        self._security_code = None
        self._cardholder_name = None
        self._card_function = None
        self._brand = None
        self.discriminator = None

        self.device_type = device_type
        self.data = data
        if security_code is not None:
            self.security_code = security_code
        if cardholder_name is not None:
            self.cardholder_name = cardholder_name
        if card_function is not None:
            self.card_function = card_function
        if brand is not None:
            self.brand = brand

    @property
    def device_type(self):
        """Gets the device_type of this PaymentDevice.  # noqa: E501

        The data format.  # noqa: E501

        :return: The device_type of this PaymentDevice.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this PaymentDevice.

        The data format.  # noqa: E501

        :param device_type: The device_type of this PaymentDevice.  # noqa: E501
        :type: str
        """
        if device_type is None:
            raise ValueError("Invalid value for `device_type`, must not be `None`")  # noqa: E501
        allowed_values = ["SWIPE"]  # noqa: E501
        if device_type not in allowed_values:
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"  # noqa: E501
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def data(self):
        """Gets the data of this PaymentDevice.  # noqa: E501

        Data from device containing, at a minimum, a transaction-unique key serial number (KSN) and track 2 card data.  # noqa: E501

        :return: The data of this PaymentDevice.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PaymentDevice.

        Data from device containing, at a minimum, a transaction-unique key serial number (KSN) and track 2 card data.  # noqa: E501

        :param data: The data of this PaymentDevice.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501
        if data is not None and not re.search(r'^(?!\s*$).+', data):  # noqa: E501
            raise ValueError(r"Invalid value for `data`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._data = data

    @property
    def security_code(self):
        """Gets the security_code of this PaymentDevice.  # noqa: E501

        Card verification value/number.  # noqa: E501

        :return: The security_code of this PaymentDevice.  # noqa: E501
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """Sets the security_code of this PaymentDevice.

        Card verification value/number.  # noqa: E501

        :param security_code: The security_code of this PaymentDevice.  # noqa: E501
        :type: str
        """
        if security_code is not None and len(security_code) > 4:
            raise ValueError("Invalid value for `security_code`, length must be less than or equal to `4`")  # noqa: E501
        if security_code is not None and len(security_code) < 3:
            raise ValueError("Invalid value for `security_code`, length must be greater than or equal to `3`")  # noqa: E501

        self._security_code = security_code

    @property
    def cardholder_name(self):
        """Gets the cardholder_name of this PaymentDevice.  # noqa: E501

        Name of cardholder.  # noqa: E501

        :return: The cardholder_name of this PaymentDevice.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        """Sets the cardholder_name of this PaymentDevice.

        Name of cardholder.  # noqa: E501

        :param cardholder_name: The cardholder_name of this PaymentDevice.  # noqa: E501
        :type: str
        """

        self._cardholder_name = cardholder_name

    @property
    def card_function(self):
        """Gets the card_function of this PaymentDevice.  # noqa: E501


        :return: The card_function of this PaymentDevice.  # noqa: E501
        :rtype: CardFunction
        """
        return self._card_function

    @card_function.setter
    def card_function(self, card_function):
        """Sets the card_function of this PaymentDevice.


        :param card_function: The card_function of this PaymentDevice.  # noqa: E501
        :type: CardFunction
        """

        self._card_function = card_function

    @property
    def brand(self):
        """Gets the brand of this PaymentDevice.  # noqa: E501

        The card brand.  # noqa: E501

        :return: The brand of this PaymentDevice.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PaymentDevice.

        The card brand.  # noqa: E501

        :param brand: The brand of this PaymentDevice.  # noqa: E501
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
        if not isinstance(other, PaymentDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
