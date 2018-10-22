# coding: utf-8

"""
    Payment Gateway API Specification

    Payment Gateway API for payment processing.   # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.amount import Amount  # noqa: F401,E501
from swagger_client.models.client_locale import ClientLocale  # noqa: F401,E501
from swagger_client.models.frequency import Frequency  # noqa: F401,E501
from swagger_client.models.payment_method import PaymentMethod  # noqa: F401,E501


class PaymentSchedulesRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'store_id': 'str',
        'reference_order_id': 'str',
        'start_date': 'date',
        'number_of_payments': 'int',
        'maximum_failures': 'int',
        'invoice_number': 'str',
        'po_number': 'str',
        'transaction_origin': 'str',
        'dynamic_merchant_name': 'str',
        'frequency': 'Frequency',
        'payment_method': 'PaymentMethod',
        'amount': 'Amount',
        'client_locale': 'ClientLocale',
        'order_id': 'str'
    }

    attribute_map = {
        'store_id': 'storeId',
        'reference_order_id': 'referenceOrderId',
        'start_date': 'startDate',
        'number_of_payments': 'numberOfPayments',
        'maximum_failures': 'maximumFailures',
        'invoice_number': 'invoiceNumber',
        'po_number': 'poNumber',
        'transaction_origin': 'transactionOrigin',
        'dynamic_merchant_name': 'dynamicMerchantName',
        'frequency': 'frequency',
        'payment_method': 'paymentMethod',
        'amount': 'amount',
        'client_locale': 'clientLocale',
        'order_id': 'orderId'
    }

    def __init__(self, store_id=None, reference_order_id=None, start_date=None, number_of_payments=None, maximum_failures=None, invoice_number=None, po_number=None, transaction_origin=None, dynamic_merchant_name=None, frequency=None, payment_method=None, amount=None, client_locale=None, order_id=None):  # noqa: E501
        """PaymentSchedulesRequest - a model defined in Swagger"""  # noqa: E501

        self._store_id = None
        self._reference_order_id = None
        self._start_date = None
        self._number_of_payments = None
        self._maximum_failures = None
        self._invoice_number = None
        self._po_number = None
        self._transaction_origin = None
        self._dynamic_merchant_name = None
        self._frequency = None
        self._payment_method = None
        self._amount = None
        self._client_locale = None
        self._order_id = None
        self.discriminator = None

        if store_id is not None:
            self.store_id = store_id
        if reference_order_id is not None:
            self.reference_order_id = reference_order_id
        if start_date is not None:
            self.start_date = start_date
        if number_of_payments is not None:
            self.number_of_payments = number_of_payments
        if maximum_failures is not None:
            self.maximum_failures = maximum_failures
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if po_number is not None:
            self.po_number = po_number
        if transaction_origin is not None:
            self.transaction_origin = transaction_origin
        if dynamic_merchant_name is not None:
            self.dynamic_merchant_name = dynamic_merchant_name
        if frequency is not None:
            self.frequency = frequency
        if payment_method is not None:
            self.payment_method = payment_method
        if amount is not None:
            self.amount = amount
        if client_locale is not None:
            self.client_locale = client_locale
        if order_id is not None:
            self.order_id = order_id

    @property
    def store_id(self):
        """Gets the store_id of this PaymentSchedulesRequest.  # noqa: E501

        Store ID number.  # noqa: E501

        :return: The store_id of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this PaymentSchedulesRequest.

        Store ID number.  # noqa: E501

        :param store_id: The store_id of this PaymentSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._store_id = store_id

    @property
    def reference_order_id(self):
        """Gets the reference_order_id of this PaymentSchedulesRequest.  # noqa: E501

        Order ID used to create recurring payment from existing transaction.  # noqa: E501

        :return: The reference_order_id of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._reference_order_id

    @reference_order_id.setter
    def reference_order_id(self, reference_order_id):
        """Sets the reference_order_id of this PaymentSchedulesRequest.

        Order ID used to create recurring payment from existing transaction.  # noqa: E501

        :param reference_order_id: The reference_order_id of this PaymentSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._reference_order_id = reference_order_id

    @property
    def start_date(self):
        """Gets the start_date of this PaymentSchedulesRequest.  # noqa: E501

        Date of mandate signature.  # noqa: E501

        :return: The start_date of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PaymentSchedulesRequest.

        Date of mandate signature.  # noqa: E501

        :param start_date: The start_date of this PaymentSchedulesRequest.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def number_of_payments(self):
        """Gets the number_of_payments of this PaymentSchedulesRequest.  # noqa: E501

        Number of times the recurring payment will process.  # noqa: E501

        :return: The number_of_payments of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: int
        """
        return self._number_of_payments

    @number_of_payments.setter
    def number_of_payments(self, number_of_payments):
        """Sets the number_of_payments of this PaymentSchedulesRequest.

        Number of times the recurring payment will process.  # noqa: E501

        :param number_of_payments: The number_of_payments of this PaymentSchedulesRequest.  # noqa: E501
        :type: int
        """
        if number_of_payments is not None and number_of_payments > 999:  # noqa: E501
            raise ValueError("Invalid value for `number_of_payments`, must be a value less than or equal to `999`")  # noqa: E501
        if number_of_payments is not None and number_of_payments < 1:  # noqa: E501
            raise ValueError("Invalid value for `number_of_payments`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_of_payments = number_of_payments

    @property
    def maximum_failures(self):
        """Gets the maximum_failures of this PaymentSchedulesRequest.  # noqa: E501

        Number of failures that can be encountered before re-tries cease.  # noqa: E501

        :return: The maximum_failures of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: int
        """
        return self._maximum_failures

    @maximum_failures.setter
    def maximum_failures(self, maximum_failures):
        """Sets the maximum_failures of this PaymentSchedulesRequest.

        Number of failures that can be encountered before re-tries cease.  # noqa: E501

        :param maximum_failures: The maximum_failures of this PaymentSchedulesRequest.  # noqa: E501
        :type: int
        """
        if maximum_failures is not None and maximum_failures > 999:  # noqa: E501
            raise ValueError("Invalid value for `maximum_failures`, must be a value less than or equal to `999`")  # noqa: E501
        if maximum_failures is not None and maximum_failures < 1:  # noqa: E501
            raise ValueError("Invalid value for `maximum_failures`, must be a value greater than or equal to `1`")  # noqa: E501

        self._maximum_failures = maximum_failures

    @property
    def invoice_number(self):
        """Gets the invoice_number of this PaymentSchedulesRequest.  # noqa: E501

        Invoice number.  # noqa: E501

        :return: The invoice_number of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this PaymentSchedulesRequest.

        Invoice number.  # noqa: E501

        :param invoice_number: The invoice_number of this PaymentSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def po_number(self):
        """Gets the po_number of this PaymentSchedulesRequest.  # noqa: E501

        Purchase order number.  # noqa: E501

        :return: The po_number of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._po_number

    @po_number.setter
    def po_number(self, po_number):
        """Sets the po_number of this PaymentSchedulesRequest.

        Purchase order number.  # noqa: E501

        :param po_number: The po_number of this PaymentSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._po_number = po_number

    @property
    def transaction_origin(self):
        """Gets the transaction_origin of this PaymentSchedulesRequest.  # noqa: E501

        The source of the transaction. The possible values are ECI (if the order was received via email or Internet), MOTO (mail order / telephone order) and RETAIL (face to face).  # noqa: E501

        :return: The transaction_origin of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction_origin

    @transaction_origin.setter
    def transaction_origin(self, transaction_origin):
        """Sets the transaction_origin of this PaymentSchedulesRequest.

        The source of the transaction. The possible values are ECI (if the order was received via email or Internet), MOTO (mail order / telephone order) and RETAIL (face to face).  # noqa: E501

        :param transaction_origin: The transaction_origin of this PaymentSchedulesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ECI", "MOTO", "RETAIL"]  # noqa: E501
        if transaction_origin not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_origin` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_origin, allowed_values)
            )

        self._transaction_origin = transaction_origin

    @property
    def dynamic_merchant_name(self):
        """Gets the dynamic_merchant_name of this PaymentSchedulesRequest.  # noqa: E501

        Dynamic merchant name for the cardholder‘s statement.  # noqa: E501

        :return: The dynamic_merchant_name of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_merchant_name

    @dynamic_merchant_name.setter
    def dynamic_merchant_name(self, dynamic_merchant_name):
        """Sets the dynamic_merchant_name of this PaymentSchedulesRequest.

        Dynamic merchant name for the cardholder‘s statement.  # noqa: E501

        :param dynamic_merchant_name: The dynamic_merchant_name of this PaymentSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._dynamic_merchant_name = dynamic_merchant_name

    @property
    def frequency(self):
        """Gets the frequency of this PaymentSchedulesRequest.  # noqa: E501


        :return: The frequency of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: Frequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this PaymentSchedulesRequest.


        :param frequency: The frequency of this PaymentSchedulesRequest.  # noqa: E501
        :type: Frequency
        """

        self._frequency = frequency

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentSchedulesRequest.  # noqa: E501


        :return: The payment_method of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: PaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentSchedulesRequest.


        :param payment_method: The payment_method of this PaymentSchedulesRequest.  # noqa: E501
        :type: PaymentMethod
        """

        self._payment_method = payment_method

    @property
    def amount(self):
        """Gets the amount of this PaymentSchedulesRequest.  # noqa: E501


        :return: The amount of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentSchedulesRequest.


        :param amount: The amount of this PaymentSchedulesRequest.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def client_locale(self):
        """Gets the client_locale of this PaymentSchedulesRequest.  # noqa: E501


        :return: The client_locale of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: ClientLocale
        """
        return self._client_locale

    @client_locale.setter
    def client_locale(self, client_locale):
        """Sets the client_locale of this PaymentSchedulesRequest.


        :param client_locale: The client_locale of this PaymentSchedulesRequest.  # noqa: E501
        :type: ClientLocale
        """

        self._client_locale = client_locale

    @property
    def order_id(self):
        """Gets the order_id of this PaymentSchedulesRequest.  # noqa: E501

        Client Order ID if supplied by client.  # noqa: E501

        :return: The order_id of this PaymentSchedulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PaymentSchedulesRequest.

        Client Order ID if supplied by client.  # noqa: E501

        :param order_id: The order_id of this PaymentSchedulesRequest.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, PaymentSchedulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
