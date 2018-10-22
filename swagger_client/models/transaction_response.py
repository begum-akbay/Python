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
from swagger_client.models.processor_data import ProcessorData  # noqa: F401,E501
from swagger_client.models.response_type import ResponseType  # noqa: F401,E501
from swagger_client.models.transaction_response_authentication_redirect import TransactionResponseAuthenticationRedirect  # noqa: F401,E501
from swagger_client.models.transaction_type import TransactionType  # noqa: F401,E501


class TransactionResponse(object):
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
        'response_type': 'ResponseType',
        'client_request_id': 'str',
        'api_trace_id': 'str',
        'ipg_transaction_id': 'str',
        'order_id': 'str',
        'transaction_type': 'TransactionType',
        'authorization_code': 'str',
        'avs_response': 'str',
        'security_code_response': 'str',
        'brand': 'str',
        'country': 'str',
        'terminal_id': 'str',
        'client_transaction_id': 'str',
        'transaction_time': 'int',
        'approved_amount': 'Amount',
        'transaction_status': 'str',
        'transaction_state': 'str',
        'authentication_redirect': 'TransactionResponseAuthenticationRedirect',
        'scheme_transaction_id': 'str',
        'processor': 'ProcessorData'
    }

    attribute_map = {
        'response_type': 'responseType',
        'client_request_id': 'clientRequestId',
        'api_trace_id': 'apiTraceId',
        'ipg_transaction_id': 'ipgTransactionId',
        'order_id': 'orderId',
        'transaction_type': 'transactionType',
        'authorization_code': 'authorizationCode',
        'avs_response': 'avsResponse',
        'security_code_response': 'securityCodeResponse',
        'brand': 'brand',
        'country': 'country',
        'terminal_id': 'terminalId',
        'client_transaction_id': 'clientTransactionId',
        'transaction_time': 'transactionTime',
        'approved_amount': 'approvedAmount',
        'transaction_status': 'transactionStatus',
        'transaction_state': 'transactionState',
        'authentication_redirect': 'authenticationRedirect',
        'scheme_transaction_id': 'schemeTransactionId',
        'processor': 'processor'
    }

    def __init__(self, response_type=None, client_request_id=None, api_trace_id=None, ipg_transaction_id=None, order_id=None, transaction_type=None, authorization_code=None, avs_response=None, security_code_response=None, brand=None, country=None, terminal_id=None, client_transaction_id=None, transaction_time=None, approved_amount=None, transaction_status=None, transaction_state=None, authentication_redirect=None, scheme_transaction_id=None, processor=None):  # noqa: E501
        """TransactionResponse - a model defined in Swagger"""  # noqa: E501

        self._response_type = None
        self._client_request_id = None
        self._api_trace_id = None
        self._ipg_transaction_id = None
        self._order_id = None
        self._transaction_type = None
        self._authorization_code = None
        self._avs_response = None
        self._security_code_response = None
        self._brand = None
        self._country = None
        self._terminal_id = None
        self._client_transaction_id = None
        self._transaction_time = None
        self._approved_amount = None
        self._transaction_status = None
        self._transaction_state = None
        self._authentication_redirect = None
        self._scheme_transaction_id = None
        self._processor = None
        self.discriminator = None

        if response_type is not None:
            self.response_type = response_type
        if client_request_id is not None:
            self.client_request_id = client_request_id
        if api_trace_id is not None:
            self.api_trace_id = api_trace_id
        if ipg_transaction_id is not None:
            self.ipg_transaction_id = ipg_transaction_id
        if order_id is not None:
            self.order_id = order_id
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if authorization_code is not None:
            self.authorization_code = authorization_code
        if avs_response is not None:
            self.avs_response = avs_response
        if security_code_response is not None:
            self.security_code_response = security_code_response
        if brand is not None:
            self.brand = brand
        if country is not None:
            self.country = country
        if terminal_id is not None:
            self.terminal_id = terminal_id
        if client_transaction_id is not None:
            self.client_transaction_id = client_transaction_id
        if transaction_time is not None:
            self.transaction_time = transaction_time
        if approved_amount is not None:
            self.approved_amount = approved_amount
        if transaction_status is not None:
            self.transaction_status = transaction_status
        if transaction_state is not None:
            self.transaction_state = transaction_state
        if authentication_redirect is not None:
            self.authentication_redirect = authentication_redirect
        if scheme_transaction_id is not None:
            self.scheme_transaction_id = scheme_transaction_id
        if processor is not None:
            self.processor = processor

    @property
    def response_type(self):
        """Gets the response_type of this TransactionResponse.  # noqa: E501

        The schema type returned in the response.  # noqa: E501

        :return: The response_type of this TransactionResponse.  # noqa: E501
        :rtype: ResponseType
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this TransactionResponse.

        The schema type returned in the response.  # noqa: E501

        :param response_type: The response_type of this TransactionResponse.  # noqa: E501
        :type: ResponseType
        """

        self._response_type = response_type

    @property
    def client_request_id(self):
        """Gets the client_request_id of this TransactionResponse.  # noqa: E501

        Echoes back the value in the Request header  # noqa: E501

        :return: The client_request_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this TransactionResponse.

        Echoes back the value in the Request header  # noqa: E501

        :param client_request_id: The client_request_id of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._client_request_id = client_request_id

    @property
    def api_trace_id(self):
        """Gets the api_trace_id of this TransactionResponse.  # noqa: E501

        Echoes back the value in the Request header  # noqa: E501

        :return: The api_trace_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_trace_id

    @api_trace_id.setter
    def api_trace_id(self, api_trace_id):
        """Sets the api_trace_id of this TransactionResponse.

        Echoes back the value in the Request header  # noqa: E501

        :param api_trace_id: The api_trace_id of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._api_trace_id = api_trace_id

    @property
    def ipg_transaction_id(self):
        """Gets the ipg_transaction_id of this TransactionResponse.  # noqa: E501

        The Response Transaction ID  # noqa: E501

        :return: The ipg_transaction_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._ipg_transaction_id

    @ipg_transaction_id.setter
    def ipg_transaction_id(self, ipg_transaction_id):
        """Sets the ipg_transaction_id of this TransactionResponse.

        The Response Transaction ID  # noqa: E501

        :param ipg_transaction_id: The ipg_transaction_id of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._ipg_transaction_id = ipg_transaction_id

    @property
    def order_id(self):
        """Gets the order_id of this TransactionResponse.  # noqa: E501

        Client Order ID if supplied by client, otherwise the Order ID  # noqa: E501

        :return: The order_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this TransactionResponse.

        Client Order ID if supplied by client, otherwise the Order ID  # noqa: E501

        :param order_id: The order_id of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def transaction_type(self):
        """Gets the transaction_type of this TransactionResponse.  # noqa: E501


        :return: The transaction_type of this TransactionResponse.  # noqa: E501
        :rtype: TransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this TransactionResponse.


        :param transaction_type: The transaction_type of this TransactionResponse.  # noqa: E501
        :type: TransactionType
        """

        self._transaction_type = transaction_type

    @property
    def authorization_code(self):
        """Gets the authorization_code of this TransactionResponse.  # noqa: E501

        The processor approval code for compliance.  # noqa: E501

        :return: The authorization_code of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._authorization_code

    @authorization_code.setter
    def authorization_code(self, authorization_code):
        """Sets the authorization_code of this TransactionResponse.

        The processor approval code for compliance.  # noqa: E501

        :param authorization_code: The authorization_code of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._authorization_code = authorization_code

    @property
    def avs_response(self):
        """Gets the avs_response of this TransactionResponse.  # noqa: E501

        The processor address validation response for compliance.  # noqa: E501

        :return: The avs_response of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._avs_response

    @avs_response.setter
    def avs_response(self, avs_response):
        """Sets the avs_response of this TransactionResponse.

        The processor address validation response for compliance.  # noqa: E501

        :param avs_response: The avs_response of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._avs_response = avs_response

    @property
    def security_code_response(self):
        """Gets the security_code_response of this TransactionResponse.  # noqa: E501

        The processor card verification validation response for compliance.  # noqa: E501

        :return: The security_code_response of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._security_code_response

    @security_code_response.setter
    def security_code_response(self, security_code_response):
        """Sets the security_code_response of this TransactionResponse.

        The processor card verification validation response for compliance.  # noqa: E501

        :param security_code_response: The security_code_response of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._security_code_response = security_code_response

    @property
    def brand(self):
        """Gets the brand of this TransactionResponse.  # noqa: E501

        Card brand of the payment instrument  # noqa: E501

        :return: The brand of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this TransactionResponse.

        Card brand of the payment instrument  # noqa: E501

        :param brand: The brand of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def country(self):
        """Gets the country of this TransactionResponse.  # noqa: E501

        Country of the card issuer  # noqa: E501

        :return: The country of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this TransactionResponse.

        Country of the card issuer  # noqa: E501

        :param country: The country of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def terminal_id(self):
        """Gets the terminal_id of this TransactionResponse.  # noqa: E501

        The terminal that is processing the transaction  # noqa: E501

        :return: The terminal_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """Sets the terminal_id of this TransactionResponse.

        The terminal that is processing the transaction  # noqa: E501

        :param terminal_id: The terminal_id of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._terminal_id = terminal_id

    @property
    def client_transaction_id(self):
        """Gets the client_transaction_id of this TransactionResponse.  # noqa: E501

        The unique client Transaction ID from the Request header, if supplied  # noqa: E501

        :return: The client_transaction_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_transaction_id

    @client_transaction_id.setter
    def client_transaction_id(self, client_transaction_id):
        """Sets the client_transaction_id of this TransactionResponse.

        The unique client Transaction ID from the Request header, if supplied  # noqa: E501

        :param client_transaction_id: The client_transaction_id of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._client_transaction_id = client_transaction_id

    @property
    def transaction_time(self):
        """Gets the transaction_time of this TransactionResponse.  # noqa: E501

        The transaction time in seconds since Epoch  # noqa: E501

        :return: The transaction_time of this TransactionResponse.  # noqa: E501
        :rtype: int
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """Sets the transaction_time of this TransactionResponse.

        The transaction time in seconds since Epoch  # noqa: E501

        :param transaction_time: The transaction_time of this TransactionResponse.  # noqa: E501
        :type: int
        """

        self._transaction_time = transaction_time

    @property
    def approved_amount(self):
        """Gets the approved_amount of this TransactionResponse.  # noqa: E501


        :return: The approved_amount of this TransactionResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._approved_amount

    @approved_amount.setter
    def approved_amount(self, approved_amount):
        """Sets the approved_amount of this TransactionResponse.


        :param approved_amount: The approved_amount of this TransactionResponse.  # noqa: E501
        :type: Amount
        """

        self._approved_amount = approved_amount

    @property
    def transaction_status(self):
        """Gets the transaction_status of this TransactionResponse.  # noqa: E501

        The status of the transaction. APPROVED/WAITING are returned by the endpoints.  VALIDATION_FAILED/DECLINED are errors. See ErrorResponse object for details.  # noqa: E501

        :return: The transaction_status of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status):
        """Sets the transaction_status of this TransactionResponse.

        The status of the transaction. APPROVED/WAITING are returned by the endpoints.  VALIDATION_FAILED/DECLINED are errors. See ErrorResponse object for details.  # noqa: E501

        :param transaction_status: The transaction_status of this TransactionResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["APPROVED", "WAITING", "VALIDATION_FAILED", "DECLINED"]  # noqa: E501
        if transaction_status not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_status` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_status, allowed_values)
            )

        self._transaction_status = transaction_status

    @property
    def transaction_state(self):
        """Gets the transaction_state of this TransactionResponse.  # noqa: E501

        The state of the transaction.  # noqa: E501

        :return: The transaction_state of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._transaction_state

    @transaction_state.setter
    def transaction_state(self, transaction_state):
        """Sets the transaction_state of this TransactionResponse.

        The state of the transaction.  # noqa: E501

        :param transaction_state: The transaction_state of this TransactionResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTHORIZED", "CAPTURED", "COMPLETED_GET", "DECLINED", "CHECKED", "INITIALIZED", "PENDING_AUTHORIZATION", "PENDING_AUTOVOID", "PENDING_CAPTURE", "PENDING_CREDIT", "PENDING_GIROPAY_INIT", "PENDING_IDEAL_INIT", "PENDING_INIT", "PENDING_READY", "PENDING_RETURN", "PENDING_SETTLEMENT", "PENDING_SOFORT_INIT", "PENDING_VOID", "READY", "SETTLED", "VOIDED", "WAITING", "WAITING_AUTHENTICATION", "WAITING_3D_SECURE", "WAITING_CLICK_AND_BUY", "WAITING_GIROPAY", "WAITING_IDEAL", "WAITING_KLARNA", "WAITING_PAYPAL", "WAITING_PAYPAL_EVENT", "WAITING_PPRO_LONG_WAITING", "WAITING_SOFORT", "WAITING_T_PAY", "WAITING_ALIPAY_PAYSECURE"]  # noqa: E501
        if transaction_state not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_state` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_state, allowed_values)
            )

        self._transaction_state = transaction_state

    @property
    def authentication_redirect(self):
        """Gets the authentication_redirect of this TransactionResponse.  # noqa: E501


        :return: The authentication_redirect of this TransactionResponse.  # noqa: E501
        :rtype: TransactionResponseAuthenticationRedirect
        """
        return self._authentication_redirect

    @authentication_redirect.setter
    def authentication_redirect(self, authentication_redirect):
        """Sets the authentication_redirect of this TransactionResponse.


        :param authentication_redirect: The authentication_redirect of this TransactionResponse.  # noqa: E501
        :type: TransactionResponseAuthenticationRedirect
        """

        self._authentication_redirect = authentication_redirect

    @property
    def scheme_transaction_id(self):
        """Gets the scheme_transaction_id of this TransactionResponse.  # noqa: E501

        The transaction id received from schemes for the initial transaction, returned for the transactions marked as \"FIRST\"  # noqa: E501

        :return: The scheme_transaction_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._scheme_transaction_id

    @scheme_transaction_id.setter
    def scheme_transaction_id(self, scheme_transaction_id):
        """Sets the scheme_transaction_id of this TransactionResponse.

        The transaction id received from schemes for the initial transaction, returned for the transactions marked as \"FIRST\"  # noqa: E501

        :param scheme_transaction_id: The scheme_transaction_id of this TransactionResponse.  # noqa: E501
        :type: str
        """
        if scheme_transaction_id is not None and len(scheme_transaction_id) > 40:
            raise ValueError("Invalid value for `scheme_transaction_id`, length must be less than or equal to `40`")  # noqa: E501

        self._scheme_transaction_id = scheme_transaction_id

    @property
    def processor(self):
        """Gets the processor of this TransactionResponse.  # noqa: E501


        :return: The processor of this TransactionResponse.  # noqa: E501
        :rtype: ProcessorData
        """
        return self._processor

    @processor.setter
    def processor(self, processor):
        """Sets the processor of this TransactionResponse.


        :param processor: The processor of this TransactionResponse.  # noqa: E501
        :type: ProcessorData
        """

        self._processor = processor

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
        if not isinstance(other, TransactionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
