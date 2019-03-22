# coding: utf-8

"""
    Payment Gateway API Specification.

    Payment Gateway API for payment processing. Version 6.4.0.20181018.001   # noqa: E501

    OpenAPI spec version: 6.4.0.20181018.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PaymentUrlRequest(object):
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
        'store_id': 'str',
        'client_locale': 'ClientLocale',
        'amount': 'Amount',
        'transaction_type': 'TransactionType',
        'order_id': 'str',
        'billing': 'Billing',
        'shipping': 'Shipping',
        'transaction_notification_url': 'str',
        'expiration': 'int',
        'authenticate_transaction': 'bool',
        'dynamic_merchant_name': 'str',
        'invoice_number': 'str',
        'purchase_order_number': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'store_id': 'storeId',
        'client_locale': 'clientLocale',
        'amount': 'amount',
        'transaction_type': 'transactionType',
        'order_id': 'orderId',
        'billing': 'billing',
        'shipping': 'shipping',
        'transaction_notification_url': 'transactionNotificationURL',
        'expiration': 'expiration',
        'authenticate_transaction': 'authenticateTransaction',
        'dynamic_merchant_name': 'dynamicMerchantName',
        'invoice_number': 'invoiceNumber',
        'purchase_order_number': 'purchaseOrderNumber',
        'ip': 'ip'
    }

    def __init__(self, store_id=None, client_locale=None, amount=None, transaction_type=None, order_id=None, billing=None, shipping=None, transaction_notification_url=None, expiration=None, authenticate_transaction=None, dynamic_merchant_name=None, invoice_number=None, purchase_order_number=None, ip=None):  # noqa: E501
        """PaymentUrlRequest - a model defined in OpenAPI"""  # noqa: E501

        self._store_id = None
        self._client_locale = None
        self._amount = None
        self._transaction_type = None
        self._order_id = None
        self._billing = None
        self._shipping = None
        self._transaction_notification_url = None
        self._expiration = None
        self._authenticate_transaction = None
        self._dynamic_merchant_name = None
        self._invoice_number = None
        self._purchase_order_number = None
        self._ip = None
        self.discriminator = None

        if store_id is not None:
            self.store_id = store_id
        if client_locale is not None:
            self.client_locale = client_locale
        self.amount = amount
        self.transaction_type = transaction_type
        if order_id is not None:
            self.order_id = order_id
        if billing is not None:
            self.billing = billing
        if shipping is not None:
            self.shipping = shipping
        if transaction_notification_url is not None:
            self.transaction_notification_url = transaction_notification_url
        if expiration is not None:
            self.expiration = expiration
        if authenticate_transaction is not None:
            self.authenticate_transaction = authenticate_transaction
        if dynamic_merchant_name is not None:
            self.dynamic_merchant_name = dynamic_merchant_name
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if ip is not None:
            self.ip = ip

    @property
    def store_id(self):
        """Gets the store_id of this PaymentUrlRequest.  # noqa: E501

        An optional Outlet ID for clients that support multiple stores in the same developer app.  # noqa: E501

        :return: The store_id of this PaymentUrlRequest.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this PaymentUrlRequest.

        An optional Outlet ID for clients that support multiple stores in the same developer app.  # noqa: E501

        :param store_id: The store_id of this PaymentUrlRequest.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def client_locale(self):
        """Gets the client_locale of this PaymentUrlRequest.  # noqa: E501


        :return: The client_locale of this PaymentUrlRequest.  # noqa: E501
        :rtype: ClientLocale
        """
        return self._client_locale

    @client_locale.setter
    def client_locale(self, client_locale):
        """Sets the client_locale of this PaymentUrlRequest.


        :param client_locale: The client_locale of this PaymentUrlRequest.  # noqa: E501
        :type: ClientLocale
        """

        self._client_locale = client_locale

    @property
    def amount(self):
        """Gets the amount of this PaymentUrlRequest.  # noqa: E501


        :return: The amount of this PaymentUrlRequest.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentUrlRequest.


        :param amount: The amount of this PaymentUrlRequest.  # noqa: E501
        :type: Amount
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def transaction_type(self):
        """Gets the transaction_type of this PaymentUrlRequest.  # noqa: E501


        :return: The transaction_type of this PaymentUrlRequest.  # noqa: E501
        :rtype: TransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this PaymentUrlRequest.


        :param transaction_type: The transaction_type of this PaymentUrlRequest.  # noqa: E501
        :type: TransactionType
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def order_id(self):
        """Gets the order_id of this PaymentUrlRequest.  # noqa: E501

        Client Order ID if supplied by client, otherwise the Order ID.  # noqa: E501

        :return: The order_id of this PaymentUrlRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PaymentUrlRequest.

        Client Order ID if supplied by client, otherwise the Order ID.  # noqa: E501

        :param order_id: The order_id of this PaymentUrlRequest.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def billing(self):
        """Gets the billing of this PaymentUrlRequest.  # noqa: E501


        :return: The billing of this PaymentUrlRequest.  # noqa: E501
        :rtype: Billing
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this PaymentUrlRequest.


        :param billing: The billing of this PaymentUrlRequest.  # noqa: E501
        :type: Billing
        """

        self._billing = billing

    @property
    def shipping(self):
        """Gets the shipping of this PaymentUrlRequest.  # noqa: E501


        :return: The shipping of this PaymentUrlRequest.  # noqa: E501
        :rtype: Shipping
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this PaymentUrlRequest.


        :param shipping: The shipping of this PaymentUrlRequest.  # noqa: E501
        :type: Shipping
        """

        self._shipping = shipping

    @property
    def transaction_notification_url(self):
        """Gets the transaction_notification_url of this PaymentUrlRequest.  # noqa: E501

        URL for notifying merchant with payment result.  # noqa: E501

        :return: The transaction_notification_url of this PaymentUrlRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction_notification_url

    @transaction_notification_url.setter
    def transaction_notification_url(self, transaction_notification_url):
        """Sets the transaction_notification_url of this PaymentUrlRequest.

        URL for notifying merchant with payment result.  # noqa: E501

        :param transaction_notification_url: The transaction_notification_url of this PaymentUrlRequest.  # noqa: E501
        :type: str
        """

        self._transaction_notification_url = transaction_notification_url

    @property
    def expiration(self):
        """Gets the expiration of this PaymentUrlRequest.  # noqa: E501

        Time until payment URL expires.  # noqa: E501

        :return: The expiration of this PaymentUrlRequest.  # noqa: E501
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this PaymentUrlRequest.

        Time until payment URL expires.  # noqa: E501

        :param expiration: The expiration of this PaymentUrlRequest.  # noqa: E501
        :type: int
        """

        self._expiration = expiration

    @property
    def authenticate_transaction(self):
        """Gets the authenticate_transaction of this PaymentUrlRequest.  # noqa: E501

        If 3D secure should be applied.  # noqa: E501

        :return: The authenticate_transaction of this PaymentUrlRequest.  # noqa: E501
        :rtype: bool
        """
        return self._authenticate_transaction

    @authenticate_transaction.setter
    def authenticate_transaction(self, authenticate_transaction):
        """Sets the authenticate_transaction of this PaymentUrlRequest.

        If 3D secure should be applied.  # noqa: E501

        :param authenticate_transaction: The authenticate_transaction of this PaymentUrlRequest.  # noqa: E501
        :type: bool
        """

        self._authenticate_transaction = authenticate_transaction

    @property
    def dynamic_merchant_name(self):
        """Gets the dynamic_merchant_name of this PaymentUrlRequest.  # noqa: E501

        Dynamic merchant name for the cardholder's statement.  # noqa: E501

        :return: The dynamic_merchant_name of this PaymentUrlRequest.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_merchant_name

    @dynamic_merchant_name.setter
    def dynamic_merchant_name(self, dynamic_merchant_name):
        """Sets the dynamic_merchant_name of this PaymentUrlRequest.

        Dynamic merchant name for the cardholder's statement.  # noqa: E501

        :param dynamic_merchant_name: The dynamic_merchant_name of this PaymentUrlRequest.  # noqa: E501
        :type: str
        """

        self._dynamic_merchant_name = dynamic_merchant_name

    @property
    def invoice_number(self):
        """Gets the invoice_number of this PaymentUrlRequest.  # noqa: E501

        Invoice number.  # noqa: E501

        :return: The invoice_number of this PaymentUrlRequest.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this PaymentUrlRequest.

        Invoice number.  # noqa: E501

        :param invoice_number: The invoice_number of this PaymentUrlRequest.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this PaymentUrlRequest.  # noqa: E501

        Purchase order number.  # noqa: E501

        :return: The purchase_order_number of this PaymentUrlRequest.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this PaymentUrlRequest.

        Purchase order number.  # noqa: E501

        :param purchase_order_number: The purchase_order_number of this PaymentUrlRequest.  # noqa: E501
        :type: str
        """

        self._purchase_order_number = purchase_order_number

    @property
    def ip(self):
        """Gets the ip of this PaymentUrlRequest.  # noqa: E501

        IPv4 or IPv6 network address.  # noqa: E501

        :return: The ip of this PaymentUrlRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this PaymentUrlRequest.

        IPv4 or IPv6 network address.  # noqa: E501

        :param ip: The ip of this PaymentUrlRequest.  # noqa: E501
        :type: str
        """

        self._ip = ip

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
        if not isinstance(other, PaymentUrlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
