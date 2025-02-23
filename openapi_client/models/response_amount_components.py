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


class ResponseAmountComponents(object):
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
        'subtotal': 'float',
        'vat_amount': 'float',
        'local_tax': 'float',
        'shipping': 'float',
        'cashback': 'float',
        'tip': 'float',
        'convenience_fee': 'float'
    }

    attribute_map = {
        'subtotal': 'subtotal',
        'vat_amount': 'vatAmount',
        'local_tax': 'localTax',
        'shipping': 'shipping',
        'cashback': 'cashback',
        'tip': 'tip',
        'convenience_fee': 'convenienceFee'
    }

    def __init__(self, subtotal=None, vat_amount=None, local_tax=None, shipping=None, cashback=None, tip=None, convenience_fee=None):  # noqa: E501
        """ResponseAmountComponents - a model defined in OpenAPI"""  # noqa: E501

        self._subtotal = None
        self._vat_amount = None
        self._local_tax = None
        self._shipping = None
        self._cashback = None
        self._tip = None
        self._convenience_fee = None
        self.discriminator = None

        if subtotal is not None:
            self.subtotal = subtotal
        if vat_amount is not None:
            self.vat_amount = vat_amount
        if local_tax is not None:
            self.local_tax = local_tax
        if shipping is not None:
            self.shipping = shipping
        if cashback is not None:
            self.cashback = cashback
        if tip is not None:
            self.tip = tip
        if convenience_fee is not None:
            self.convenience_fee = convenience_fee

    @property
    def subtotal(self):
        """Gets the subtotal of this ResponseAmountComponents.  # noqa: E501

        Subtotal amount.  # noqa: E501

        :return: The subtotal of this ResponseAmountComponents.  # noqa: E501
        :rtype: float
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """Sets the subtotal of this ResponseAmountComponents.

        Subtotal amount.  # noqa: E501

        :param subtotal: The subtotal of this ResponseAmountComponents.  # noqa: E501
        :type: float
        """

        self._subtotal = subtotal

    @property
    def vat_amount(self):
        """Gets the vat_amount of this ResponseAmountComponents.  # noqa: E501

        Value-added tax amount.  # noqa: E501

        :return: The vat_amount of this ResponseAmountComponents.  # noqa: E501
        :rtype: float
        """
        return self._vat_amount

    @vat_amount.setter
    def vat_amount(self, vat_amount):
        """Sets the vat_amount of this ResponseAmountComponents.

        Value-added tax amount.  # noqa: E501

        :param vat_amount: The vat_amount of this ResponseAmountComponents.  # noqa: E501
        :type: float
        """

        self._vat_amount = vat_amount

    @property
    def local_tax(self):
        """Gets the local_tax of this ResponseAmountComponents.  # noqa: E501

        Local tax amount.  # noqa: E501

        :return: The local_tax of this ResponseAmountComponents.  # noqa: E501
        :rtype: float
        """
        return self._local_tax

    @local_tax.setter
    def local_tax(self, local_tax):
        """Sets the local_tax of this ResponseAmountComponents.

        Local tax amount.  # noqa: E501

        :param local_tax: The local_tax of this ResponseAmountComponents.  # noqa: E501
        :type: float
        """

        self._local_tax = local_tax

    @property
    def shipping(self):
        """Gets the shipping of this ResponseAmountComponents.  # noqa: E501

        Shipping amount.  # noqa: E501

        :return: The shipping of this ResponseAmountComponents.  # noqa: E501
        :rtype: float
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this ResponseAmountComponents.

        Shipping amount.  # noqa: E501

        :param shipping: The shipping of this ResponseAmountComponents.  # noqa: E501
        :type: float
        """

        self._shipping = shipping

    @property
    def cashback(self):
        """Gets the cashback of this ResponseAmountComponents.  # noqa: E501

        Cashback amount.  # noqa: E501

        :return: The cashback of this ResponseAmountComponents.  # noqa: E501
        :rtype: float
        """
        return self._cashback

    @cashback.setter
    def cashback(self, cashback):
        """Sets the cashback of this ResponseAmountComponents.

        Cashback amount.  # noqa: E501

        :param cashback: The cashback of this ResponseAmountComponents.  # noqa: E501
        :type: float
        """

        self._cashback = cashback

    @property
    def tip(self):
        """Gets the tip of this ResponseAmountComponents.  # noqa: E501

        Tip amount.  # noqa: E501

        :return: The tip of this ResponseAmountComponents.  # noqa: E501
        :rtype: float
        """
        return self._tip

    @tip.setter
    def tip(self, tip):
        """Sets the tip of this ResponseAmountComponents.

        Tip amount.  # noqa: E501

        :param tip: The tip of this ResponseAmountComponents.  # noqa: E501
        :type: float
        """

        self._tip = tip

    @property
    def convenience_fee(self):
        """Gets the convenience_fee of this ResponseAmountComponents.  # noqa: E501

        Amount added for proccessing or handling fees.  # noqa: E501

        :return: The convenience_fee of this ResponseAmountComponents.  # noqa: E501
        :rtype: float
        """
        return self._convenience_fee

    @convenience_fee.setter
    def convenience_fee(self, convenience_fee):
        """Sets the convenience_fee of this ResponseAmountComponents.

        Amount added for proccessing or handling fees.  # noqa: E501

        :param convenience_fee: The convenience_fee of this ResponseAmountComponents.  # noqa: E501
        :type: float
        """

        self._convenience_fee = convenience_fee

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
        if not isinstance(other, ResponseAmountComponents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
