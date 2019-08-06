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


class RecurringPaymentDetails(object):
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
        'purchase_order_number': 'str',
        'invoice_number': 'str',
        'creation_date': 'str',
        'start_date': 'str',
        'next_attempt_date': 'str',
        'transaction_amount': 'Amount',
        'payment_method_details': 'PaymentMethodDetails',
        'frequency': 'Frequency',
        'number_of_payments': 'int',
        'run_count': 'int',
        'state': 'str',
        'comments': 'str'
    }

    attribute_map = {
        'store_id': 'storeId',
        'purchase_order_number': 'purchaseOrderNumber',
        'invoice_number': 'invoiceNumber',
        'creation_date': 'creationDate',
        'start_date': 'startDate',
        'next_attempt_date': 'nextAttemptDate',
        'transaction_amount': 'transactionAmount',
        'payment_method_details': 'paymentMethodDetails',
        'frequency': 'frequency',
        'number_of_payments': 'numberOfPayments',
        'run_count': 'runCount',
        'state': 'state',
        'comments': 'comments'
    }

    def __init__(self, store_id=None, purchase_order_number=None, invoice_number=None, creation_date=None, start_date=None, next_attempt_date=None, transaction_amount=None, payment_method_details=None, frequency=None, number_of_payments=None, run_count=None, state=None, comments=None):  # noqa: E501
        """RecurringPaymentDetails - a model defined in OpenAPI"""  # noqa: E501

        self._store_id = None
        self._purchase_order_number = None
        self._invoice_number = None
        self._creation_date = None
        self._start_date = None
        self._next_attempt_date = None
        self._transaction_amount = None
        self._payment_method_details = None
        self._frequency = None
        self._number_of_payments = None
        self._run_count = None
        self._state = None
        self._comments = None
        self.discriminator = None

        if store_id is not None:
            self.store_id = store_id
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if creation_date is not None:
            self.creation_date = creation_date
        if start_date is not None:
            self.start_date = start_date
        if next_attempt_date is not None:
            self.next_attempt_date = next_attempt_date
        if transaction_amount is not None:
            self.transaction_amount = transaction_amount
        if payment_method_details is not None:
            self.payment_method_details = payment_method_details
        if frequency is not None:
            self.frequency = frequency
        if number_of_payments is not None:
            self.number_of_payments = number_of_payments
        if run_count is not None:
            self.run_count = run_count
        if state is not None:
            self.state = state
        if comments is not None:
            self.comments = comments

    @property
    def store_id(self):
        """Gets the store_id of this RecurringPaymentDetails.  # noqa: E501

        Store ID number.  # noqa: E501

        :return: The store_id of this RecurringPaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this RecurringPaymentDetails.

        Store ID number.  # noqa: E501

        :param store_id: The store_id of this RecurringPaymentDetails.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this RecurringPaymentDetails.  # noqa: E501

        Purchase order number.  # noqa: E501

        :return: The purchase_order_number of this RecurringPaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this RecurringPaymentDetails.

        Purchase order number.  # noqa: E501

        :param purchase_order_number: The purchase_order_number of this RecurringPaymentDetails.  # noqa: E501
        :type: str
        """

        self._purchase_order_number = purchase_order_number

    @property
    def invoice_number(self):
        """Gets the invoice_number of this RecurringPaymentDetails.  # noqa: E501

        Invoice number.  # noqa: E501

        :return: The invoice_number of this RecurringPaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this RecurringPaymentDetails.

        Invoice number.  # noqa: E501

        :param invoice_number: The invoice_number of this RecurringPaymentDetails.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def creation_date(self):
        """Gets the creation_date of this RecurringPaymentDetails.  # noqa: E501

        Date recurring payment was created.  # noqa: E501

        :return: The creation_date of this RecurringPaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this RecurringPaymentDetails.

        Date recurring payment was created.  # noqa: E501

        :param creation_date: The creation_date of this RecurringPaymentDetails.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

    @property
    def start_date(self):
        """Gets the start_date of this RecurringPaymentDetails.  # noqa: E501

        Date of mandate signature.  # noqa: E501

        :return: The start_date of this RecurringPaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this RecurringPaymentDetails.

        Date of mandate signature.  # noqa: E501

        :param start_date: The start_date of this RecurringPaymentDetails.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def next_attempt_date(self):
        """Gets the next_attempt_date of this RecurringPaymentDetails.  # noqa: E501

        Date of next transaction process attempt.  # noqa: E501

        :return: The next_attempt_date of this RecurringPaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._next_attempt_date

    @next_attempt_date.setter
    def next_attempt_date(self, next_attempt_date):
        """Sets the next_attempt_date of this RecurringPaymentDetails.

        Date of next transaction process attempt.  # noqa: E501

        :param next_attempt_date: The next_attempt_date of this RecurringPaymentDetails.  # noqa: E501
        :type: str
        """

        self._next_attempt_date = next_attempt_date

    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this RecurringPaymentDetails.  # noqa: E501


        :return: The transaction_amount of this RecurringPaymentDetails.  # noqa: E501
        :rtype: Amount
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this RecurringPaymentDetails.


        :param transaction_amount: The transaction_amount of this RecurringPaymentDetails.  # noqa: E501
        :type: Amount
        """

        self._transaction_amount = transaction_amount

    @property
    def payment_method_details(self):
        """Gets the payment_method_details of this RecurringPaymentDetails.  # noqa: E501


        :return: The payment_method_details of this RecurringPaymentDetails.  # noqa: E501
        :rtype: PaymentMethodDetails
        """
        return self._payment_method_details

    @payment_method_details.setter
    def payment_method_details(self, payment_method_details):
        """Sets the payment_method_details of this RecurringPaymentDetails.


        :param payment_method_details: The payment_method_details of this RecurringPaymentDetails.  # noqa: E501
        :type: PaymentMethodDetails
        """

        self._payment_method_details = payment_method_details

    @property
    def frequency(self):
        """Gets the frequency of this RecurringPaymentDetails.  # noqa: E501


        :return: The frequency of this RecurringPaymentDetails.  # noqa: E501
        :rtype: Frequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this RecurringPaymentDetails.


        :param frequency: The frequency of this RecurringPaymentDetails.  # noqa: E501
        :type: Frequency
        """

        self._frequency = frequency

    @property
    def number_of_payments(self):
        """Gets the number_of_payments of this RecurringPaymentDetails.  # noqa: E501

        Number of times the recurring payment will process.  # noqa: E501

        :return: The number_of_payments of this RecurringPaymentDetails.  # noqa: E501
        :rtype: int
        """
        return self._number_of_payments

    @number_of_payments.setter
    def number_of_payments(self, number_of_payments):
        """Sets the number_of_payments of this RecurringPaymentDetails.

        Number of times the recurring payment will process.  # noqa: E501

        :param number_of_payments: The number_of_payments of this RecurringPaymentDetails.  # noqa: E501
        :type: int
        """
        if number_of_payments is not None and number_of_payments > 999:  # noqa: E501
            raise ValueError("Invalid value for `number_of_payments`, must be a value less than or equal to `999`")  # noqa: E501
        if number_of_payments is not None and number_of_payments < 1:  # noqa: E501
            raise ValueError("Invalid value for `number_of_payments`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_of_payments = number_of_payments

    @property
    def run_count(self):
        """Gets the run_count of this RecurringPaymentDetails.  # noqa: E501

        Times the recurring payment has already run.  # noqa: E501

        :return: The run_count of this RecurringPaymentDetails.  # noqa: E501
        :rtype: int
        """
        return self._run_count

    @run_count.setter
    def run_count(self, run_count):
        """Sets the run_count of this RecurringPaymentDetails.

        Times the recurring payment has already run.  # noqa: E501

        :param run_count: The run_count of this RecurringPaymentDetails.  # noqa: E501
        :type: int
        """
        if run_count is not None and run_count > 999:  # noqa: E501
            raise ValueError("Invalid value for `run_count`, must be a value less than or equal to `999`")  # noqa: E501
        if run_count is not None and run_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `run_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._run_count = run_count

    @property
    def state(self):
        """Gets the state of this RecurringPaymentDetails.  # noqa: E501

        State of the recurring payment.  # noqa: E501

        :return: The state of this RecurringPaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RecurringPaymentDetails.

        State of the recurring payment.  # noqa: E501

        :param state: The state of this RecurringPaymentDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["Installed", "Inactivated", "Cancelled"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def comments(self):
        """Gets the comments of this RecurringPaymentDetails.  # noqa: E501

        User supplied comments.  # noqa: E501

        :return: The comments of this RecurringPaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this RecurringPaymentDetails.

        User supplied comments.  # noqa: E501

        :param comments: The comments of this RecurringPaymentDetails.  # noqa: E501
        :type: str
        """

        self._comments = comments

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
        if not isinstance(other, RecurringPaymentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
