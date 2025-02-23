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


class SubMerchantSplit(object):
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
        'merchant_id': 'str',
        'amount': 'float'
    }

    attribute_map = {
        'merchant_id': 'merchantID',
        'amount': 'amount'
    }

    def __init__(self, merchant_id=None, amount=None):  # noqa: E501
        """SubMerchantSplit - a model defined in OpenAPI"""  # noqa: E501

        self._merchant_id = None
        self._amount = None
        self.discriminator = None

        self.merchant_id = merchant_id
        self.amount = amount

    @property
    def merchant_id(self):
        """Gets the merchant_id of this SubMerchantSplit.  # noqa: E501

        ID of merchant for tracking.  # noqa: E501

        :return: The merchant_id of this SubMerchantSplit.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this SubMerchantSplit.

        ID of merchant for tracking.  # noqa: E501

        :param merchant_id: The merchant_id of this SubMerchantSplit.  # noqa: E501
        :type: str
        """
        if merchant_id is None:
            raise ValueError("Invalid value for `merchant_id`, must not be `None`")  # noqa: E501
        if merchant_id is not None and len(merchant_id) > 15:
            raise ValueError("Invalid value for `merchant_id`, length must be less than or equal to `15`")  # noqa: E501
        if merchant_id is not None and not re.search(r'[0-9]{1,15}', merchant_id):  # noqa: E501
            raise ValueError(r"Invalid value for `merchant_id`, must be a follow pattern or equal to `/[0-9]{1,15}/`")  # noqa: E501

        self._merchant_id = merchant_id

    @property
    def amount(self):
        """Gets the amount of this SubMerchantSplit.  # noqa: E501

        The amount each sub-merchant receives.  # noqa: E501

        :return: The amount of this SubMerchantSplit.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SubMerchantSplit.

        The amount each sub-merchant receives.  # noqa: E501

        :param amount: The amount of this SubMerchantSplit.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

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
        if not isinstance(other, SubMerchantSplit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
