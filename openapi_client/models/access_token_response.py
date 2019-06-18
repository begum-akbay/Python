# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    OpenAPI spec version: 6.6.0.20190329.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AccessTokenResponse(object):
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
        'access_token': 'str',
        'client_request_id': 'str',
        'request_status': 'str'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'client_request_id': 'clientRequestId',
        'request_status': 'requestStatus'
    }

    def __init__(self, access_token=None, client_request_id=None, request_status=None):  # noqa: E501
        """AccessTokenResponse - a model defined in OpenAPI"""  # noqa: E501

        self._access_token = None
        self._client_request_id = None
        self._request_status = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if client_request_id is not None:
            self.client_request_id = client_request_id
        if request_status is not None:
            self.request_status = request_status

    @property
    def access_token(self):
        """Gets the access_token of this AccessTokenResponse.  # noqa: E501

        Access token for authentication.  # noqa: E501

        :return: The access_token of this AccessTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this AccessTokenResponse.

        Access token for authentication.  # noqa: E501

        :param access_token: The access_token of this AccessTokenResponse.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def client_request_id(self):
        """Gets the client_request_id of this AccessTokenResponse.  # noqa: E501

        Echoes back the value from the request header for tracking.  # noqa: E501

        :return: The client_request_id of this AccessTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this AccessTokenResponse.

        Echoes back the value from the request header for tracking.  # noqa: E501

        :param client_request_id: The client_request_id of this AccessTokenResponse.  # noqa: E501
        :type: str
        """

        self._client_request_id = client_request_id

    @property
    def request_status(self):
        """Gets the request_status of this AccessTokenResponse.  # noqa: E501

        The result of the requested operation. If this is anything other than 'SUCCESS', please refer to the 400s HTTP error codes. See ErrorResponse object for details.  # noqa: E501

        :return: The request_status of this AccessTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_status

    @request_status.setter
    def request_status(self, request_status):
        """Sets the request_status of this AccessTokenResponse.

        The result of the requested operation. If this is anything other than 'SUCCESS', please refer to the 400s HTTP error codes. See ErrorResponse object for details.  # noqa: E501

        :param request_status: The request_status of this AccessTokenResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS"]  # noqa: E501
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
        if not isinstance(other, AccessTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
