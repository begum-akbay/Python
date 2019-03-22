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


class CardInfoLookupResponse(object):
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
        'card_details': 'list[CardInfo]',
        'request_status': 'str'
    }

    attribute_map = {
        'client_request_id': 'clientRequestId',
        'api_trace_id': 'apiTraceId',
        'response_type': 'responseType',
        'card_details': 'cardDetails',
        'request_status': 'requestStatus'
    }

    def __init__(self, client_request_id=None, api_trace_id=None, response_type=None, card_details=None, request_status=None):  # noqa: E501
        """CardInfoLookupResponse - a model defined in OpenAPI"""  # noqa: E501

        self._client_request_id = None
        self._api_trace_id = None
        self._response_type = None
        self._card_details = None
        self._request_status = None
        self.discriminator = None

        if client_request_id is not None:
            self.client_request_id = client_request_id
        if api_trace_id is not None:
            self.api_trace_id = api_trace_id
        if response_type is not None:
            self.response_type = response_type
        if card_details is not None:
            self.card_details = card_details
        if request_status is not None:
            self.request_status = request_status

    @property
    def client_request_id(self):
        """Gets the client_request_id of this CardInfoLookupResponse.  # noqa: E501

        Echoes back the value in the request header for tracking.  # noqa: E501

        :return: The client_request_id of this CardInfoLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this CardInfoLookupResponse.

        Echoes back the value in the request header for tracking.  # noqa: E501

        :param client_request_id: The client_request_id of this CardInfoLookupResponse.  # noqa: E501
        :type: str
        """

        self._client_request_id = client_request_id

    @property
    def api_trace_id(self):
        """Gets the api_trace_id of this CardInfoLookupResponse.  # noqa: E501

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :return: The api_trace_id of this CardInfoLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_trace_id

    @api_trace_id.setter
    def api_trace_id(self, api_trace_id):
        """Sets the api_trace_id of this CardInfoLookupResponse.

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :param api_trace_id: The api_trace_id of this CardInfoLookupResponse.  # noqa: E501
        :type: str
        """

        self._api_trace_id = api_trace_id

    @property
    def response_type(self):
        """Gets the response_type of this CardInfoLookupResponse.  # noqa: E501


        :return: The response_type of this CardInfoLookupResponse.  # noqa: E501
        :rtype: ResponseType
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this CardInfoLookupResponse.


        :param response_type: The response_type of this CardInfoLookupResponse.  # noqa: E501
        :type: ResponseType
        """

        self._response_type = response_type

    @property
    def card_details(self):
        """Gets the card_details of this CardInfoLookupResponse.  # noqa: E501

        One or more card information retrieved based on BIN.  # noqa: E501

        :return: The card_details of this CardInfoLookupResponse.  # noqa: E501
        :rtype: list[CardInfo]
        """
        return self._card_details

    @card_details.setter
    def card_details(self, card_details):
        """Sets the card_details of this CardInfoLookupResponse.

        One or more card information retrieved based on BIN.  # noqa: E501

        :param card_details: The card_details of this CardInfoLookupResponse.  # noqa: E501
        :type: list[CardInfo]
        """

        self._card_details = card_details

    @property
    def request_status(self):
        """Gets the request_status of this CardInfoLookupResponse.  # noqa: E501

        Request status.  # noqa: E501

        :return: The request_status of this CardInfoLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_status

    @request_status.setter
    def request_status(self, request_status):
        """Sets the request_status of this CardInfoLookupResponse.

        Request status.  # noqa: E501

        :param request_status: The request_status of this CardInfoLookupResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "LIST_EMPTY"]  # noqa: E501
        if request_status not in allowed_values:
            raise ValueError(
                "Invalid value for `request_status` ({0}), must be one of {1}"  # noqa: E501
                .format(request_status, allowed_values)
            )

        self._request_status = request_status

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
        if not isinstance(other, CardInfoLookupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
