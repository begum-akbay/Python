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


class EncryptedGooglePayWalletPaymentMethodAllOf(object):
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
        'encrypted_google_pay': 'EncryptedGooglePay'
    }

    attribute_map = {
        'encrypted_google_pay': 'encryptedGooglePay'
    }

    def __init__(self, encrypted_google_pay=None):  # noqa: E501
        """EncryptedGooglePayWalletPaymentMethodAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._encrypted_google_pay = None
        self.discriminator = None

        self.encrypted_google_pay = encrypted_google_pay

    @property
    def encrypted_google_pay(self):
        """Gets the encrypted_google_pay of this EncryptedGooglePayWalletPaymentMethodAllOf.  # noqa: E501


        :return: The encrypted_google_pay of this EncryptedGooglePayWalletPaymentMethodAllOf.  # noqa: E501
        :rtype: EncryptedGooglePay
        """
        return self._encrypted_google_pay

    @encrypted_google_pay.setter
    def encrypted_google_pay(self, encrypted_google_pay):
        """Sets the encrypted_google_pay of this EncryptedGooglePayWalletPaymentMethodAllOf.


        :param encrypted_google_pay: The encrypted_google_pay of this EncryptedGooglePayWalletPaymentMethodAllOf.  # noqa: E501
        :type: EncryptedGooglePay
        """
        if encrypted_google_pay is None:
            raise ValueError("Invalid value for `encrypted_google_pay`, must not be `None`")  # noqa: E501

        self._encrypted_google_pay = encrypted_google_pay

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
        if not isinstance(other, EncryptedGooglePayWalletPaymentMethodAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
