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


class PaymentTokenPreAuthTransactionAllOf(object):
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
        'payment_method': 'PaymentTokenPaymentMethod',
        'stored_credentials': 'StoredCredential',
        'split_shipment': 'SplitShipment',
        'settlement_split': 'list[SubMerchantSplit]',
        'authentication_request': 'AuthenticationRequest',
        'authentication_result': 'AuthenticationResult',
        'decremental_flag': 'bool'
    }

    attribute_map = {
        'payment_method': 'paymentMethod',
        'stored_credentials': 'storedCredentials',
        'split_shipment': 'splitShipment',
        'settlement_split': 'settlementSplit',
        'authentication_request': 'authenticationRequest',
        'authentication_result': 'authenticationResult',
        'decremental_flag': 'decrementalFlag'
    }

    def __init__(self, payment_method=None, stored_credentials=None, split_shipment=None, settlement_split=None, authentication_request=None, authentication_result=None, decremental_flag=False):  # noqa: E501
        """PaymentTokenPreAuthTransactionAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._payment_method = None
        self._stored_credentials = None
        self._split_shipment = None
        self._settlement_split = None
        self._authentication_request = None
        self._authentication_result = None
        self._decremental_flag = None
        self.discriminator = None

        self.payment_method = payment_method
        if stored_credentials is not None:
            self.stored_credentials = stored_credentials
        if split_shipment is not None:
            self.split_shipment = split_shipment
        if settlement_split is not None:
            self.settlement_split = settlement_split
        if authentication_request is not None:
            self.authentication_request = authentication_request
        if authentication_result is not None:
            self.authentication_result = authentication_result
        if decremental_flag is not None:
            self.decremental_flag = decremental_flag

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501


        :return: The payment_method of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :rtype: PaymentTokenPaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentTokenPreAuthTransactionAllOf.


        :param payment_method: The payment_method of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :type: PaymentTokenPaymentMethod
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

    @property
    def stored_credentials(self):
        """Gets the stored_credentials of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501


        :return: The stored_credentials of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :rtype: StoredCredential
        """
        return self._stored_credentials

    @stored_credentials.setter
    def stored_credentials(self, stored_credentials):
        """Sets the stored_credentials of this PaymentTokenPreAuthTransactionAllOf.


        :param stored_credentials: The stored_credentials of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :type: StoredCredential
        """

        self._stored_credentials = stored_credentials

    @property
    def split_shipment(self):
        """Gets the split_shipment of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501


        :return: The split_shipment of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :rtype: SplitShipment
        """
        return self._split_shipment

    @split_shipment.setter
    def split_shipment(self, split_shipment):
        """Sets the split_shipment of this PaymentTokenPreAuthTransactionAllOf.


        :param split_shipment: The split_shipment of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :type: SplitShipment
        """

        self._split_shipment = split_shipment

    @property
    def settlement_split(self):
        """Gets the settlement_split of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501

        Settle with multiple sub-merchants, sale and preAuth only.  # noqa: E501

        :return: The settlement_split of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :rtype: list[SubMerchantSplit]
        """
        return self._settlement_split

    @settlement_split.setter
    def settlement_split(self, settlement_split):
        """Sets the settlement_split of this PaymentTokenPreAuthTransactionAllOf.

        Settle with multiple sub-merchants, sale and preAuth only.  # noqa: E501

        :param settlement_split: The settlement_split of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :type: list[SubMerchantSplit]
        """

        self._settlement_split = settlement_split

    @property
    def authentication_request(self):
        """Gets the authentication_request of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501


        :return: The authentication_request of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :rtype: AuthenticationRequest
        """
        return self._authentication_request

    @authentication_request.setter
    def authentication_request(self, authentication_request):
        """Sets the authentication_request of this PaymentTokenPreAuthTransactionAllOf.


        :param authentication_request: The authentication_request of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :type: AuthenticationRequest
        """

        self._authentication_request = authentication_request

    @property
    def authentication_result(self):
        """Gets the authentication_result of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501


        :return: The authentication_result of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :rtype: AuthenticationResult
        """
        return self._authentication_result

    @authentication_result.setter
    def authentication_result(self, authentication_result):
        """Sets the authentication_result of this PaymentTokenPreAuthTransactionAllOf.


        :param authentication_result: The authentication_result of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :type: AuthenticationResult
        """

        self._authentication_result = authentication_result

    @property
    def decremental_flag(self):
        """Gets the decremental_flag of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501

        This flag can only be used in a preAuth transaction that updates the amount of a previous preAuth transaction to either increase the preAuth amount (DecrementalPreAuthFlag = false) or decrease the preAuth amount (DecrementalPreAuthFlag = true).  # noqa: E501

        :return: The decremental_flag of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._decremental_flag

    @decremental_flag.setter
    def decremental_flag(self, decremental_flag):
        """Sets the decremental_flag of this PaymentTokenPreAuthTransactionAllOf.

        This flag can only be used in a preAuth transaction that updates the amount of a previous preAuth transaction to either increase the preAuth amount (DecrementalPreAuthFlag = false) or decrease the preAuth amount (DecrementalPreAuthFlag = true).  # noqa: E501

        :param decremental_flag: The decremental_flag of this PaymentTokenPreAuthTransactionAllOf.  # noqa: E501
        :type: bool
        """

        self._decremental_flag = decremental_flag

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
        if not isinstance(other, PaymentTokenPreAuthTransactionAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
