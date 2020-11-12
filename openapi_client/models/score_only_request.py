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


class ScoreOnlyRequest(object):
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
        'original_transaction_type': 'str',
        'original_transaction_id': 'str',
        'amount': 'str',
        'currency_code': 'str',
        'customer': 'Customer',
        'billing_address': 'BillingAddress',
        'device': 'Device',
        'loyalty': 'Loyalty',
        'payment': 'Payment',
        'merchant': 'Merchant',
        'order': 'FraudOrder',
        'user_defined': 'object'
    }

    attribute_map = {
        'merchant_ref': 'merchantRef',
        'transaction_type': 'transactionType',
        'original_transaction_type': 'originalTransactionType',
        'original_transaction_id': 'originalTransactionId',
        'amount': 'amount',
        'currency_code': 'currencyCode',
        'customer': 'customer',
        'billing_address': 'billingAddress',
        'device': 'device',
        'loyalty': 'loyalty',
        'payment': 'payment',
        'merchant': 'merchant',
        'order': 'order',
        'user_defined': 'userDefined'
    }

    def __init__(self, merchant_ref=None, transaction_type=None, original_transaction_type=None, original_transaction_id=None, amount=None, currency_code=None, customer=None, billing_address=None, device=None, loyalty=None, payment=None, merchant=None, order=None, user_defined=None):  # noqa: E501
        """ScoreOnlyRequest - a model defined in OpenAPI"""  # noqa: E501

        self._merchant_ref = None
        self._transaction_type = None
        self._original_transaction_type = None
        self._original_transaction_id = None
        self._amount = None
        self._currency_code = None
        self._customer = None
        self._billing_address = None
        self._device = None
        self._loyalty = None
        self._payment = None
        self._merchant = None
        self._order = None
        self._user_defined = None
        self.discriminator = None

        if merchant_ref is not None:
            self.merchant_ref = merchant_ref
        self.transaction_type = transaction_type
        self.original_transaction_type = original_transaction_type
        self.original_transaction_id = original_transaction_id
        self.amount = amount
        self.currency_code = currency_code
        if customer is not None:
            self.customer = customer
        if billing_address is not None:
            self.billing_address = billing_address
        if device is not None:
            self.device = device
        if loyalty is not None:
            self.loyalty = loyalty
        self.payment = payment
        self.merchant = merchant
        if order is not None:
            self.order = order
        if user_defined is not None:
            self.user_defined = user_defined

    @property
    def merchant_ref(self):
        """Gets the merchant_ref of this ScoreOnlyRequest.  # noqa: E501

        Merchant reference code. Used by FirstAPI and reflected in settlement records and Webhook notifications. Typically, the merchantRef field is the purchase order number or unique sequence value associated to a given transaction.  # noqa: E501

        :return: The merchant_ref of this ScoreOnlyRequest.  # noqa: E501
        :rtype: str
        """
        return self._merchant_ref

    @merchant_ref.setter
    def merchant_ref(self, merchant_ref):
        """Sets the merchant_ref of this ScoreOnlyRequest.

        Merchant reference code. Used by FirstAPI and reflected in settlement records and Webhook notifications. Typically, the merchantRef field is the purchase order number or unique sequence value associated to a given transaction.  # noqa: E501

        :param merchant_ref: The merchant_ref of this ScoreOnlyRequest.  # noqa: E501
        :type: str
        """

        self._merchant_ref = merchant_ref

    @property
    def transaction_type(self):
        """Gets the transaction_type of this ScoreOnlyRequest.  # noqa: E501

        Type of transaction merchant wants to process.  # noqa: E501

        :return: The transaction_type of this ScoreOnlyRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this ScoreOnlyRequest.

        Type of transaction merchant wants to process.  # noqa: E501

        :param transaction_type: The transaction_type of this ScoreOnlyRequest.  # noqa: E501
        :type: str
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def original_transaction_type(self):
        """Gets the original_transaction_type of this ScoreOnlyRequest.  # noqa: E501

        Defines the type of the original transaction that is being evaluated for the Fraud Score.  # noqa: E501

        :return: The original_transaction_type of this ScoreOnlyRequest.  # noqa: E501
        :rtype: str
        """
        return self._original_transaction_type

    @original_transaction_type.setter
    def original_transaction_type(self, original_transaction_type):
        """Sets the original_transaction_type of this ScoreOnlyRequest.

        Defines the type of the original transaction that is being evaluated for the Fraud Score.  # noqa: E501

        :param original_transaction_type: The original_transaction_type of this ScoreOnlyRequest.  # noqa: E501
        :type: str
        """
        if original_transaction_type is None:
            raise ValueError("Invalid value for `original_transaction_type`, must not be `None`")  # noqa: E501
        allowed_values = ["transaction/authorization", "transaction/authorization-reversal", "transaction/deposit", "transaction/deposit-reversal", "transaction/purchase", "transaction/purchase-reversal", "transaction/refund-authorization", "transaction/refund-deposit", "transaction/verification", "transaction/balance-inquiry"]  # noqa: E501
        if original_transaction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `original_transaction_type` ({0}), must be one of {1}"  # noqa: E501
                .format(original_transaction_type, allowed_values)
            )

        self._original_transaction_type = original_transaction_type

    @property
    def original_transaction_id(self):
        """Gets the original_transaction_id of this ScoreOnlyRequest.  # noqa: E501

        The unique ID of this transaction. Must be unique for the entire system (not just within a specific merchant or industry). Subsequent requests related to the same transaction must have the same transactionId (e.g. transaction/deposit or transaction/authorization-reversal). This field is used for matching transactions with settlement and chargeback information. If there is no such ID available you may wish to compose one from fields available in both systems. Consider including backend, issuer, merchant id, date and time, amount, etc. as necessary.  # noqa: E501

        :return: The original_transaction_id of this ScoreOnlyRequest.  # noqa: E501
        :rtype: str
        """
        return self._original_transaction_id

    @original_transaction_id.setter
    def original_transaction_id(self, original_transaction_id):
        """Sets the original_transaction_id of this ScoreOnlyRequest.

        The unique ID of this transaction. Must be unique for the entire system (not just within a specific merchant or industry). Subsequent requests related to the same transaction must have the same transactionId (e.g. transaction/deposit or transaction/authorization-reversal). This field is used for matching transactions with settlement and chargeback information. If there is no such ID available you may wish to compose one from fields available in both systems. Consider including backend, issuer, merchant id, date and time, amount, etc. as necessary.  # noqa: E501

        :param original_transaction_id: The original_transaction_id of this ScoreOnlyRequest.  # noqa: E501
        :type: str
        """
        if original_transaction_id is None:
            raise ValueError("Invalid value for `original_transaction_id`, must not be `None`")  # noqa: E501
        if original_transaction_id is not None and not re.search(r'^(?!\s*$).+', original_transaction_id):  # noqa: E501
            raise ValueError(r"Invalid value for `original_transaction_id`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._original_transaction_id = original_transaction_id

    @property
    def amount(self):
        """Gets the amount of this ScoreOnlyRequest.  # noqa: E501

        The amount processed for the original transaction.  # noqa: E501

        :return: The amount of this ScoreOnlyRequest.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ScoreOnlyRequest.

        The amount processed for the original transaction.  # noqa: E501

        :param amount: The amount of this ScoreOnlyRequest.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501
        if amount is not None and not re.search(r'^(?!\s*$).+', amount):  # noqa: E501
            raise ValueError(r"Invalid value for `amount`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._amount = amount

    @property
    def currency_code(self):
        """Gets the currency_code of this ScoreOnlyRequest.  # noqa: E501

        The currency of the original transaction.  # noqa: E501

        :return: The currency_code of this ScoreOnlyRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this ScoreOnlyRequest.

        The currency of the original transaction.  # noqa: E501

        :param currency_code: The currency_code of this ScoreOnlyRequest.  # noqa: E501
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501
        if currency_code is not None and not re.search(r'([A-Z]{3})|([0-9]{3})', currency_code):  # noqa: E501
            raise ValueError(r"Invalid value for `currency_code`, must be a follow pattern or equal to `/([A-Z]{3})|([0-9]{3})/`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def customer(self):
        """Gets the customer of this ScoreOnlyRequest.  # noqa: E501


        :return: The customer of this ScoreOnlyRequest.  # noqa: E501
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this ScoreOnlyRequest.


        :param customer: The customer of this ScoreOnlyRequest.  # noqa: E501
        :type: Customer
        """

        self._customer = customer

    @property
    def billing_address(self):
        """Gets the billing_address of this ScoreOnlyRequest.  # noqa: E501


        :return: The billing_address of this ScoreOnlyRequest.  # noqa: E501
        :rtype: BillingAddress
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this ScoreOnlyRequest.


        :param billing_address: The billing_address of this ScoreOnlyRequest.  # noqa: E501
        :type: BillingAddress
        """

        self._billing_address = billing_address

    @property
    def device(self):
        """Gets the device of this ScoreOnlyRequest.  # noqa: E501


        :return: The device of this ScoreOnlyRequest.  # noqa: E501
        :rtype: Device
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this ScoreOnlyRequest.


        :param device: The device of this ScoreOnlyRequest.  # noqa: E501
        :type: Device
        """

        self._device = device

    @property
    def loyalty(self):
        """Gets the loyalty of this ScoreOnlyRequest.  # noqa: E501


        :return: The loyalty of this ScoreOnlyRequest.  # noqa: E501
        :rtype: Loyalty
        """
        return self._loyalty

    @loyalty.setter
    def loyalty(self, loyalty):
        """Sets the loyalty of this ScoreOnlyRequest.


        :param loyalty: The loyalty of this ScoreOnlyRequest.  # noqa: E501
        :type: Loyalty
        """

        self._loyalty = loyalty

    @property
    def payment(self):
        """Gets the payment of this ScoreOnlyRequest.  # noqa: E501


        :return: The payment of this ScoreOnlyRequest.  # noqa: E501
        :rtype: Payment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this ScoreOnlyRequest.


        :param payment: The payment of this ScoreOnlyRequest.  # noqa: E501
        :type: Payment
        """
        if payment is None:
            raise ValueError("Invalid value for `payment`, must not be `None`")  # noqa: E501

        self._payment = payment

    @property
    def merchant(self):
        """Gets the merchant of this ScoreOnlyRequest.  # noqa: E501


        :return: The merchant of this ScoreOnlyRequest.  # noqa: E501
        :rtype: Merchant
        """
        return self._merchant

    @merchant.setter
    def merchant(self, merchant):
        """Sets the merchant of this ScoreOnlyRequest.


        :param merchant: The merchant of this ScoreOnlyRequest.  # noqa: E501
        :type: Merchant
        """
        if merchant is None:
            raise ValueError("Invalid value for `merchant`, must not be `None`")  # noqa: E501

        self._merchant = merchant

    @property
    def order(self):
        """Gets the order of this ScoreOnlyRequest.  # noqa: E501


        :return: The order of this ScoreOnlyRequest.  # noqa: E501
        :rtype: FraudOrder
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ScoreOnlyRequest.


        :param order: The order of this ScoreOnlyRequest.  # noqa: E501
        :type: FraudOrder
        """

        self._order = order

    @property
    def user_defined(self):
        """Gets the user_defined of this ScoreOnlyRequest.  # noqa: E501

        A JSON object that can carry any additional information that might be helpful for fraud detection.  # noqa: E501

        :return: The user_defined of this ScoreOnlyRequest.  # noqa: E501
        :rtype: object
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this ScoreOnlyRequest.

        A JSON object that can carry any additional information that might be helpful for fraud detection.  # noqa: E501

        :param user_defined: The user_defined of this ScoreOnlyRequest.  # noqa: E501
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
        if not isinstance(other, ScoreOnlyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
