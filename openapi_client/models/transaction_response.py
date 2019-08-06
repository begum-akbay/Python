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


class TransactionResponse(object):
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
        'transaction_type': 'TransactionType',
        'payment_token': 'PaymentTokenDetails',
        'transaction_origin': 'TransactionOrigin',
        'payment_method_details': 'PaymentMethodDetails',
        'country': 'str',
        'terminal_id': 'str',
        'merchant_transaction_id': 'str',
        'transaction_time': 'int',
        'approved_amount': 'Amount',
        'transaction_status': 'str',
        'transaction_state': 'str',
        'secure3d_response': 'Secure3dResponse',
        'redirect_url': 'str',
        'authentication_redirect': 'AuthenticationRedirect',
        'scheme_transaction_id': 'str',
        'processor': 'ProcessorData',
        'additional_details': 'AdditionalTransactionDetails',
        'account_updater_response': 'AccountUpdaterResponse'
    }

    attribute_map = {
        'client_request_id': 'clientRequestId',
        'api_trace_id': 'apiTraceId',
        'response_type': 'responseType',
        'ipg_transaction_id': 'ipgTransactionId',
        'order_id': 'orderId',
        'transaction_type': 'transactionType',
        'payment_token': 'paymentToken',
        'transaction_origin': 'transactionOrigin',
        'payment_method_details': 'paymentMethodDetails',
        'country': 'country',
        'terminal_id': 'terminalId',
        'merchant_transaction_id': 'merchantTransactionId',
        'transaction_time': 'transactionTime',
        'approved_amount': 'approvedAmount',
        'transaction_status': 'transactionStatus',
        'transaction_state': 'transactionState',
        'secure3d_response': 'secure3dResponse',
        'redirect_url': 'redirectURL',
        'authentication_redirect': 'authenticationRedirect',
        'scheme_transaction_id': 'schemeTransactionId',
        'processor': 'processor',
        'additional_details': 'additionalDetails',
        'account_updater_response': 'accountUpdaterResponse'
    }

    def __init__(self, client_request_id=None, api_trace_id=None, response_type=None, ipg_transaction_id=None, order_id=None, transaction_type=None, payment_token=None, transaction_origin=None, payment_method_details=None, country=None, terminal_id=None, merchant_transaction_id=None, transaction_time=None, approved_amount=None, transaction_status=None, transaction_state=None, secure3d_response=None, redirect_url=None, authentication_redirect=None, scheme_transaction_id=None, processor=None, additional_details=None, account_updater_response=None):  # noqa: E501
        """TransactionResponse - a model defined in OpenAPI"""  # noqa: E501

        self._client_request_id = None
        self._api_trace_id = None
        self._response_type = None
        self._ipg_transaction_id = None
        self._order_id = None
        self._transaction_type = None
        self._payment_token = None
        self._transaction_origin = None
        self._payment_method_details = None
        self._country = None
        self._terminal_id = None
        self._merchant_transaction_id = None
        self._transaction_time = None
        self._approved_amount = None
        self._transaction_status = None
        self._transaction_state = None
        self._secure3d_response = None
        self._redirect_url = None
        self._authentication_redirect = None
        self._scheme_transaction_id = None
        self._processor = None
        self._additional_details = None
        self._account_updater_response = None
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
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if payment_token is not None:
            self.payment_token = payment_token
        if transaction_origin is not None:
            self.transaction_origin = transaction_origin
        if payment_method_details is not None:
            self.payment_method_details = payment_method_details
        if country is not None:
            self.country = country
        if terminal_id is not None:
            self.terminal_id = terminal_id
        if merchant_transaction_id is not None:
            self.merchant_transaction_id = merchant_transaction_id
        if transaction_time is not None:
            self.transaction_time = transaction_time
        if approved_amount is not None:
            self.approved_amount = approved_amount
        if transaction_status is not None:
            self.transaction_status = transaction_status
        if transaction_state is not None:
            self.transaction_state = transaction_state
        if secure3d_response is not None:
            self.secure3d_response = secure3d_response
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if authentication_redirect is not None:
            self.authentication_redirect = authentication_redirect
        if scheme_transaction_id is not None:
            self.scheme_transaction_id = scheme_transaction_id
        if processor is not None:
            self.processor = processor
        if additional_details is not None:
            self.additional_details = additional_details
        if account_updater_response is not None:
            self.account_updater_response = account_updater_response

    @property
    def client_request_id(self):
        """Gets the client_request_id of this TransactionResponse.  # noqa: E501

        Echoes back the value in the request header for tracking.  # noqa: E501

        :return: The client_request_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this TransactionResponse.

        Echoes back the value in the request header for tracking.  # noqa: E501

        :param client_request_id: The client_request_id of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._client_request_id = client_request_id

    @property
    def api_trace_id(self):
        """Gets the api_trace_id of this TransactionResponse.  # noqa: E501

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :return: The api_trace_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_trace_id

    @api_trace_id.setter
    def api_trace_id(self, api_trace_id):
        """Sets the api_trace_id of this TransactionResponse.

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :param api_trace_id: The api_trace_id of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._api_trace_id = api_trace_id

    @property
    def response_type(self):
        """Gets the response_type of this TransactionResponse.  # noqa: E501


        :return: The response_type of this TransactionResponse.  # noqa: E501
        :rtype: ResponseType
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this TransactionResponse.


        :param response_type: The response_type of this TransactionResponse.  # noqa: E501
        :type: ResponseType
        """

        self._response_type = response_type

    @property
    def ipg_transaction_id(self):
        """Gets the ipg_transaction_id of this TransactionResponse.  # noqa: E501

        The response transaction ID.  # noqa: E501

        :return: The ipg_transaction_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._ipg_transaction_id

    @ipg_transaction_id.setter
    def ipg_transaction_id(self, ipg_transaction_id):
        """Sets the ipg_transaction_id of this TransactionResponse.

        The response transaction ID.  # noqa: E501

        :param ipg_transaction_id: The ipg_transaction_id of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._ipg_transaction_id = ipg_transaction_id

    @property
    def order_id(self):
        """Gets the order_id of this TransactionResponse.  # noqa: E501

        Client order ID if supplied by client, otherwise the order ID.  # noqa: E501

        :return: The order_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this TransactionResponse.

        Client order ID if supplied by client, otherwise the order ID.  # noqa: E501

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
    def payment_token(self):
        """Gets the payment_token of this TransactionResponse.  # noqa: E501


        :return: The payment_token of this TransactionResponse.  # noqa: E501
        :rtype: PaymentTokenDetails
        """
        return self._payment_token

    @payment_token.setter
    def payment_token(self, payment_token):
        """Sets the payment_token of this TransactionResponse.


        :param payment_token: The payment_token of this TransactionResponse.  # noqa: E501
        :type: PaymentTokenDetails
        """

        self._payment_token = payment_token

    @property
    def transaction_origin(self):
        """Gets the transaction_origin of this TransactionResponse.  # noqa: E501


        :return: The transaction_origin of this TransactionResponse.  # noqa: E501
        :rtype: TransactionOrigin
        """
        return self._transaction_origin

    @transaction_origin.setter
    def transaction_origin(self, transaction_origin):
        """Sets the transaction_origin of this TransactionResponse.


        :param transaction_origin: The transaction_origin of this TransactionResponse.  # noqa: E501
        :type: TransactionOrigin
        """

        self._transaction_origin = transaction_origin

    @property
    def payment_method_details(self):
        """Gets the payment_method_details of this TransactionResponse.  # noqa: E501


        :return: The payment_method_details of this TransactionResponse.  # noqa: E501
        :rtype: PaymentMethodDetails
        """
        return self._payment_method_details

    @payment_method_details.setter
    def payment_method_details(self, payment_method_details):
        """Sets the payment_method_details of this TransactionResponse.


        :param payment_method_details: The payment_method_details of this TransactionResponse.  # noqa: E501
        :type: PaymentMethodDetails
        """

        self._payment_method_details = payment_method_details

    @property
    def country(self):
        """Gets the country of this TransactionResponse.  # noqa: E501

        Country of the card issuer.  # noqa: E501

        :return: The country of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this TransactionResponse.

        Country of the card issuer.  # noqa: E501

        :param country: The country of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def terminal_id(self):
        """Gets the terminal_id of this TransactionResponse.  # noqa: E501

        The terminal that is processing the transaction.  # noqa: E501

        :return: The terminal_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """Sets the terminal_id of this TransactionResponse.

        The terminal that is processing the transaction.  # noqa: E501

        :param terminal_id: The terminal_id of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._terminal_id = terminal_id

    @property
    def merchant_transaction_id(self):
        """Gets the merchant_transaction_id of this TransactionResponse.  # noqa: E501

        The unique merchant transaction ID from the request header, if supplied.  # noqa: E501

        :return: The merchant_transaction_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_transaction_id

    @merchant_transaction_id.setter
    def merchant_transaction_id(self, merchant_transaction_id):
        """Sets the merchant_transaction_id of this TransactionResponse.

        The unique merchant transaction ID from the request header, if supplied.  # noqa: E501

        :param merchant_transaction_id: The merchant_transaction_id of this TransactionResponse.  # noqa: E501
        :type: str
        """
        if merchant_transaction_id is not None and len(merchant_transaction_id) > 40:
            raise ValueError("Invalid value for `merchant_transaction_id`, length must be less than or equal to `40`")  # noqa: E501

        self._merchant_transaction_id = merchant_transaction_id

    @property
    def transaction_time(self):
        """Gets the transaction_time of this TransactionResponse.  # noqa: E501

        The transaction time in seconds since epoch.  # noqa: E501

        :return: The transaction_time of this TransactionResponse.  # noqa: E501
        :rtype: int
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """Sets the transaction_time of this TransactionResponse.

        The transaction time in seconds since epoch.  # noqa: E501

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
        allowed_values = ["APPROVED", "WAITING", "VALIDATION_FAILED", "PROCESSING_FAILED", "DECLINED"]  # noqa: E501
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
        allowed_values = ["AUTHORIZED", "CAPTURED", "DECLINED", "CHECKED", "COMPLETED_GET", "INITIALIZED", "PENDING", "READY", "TEMPLATE", "SETTLED", "VOIDED", "WAITING"]  # noqa: E501
        if transaction_state not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_state` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_state, allowed_values)
            )

        self._transaction_state = transaction_state

    @property
    def secure3d_response(self):
        """Gets the secure3d_response of this TransactionResponse.  # noqa: E501


        :return: The secure3d_response of this TransactionResponse.  # noqa: E501
        :rtype: Secure3dResponse
        """
        return self._secure3d_response

    @secure3d_response.setter
    def secure3d_response(self, secure3d_response):
        """Sets the secure3d_response of this TransactionResponse.


        :param secure3d_response: The secure3d_response of this TransactionResponse.  # noqa: E501
        :type: Secure3dResponse
        """

        self._secure3d_response = secure3d_response

    @property
    def redirect_url(self):
        """Gets the redirect_url of this TransactionResponse.  # noqa: E501

        The endpoint redirection URL.  # noqa: E501

        :return: The redirect_url of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this TransactionResponse.

        The endpoint redirection URL.  # noqa: E501

        :param redirect_url: The redirect_url of this TransactionResponse.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def authentication_redirect(self):
        """Gets the authentication_redirect of this TransactionResponse.  # noqa: E501


        :return: The authentication_redirect of this TransactionResponse.  # noqa: E501
        :rtype: AuthenticationRedirect
        """
        return self._authentication_redirect

    @authentication_redirect.setter
    def authentication_redirect(self, authentication_redirect):
        """Sets the authentication_redirect of this TransactionResponse.


        :param authentication_redirect: The authentication_redirect of this TransactionResponse.  # noqa: E501
        :type: AuthenticationRedirect
        """

        self._authentication_redirect = authentication_redirect

    @property
    def scheme_transaction_id(self):
        """Gets the scheme_transaction_id of this TransactionResponse.  # noqa: E501

        The transaction ID received from schemes for the initial transaction of card on file flows.  # noqa: E501

        :return: The scheme_transaction_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._scheme_transaction_id

    @scheme_transaction_id.setter
    def scheme_transaction_id(self, scheme_transaction_id):
        """Sets the scheme_transaction_id of this TransactionResponse.

        The transaction ID received from schemes for the initial transaction of card on file flows.  # noqa: E501

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

    @property
    def additional_details(self):
        """Gets the additional_details of this TransactionResponse.  # noqa: E501


        :return: The additional_details of this TransactionResponse.  # noqa: E501
        :rtype: AdditionalTransactionDetails
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """Sets the additional_details of this TransactionResponse.


        :param additional_details: The additional_details of this TransactionResponse.  # noqa: E501
        :type: AdditionalTransactionDetails
        """

        self._additional_details = additional_details

    @property
    def account_updater_response(self):
        """Gets the account_updater_response of this TransactionResponse.  # noqa: E501


        :return: The account_updater_response of this TransactionResponse.  # noqa: E501
        :rtype: AccountUpdaterResponse
        """
        return self._account_updater_response

    @account_updater_response.setter
    def account_updater_response(self, account_updater_response):
        """Sets the account_updater_response of this TransactionResponse.


        :param account_updater_response: The account_updater_response of this TransactionResponse.  # noqa: E501
        :type: AccountUpdaterResponse
        """

        self._account_updater_response = account_updater_response

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
        if not isinstance(other, TransactionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
