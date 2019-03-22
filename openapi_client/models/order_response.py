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


class OrderResponse(object):
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
        'client_request_id': 'str',
        'api_trace_id': 'str',
        'response_type': 'ResponseType',
        'ipg_transaction_id': 'str',
        'order_id': 'str',
        'transaction_time': 'int',
        'billing': 'Billing',
        'shipping': 'Shipping',
        'mandate': 'SepaMandate',
        'transactions': 'list[Transaction]',
        'processor': 'ProcessorData'
    }

    attribute_map = {
        'client_request_id': 'clientRequestId',
        'api_trace_id': 'apiTraceId',
        'response_type': 'responseType',
        'ipg_transaction_id': 'ipgTransactionId',
        'order_id': 'orderId',
        'transaction_time': 'transactionTime',
        'billing': 'billing',
        'shipping': 'shipping',
        'mandate': 'mandate',
        'transactions': 'transactions',
        'processor': 'processor'
    }

    def __init__(self, client_request_id=None, api_trace_id=None, response_type=None, ipg_transaction_id=None, order_id=None, transaction_time=None, billing=None, shipping=None, mandate=None, transactions=None, processor=None):  # noqa: E501
        """OrderResponse - a model defined in OpenAPI"""  # noqa: E501

        self._client_request_id = None
        self._api_trace_id = None
        self._response_type = None
        self._ipg_transaction_id = None
        self._order_id = None
        self._transaction_time = None
        self._billing = None
        self._shipping = None
        self._mandate = None
        self._transactions = None
        self._processor = None
        self.discriminator = None

        if client_request_id is not None:
            self.client_request_id = client_request_id
        if api_trace_id is not None:
            self.api_trace_id = api_trace_id
        if response_type is not None:
            self.response_type = response_type
        if ipg_transaction_id is not None:
            self.ipg_transaction_id = ipg_transaction_id
        if order_id is not None:
            self.order_id = order_id
        if transaction_time is not None:
            self.transaction_time = transaction_time
        if billing is not None:
            self.billing = billing
        if shipping is not None:
            self.shipping = shipping
        if mandate is not None:
            self.mandate = mandate
        if transactions is not None:
            self.transactions = transactions
        if processor is not None:
            self.processor = processor

    @property
    def client_request_id(self):
        """Gets the client_request_id of this OrderResponse.  # noqa: E501

        Echoes back the value in the request header for tracking.  # noqa: E501

        :return: The client_request_id of this OrderResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this OrderResponse.

        Echoes back the value in the request header for tracking.  # noqa: E501

        :param client_request_id: The client_request_id of this OrderResponse.  # noqa: E501
        :type: str
        """

        self._client_request_id = client_request_id

    @property
    def api_trace_id(self):
        """Gets the api_trace_id of this OrderResponse.  # noqa: E501

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :return: The api_trace_id of this OrderResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_trace_id

    @api_trace_id.setter
    def api_trace_id(self, api_trace_id):
        """Sets the api_trace_id of this OrderResponse.

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :param api_trace_id: The api_trace_id of this OrderResponse.  # noqa: E501
        :type: str
        """

        self._api_trace_id = api_trace_id

    @property
    def response_type(self):
        """Gets the response_type of this OrderResponse.  # noqa: E501


        :return: The response_type of this OrderResponse.  # noqa: E501
        :rtype: ResponseType
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this OrderResponse.


        :param response_type: The response_type of this OrderResponse.  # noqa: E501
        :type: ResponseType
        """

        self._response_type = response_type

    @property
    def ipg_transaction_id(self):
        """Gets the ipg_transaction_id of this OrderResponse.  # noqa: E501

        The response transaction ID  # noqa: E501

        :return: The ipg_transaction_id of this OrderResponse.  # noqa: E501
        :rtype: str
        """
        return self._ipg_transaction_id

    @ipg_transaction_id.setter
    def ipg_transaction_id(self, ipg_transaction_id):
        """Sets the ipg_transaction_id of this OrderResponse.

        The response transaction ID  # noqa: E501

        :param ipg_transaction_id: The ipg_transaction_id of this OrderResponse.  # noqa: E501
        :type: str
        """

        self._ipg_transaction_id = ipg_transaction_id

    @property
    def order_id(self):
        """Gets the order_id of this OrderResponse.  # noqa: E501

        Client order ID if supplied by client, otherwise the order ID  # noqa: E501

        :return: The order_id of this OrderResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderResponse.

        Client order ID if supplied by client, otherwise the order ID  # noqa: E501

        :param order_id: The order_id of this OrderResponse.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def transaction_time(self):
        """Gets the transaction_time of this OrderResponse.  # noqa: E501

        The transaction time in seconds since Epoch  # noqa: E501

        :return: The transaction_time of this OrderResponse.  # noqa: E501
        :rtype: int
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """Sets the transaction_time of this OrderResponse.

        The transaction time in seconds since Epoch  # noqa: E501

        :param transaction_time: The transaction_time of this OrderResponse.  # noqa: E501
        :type: int
        """

        self._transaction_time = transaction_time

    @property
    def billing(self):
        """Gets the billing of this OrderResponse.  # noqa: E501


        :return: The billing of this OrderResponse.  # noqa: E501
        :rtype: Billing
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this OrderResponse.


        :param billing: The billing of this OrderResponse.  # noqa: E501
        :type: Billing
        """

        self._billing = billing

    @property
    def shipping(self):
        """Gets the shipping of this OrderResponse.  # noqa: E501


        :return: The shipping of this OrderResponse.  # noqa: E501
        :rtype: Shipping
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this OrderResponse.


        :param shipping: The shipping of this OrderResponse.  # noqa: E501
        :type: Shipping
        """

        self._shipping = shipping

    @property
    def mandate(self):
        """Gets the mandate of this OrderResponse.  # noqa: E501


        :return: The mandate of this OrderResponse.  # noqa: E501
        :rtype: SepaMandate
        """
        return self._mandate

    @mandate.setter
    def mandate(self, mandate):
        """Sets the mandate of this OrderResponse.


        :param mandate: The mandate of this OrderResponse.  # noqa: E501
        :type: SepaMandate
        """

        self._mandate = mandate

    @property
    def transactions(self):
        """Gets the transactions of this OrderResponse.  # noqa: E501

        Required for some payment methods (for example, Klarna)  # noqa: E501

        :return: The transactions of this OrderResponse.  # noqa: E501
        :rtype: list[Transaction]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this OrderResponse.

        Required for some payment methods (for example, Klarna)  # noqa: E501

        :param transactions: The transactions of this OrderResponse.  # noqa: E501
        :type: list[Transaction]
        """

        self._transactions = transactions

    @property
    def processor(self):
        """Gets the processor of this OrderResponse.  # noqa: E501


        :return: The processor of this OrderResponse.  # noqa: E501
        :rtype: ProcessorData
        """
        return self._processor

    @processor.setter
    def processor(self, processor):
        """Sets the processor of this OrderResponse.


        :param processor: The processor of this OrderResponse.  # noqa: E501
        :type: ProcessorData
        """

        self._processor = processor

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
        if not isinstance(other, OrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
