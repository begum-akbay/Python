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


class ClientRegistration(object):
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
        'merchant_ref': 'str',
        'transaction_type': 'str',
        'customer': 'Customer',
        'merchant': 'Merchant',
        'device': 'FraudRegistrationDevice',
        'user_defined': 'object',
        'original_transaction_type': 'str'
    }

    attribute_map = {
        'merchant_ref': 'merchantRef',
        'transaction_type': 'transactionType',
        'customer': 'customer',
        'merchant': 'merchant',
        'device': 'device',
        'user_defined': 'userDefined',
        'original_transaction_type': 'originalTransactionType'
    }

    def __init__(self, merchant_ref=None, transaction_type=None, customer=None, merchant=None, device=None, user_defined=None, original_transaction_type=None):  # noqa: E501
        """ClientRegistration - a model defined in OpenAPI"""  # noqa: E501

        self._merchant_ref = None
        self._transaction_type = None
        self._customer = None
        self._merchant = None
        self._device = None
        self._user_defined = None
        self._original_transaction_type = None
        self.discriminator = None

        if merchant_ref is not None:
            self.merchant_ref = merchant_ref
        self.transaction_type = transaction_type
        self.customer = customer
        self.merchant = merchant
        if device is not None:
            self.device = device
        if user_defined is not None:
            self.user_defined = user_defined
        self.original_transaction_type = original_transaction_type

    @property
    def merchant_ref(self):
        """Gets the merchant_ref of this ClientRegistration.  # noqa: E501

        Merchant reference code. Used by FirstAPI and reflected in settlement records and webhook notifications. Typically, the merchantRef field is the purchase order number or unique sequence value associated to a given transaction.  # noqa: E501

        :return: The merchant_ref of this ClientRegistration.  # noqa: E501
        :rtype: str
        """
        return self._merchant_ref

    @merchant_ref.setter
    def merchant_ref(self, merchant_ref):
        """Sets the merchant_ref of this ClientRegistration.

        Merchant reference code. Used by FirstAPI and reflected in settlement records and webhook notifications. Typically, the merchantRef field is the purchase order number or unique sequence value associated to a given transaction.  # noqa: E501

        :param merchant_ref: The merchant_ref of this ClientRegistration.  # noqa: E501
        :type: str
        """

        self._merchant_ref = merchant_ref

    @property
    def transaction_type(self):
        """Gets the transaction_type of this ClientRegistration.  # noqa: E501

        Type of transaction merchant wants to process.  # noqa: E501

        :return: The transaction_type of this ClientRegistration.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this ClientRegistration.

        Type of transaction merchant wants to process.  # noqa: E501

        :param transaction_type: The transaction_type of this ClientRegistration.  # noqa: E501
        :type: str
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def customer(self):
        """Gets the customer of this ClientRegistration.  # noqa: E501


        :return: The customer of this ClientRegistration.  # noqa: E501
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this ClientRegistration.


        :param customer: The customer of this ClientRegistration.  # noqa: E501
        :type: Customer
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def merchant(self):
        """Gets the merchant of this ClientRegistration.  # noqa: E501


        :return: The merchant of this ClientRegistration.  # noqa: E501
        :rtype: Merchant
        """
        return self._merchant

    @merchant.setter
    def merchant(self, merchant):
        """Sets the merchant of this ClientRegistration.


        :param merchant: The merchant of this ClientRegistration.  # noqa: E501
        :type: Merchant
        """
        if merchant is None:
            raise ValueError("Invalid value for `merchant`, must not be `None`")  # noqa: E501

        self._merchant = merchant

    @property
    def device(self):
        """Gets the device of this ClientRegistration.  # noqa: E501


        :return: The device of this ClientRegistration.  # noqa: E501
        :rtype: FraudRegistrationDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this ClientRegistration.


        :param device: The device of this ClientRegistration.  # noqa: E501
        :type: FraudRegistrationDevice
        """

        self._device = device

    @property
    def user_defined(self):
        """Gets the user_defined of this ClientRegistration.  # noqa: E501

        A JSON object that can carry any additional information that might be helpful for fraud detection.  # noqa: E501

        :return: The user_defined of this ClientRegistration.  # noqa: E501
        :rtype: object
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this ClientRegistration.

        A JSON object that can carry any additional information that might be helpful for fraud detection.  # noqa: E501

        :param user_defined: The user_defined of this ClientRegistration.  # noqa: E501
        :type: object
        """

        self._user_defined = user_defined

    @property
    def original_transaction_type(self):
        """Gets the original_transaction_type of this ClientRegistration.  # noqa: E501

        Defines the type of the original transaction that is being evaluated for the Fraud Score.  # noqa: E501

        :return: The original_transaction_type of this ClientRegistration.  # noqa: E501
        :rtype: str
        """
        return self._original_transaction_type

    @original_transaction_type.setter
    def original_transaction_type(self, original_transaction_type):
        """Sets the original_transaction_type of this ClientRegistration.

        Defines the type of the original transaction that is being evaluated for the Fraud Score.  # noqa: E501

        :param original_transaction_type: The original_transaction_type of this ClientRegistration.  # noqa: E501
        :type: str
        """
        if original_transaction_type is None:
            raise ValueError("Invalid value for `original_transaction_type`, must not be `None`")  # noqa: E501

        self._original_transaction_type = original_transaction_type

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
        if not isinstance(other, ClientRegistration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
