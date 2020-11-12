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


class Merchant(object):
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
        'mcc': 'str',
        'merchant_unique_id': 'str',
        'location': 'Location',
        'user_defined': 'object'
    }

    attribute_map = {
        'mcc': 'mcc',
        'merchant_unique_id': 'merchantUniqueId',
        'location': 'location',
        'user_defined': 'userDefined'
    }

    def __init__(self, mcc=None, merchant_unique_id=None, location=None, user_defined=None):  # noqa: E501
        """Merchant - a model defined in OpenAPI"""  # noqa: E501

        self._mcc = None
        self._merchant_unique_id = None
        self._location = None
        self._user_defined = None
        self.discriminator = None

        if mcc is not None:
            self.mcc = mcc
        self.merchant_unique_id = merchant_unique_id
        if location is not None:
            self.location = location
        if user_defined is not None:
            self.user_defined = user_defined

    @property
    def mcc(self):
        """Gets the mcc of this Merchant.  # noqa: E501

        The 4-digit Merchant Category Code. The merchant might be associated with multiple MCCs. In that case the MCC provided here will be the one that better describes the current transaction.  # noqa: E501

        :return: The mcc of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc):
        """Sets the mcc of this Merchant.

        The 4-digit Merchant Category Code. The merchant might be associated with multiple MCCs. In that case the MCC provided here will be the one that better describes the current transaction.  # noqa: E501

        :param mcc: The mcc of this Merchant.  # noqa: E501
        :type: str
        """

        self._mcc = mcc

    @property
    def merchant_unique_id(self):
        """Gets the merchant_unique_id of this Merchant.  # noqa: E501

        The unique ID of this merchant. Must be unique for the entire system (not just within a specific industry).  # noqa: E501

        :return: The merchant_unique_id of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._merchant_unique_id

    @merchant_unique_id.setter
    def merchant_unique_id(self, merchant_unique_id):
        """Sets the merchant_unique_id of this Merchant.

        The unique ID of this merchant. Must be unique for the entire system (not just within a specific industry).  # noqa: E501

        :param merchant_unique_id: The merchant_unique_id of this Merchant.  # noqa: E501
        :type: str
        """
        if merchant_unique_id is None:
            raise ValueError("Invalid value for `merchant_unique_id`, must not be `None`")  # noqa: E501
        if merchant_unique_id is not None and not re.search(r'^(?!\s*$).+', merchant_unique_id):  # noqa: E501
            raise ValueError(r"Invalid value for `merchant_unique_id`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._merchant_unique_id = merchant_unique_id

    @property
    def location(self):
        """Gets the location of this Merchant.  # noqa: E501


        :return: The location of this Merchant.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Merchant.


        :param location: The location of this Merchant.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def user_defined(self):
        """Gets the user_defined of this Merchant.  # noqa: E501

        A JSON object that can carry any additional information about the merchant that might be helpful for fraud detection.  # noqa: E501

        :return: The user_defined of this Merchant.  # noqa: E501
        :rtype: object
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this Merchant.

        A JSON object that can carry any additional information about the merchant that might be helpful for fraud detection.  # noqa: E501

        :param user_defined: The user_defined of this Merchant.  # noqa: E501
        :type: object
        """

        self._user_defined = user_defined

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
        if not isinstance(other, Merchant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
