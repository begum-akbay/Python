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


class PaymentTokenPaymentMethod(object):
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
        'payment_token': 'UsePaymentToken',
        'payment_facilitator': 'PaymentFacilitator'
    }

    attribute_map = {
        'payment_token': 'paymentToken',
        'payment_facilitator': 'paymentFacilitator'
    }

    def __init__(self, payment_token=None, payment_facilitator=None):  # noqa: E501
        """PaymentTokenPaymentMethod - a model defined in OpenAPI"""  # noqa: E501

        self._payment_token = None
        self._payment_facilitator = None
        self.discriminator = None

        self.payment_token = payment_token
        if payment_facilitator is not None:
            self.payment_facilitator = payment_facilitator

    @property
    def payment_token(self):
        """Gets the payment_token of this PaymentTokenPaymentMethod.  # noqa: E501


        :return: The payment_token of this PaymentTokenPaymentMethod.  # noqa: E501
        :rtype: UsePaymentToken
        """
        return self._payment_token

    @payment_token.setter
    def payment_token(self, payment_token):
        """Sets the payment_token of this PaymentTokenPaymentMethod.


        :param payment_token: The payment_token of this PaymentTokenPaymentMethod.  # noqa: E501
        :type: UsePaymentToken
        """
        if payment_token is None:
            raise ValueError("Invalid value for `payment_token`, must not be `None`")  # noqa: E501

        self._payment_token = payment_token

    @property
    def payment_facilitator(self):
        """Gets the payment_facilitator of this PaymentTokenPaymentMethod.  # noqa: E501


        :return: The payment_facilitator of this PaymentTokenPaymentMethod.  # noqa: E501
        :rtype: PaymentFacilitator
        """
        return self._payment_facilitator

    @payment_facilitator.setter
    def payment_facilitator(self, payment_facilitator):
        """Sets the payment_facilitator of this PaymentTokenPaymentMethod.


        :param payment_facilitator: The payment_facilitator of this PaymentTokenPaymentMethod.  # noqa: E501
        :type: PaymentFacilitator
        """

        self._payment_facilitator = payment_facilitator

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
        if not isinstance(other, PaymentTokenPaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
