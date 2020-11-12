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


class Secure3DAuthenticationResponseParams(object):
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
        'payer_authentication_request': 'str',
        'term_url': 'str',
        'merchant_data': 'str',
        'acs_url': 'str',
        'c_req': 'str',
        'session_data': 'str'
    }

    attribute_map = {
        'payer_authentication_request': 'payerAuthenticationRequest',
        'term_url': 'termURL',
        'merchant_data': 'merchantData',
        'acs_url': 'acsURL',
        'c_req': 'cReq',
        'session_data': 'sessionData'
    }

    def __init__(self, payer_authentication_request=None, term_url=None, merchant_data=None, acs_url=None, c_req=None, session_data=None):  # noqa: E501
        """Secure3DAuthenticationResponseParams - a model defined in OpenAPI"""  # noqa: E501

        self._payer_authentication_request = None
        self._term_url = None
        self._merchant_data = None
        self._acs_url = None
        self._c_req = None
        self._session_data = None
        self.discriminator = None

        if payer_authentication_request is not None:
            self.payer_authentication_request = payer_authentication_request
        if term_url is not None:
            self.term_url = term_url
        if merchant_data is not None:
            self.merchant_data = merchant_data
        if acs_url is not None:
            self.acs_url = acs_url
        if c_req is not None:
            self.c_req = c_req
        if session_data is not None:
            self.session_data = session_data

    @property
    def payer_authentication_request(self):
        """Gets the payer_authentication_request of this Secure3DAuthenticationResponseParams.  # noqa: E501

        Message sent from merchant server to authenticate the cardholder.  # noqa: E501

        :return: The payer_authentication_request of this Secure3DAuthenticationResponseParams.  # noqa: E501
        :rtype: str
        """
        return self._payer_authentication_request

    @payer_authentication_request.setter
    def payer_authentication_request(self, payer_authentication_request):
        """Sets the payer_authentication_request of this Secure3DAuthenticationResponseParams.

        Message sent from merchant server to authenticate the cardholder.  # noqa: E501

        :param payer_authentication_request: The payer_authentication_request of this Secure3DAuthenticationResponseParams.  # noqa: E501
        :type: str
        """

        self._payer_authentication_request = payer_authentication_request

    @property
    def term_url(self):
        """Gets the term_url of this Secure3DAuthenticationResponseParams.  # noqa: E501

        Terminal URL for processing request.  # noqa: E501

        :return: The term_url of this Secure3DAuthenticationResponseParams.  # noqa: E501
        :rtype: str
        """
        return self._term_url

    @term_url.setter
    def term_url(self, term_url):
        """Sets the term_url of this Secure3DAuthenticationResponseParams.

        Terminal URL for processing request.  # noqa: E501

        :param term_url: The term_url of this Secure3DAuthenticationResponseParams.  # noqa: E501
        :type: str
        """

        self._term_url = term_url

    @property
    def merchant_data(self):
        """Gets the merchant_data of this Secure3DAuthenticationResponseParams.  # noqa: E501

        Formatted string encoding transaction time, order ID, and return URL data.  # noqa: E501

        :return: The merchant_data of this Secure3DAuthenticationResponseParams.  # noqa: E501
        :rtype: str
        """
        return self._merchant_data

    @merchant_data.setter
    def merchant_data(self, merchant_data):
        """Sets the merchant_data of this Secure3DAuthenticationResponseParams.

        Formatted string encoding transaction time, order ID, and return URL data.  # noqa: E501

        :param merchant_data: The merchant_data of this Secure3DAuthenticationResponseParams.  # noqa: E501
        :type: str
        """

        self._merchant_data = merchant_data

    @property
    def acs_url(self):
        """Gets the acs_url of this Secure3DAuthenticationResponseParams.  # noqa: E501

        The URL for the authentication redirect for the merchant.  # noqa: E501

        :return: The acs_url of this Secure3DAuthenticationResponseParams.  # noqa: E501
        :rtype: str
        """
        return self._acs_url

    @acs_url.setter
    def acs_url(self, acs_url):
        """Sets the acs_url of this Secure3DAuthenticationResponseParams.

        The URL for the authentication redirect for the merchant.  # noqa: E501

        :param acs_url: The acs_url of this Secure3DAuthenticationResponseParams.  # noqa: E501
        :type: str
        """

        self._acs_url = acs_url

    @property
    def c_req(self):
        """Gets the c_req of this Secure3DAuthenticationResponseParams.  # noqa: E501

        The CReq message initiates cardholder interaction in a 3DS 2.x challenge flow and carries authentication data from the cardholder.  # noqa: E501

        :return: The c_req of this Secure3DAuthenticationResponseParams.  # noqa: E501
        :rtype: str
        """
        return self._c_req

    @c_req.setter
    def c_req(self, c_req):
        """Sets the c_req of this Secure3DAuthenticationResponseParams.

        The CReq message initiates cardholder interaction in a 3DS 2.x challenge flow and carries authentication data from the cardholder.  # noqa: E501

        :param c_req: The c_req of this Secure3DAuthenticationResponseParams.  # noqa: E501
        :type: str
        """

        self._c_req = c_req

    @property
    def session_data(self):
        """Gets the session_data of this Secure3DAuthenticationResponseParams.  # noqa: E501

        Customer web browser session data.  # noqa: E501

        :return: The session_data of this Secure3DAuthenticationResponseParams.  # noqa: E501
        :rtype: str
        """
        return self._session_data

    @session_data.setter
    def session_data(self, session_data):
        """Sets the session_data of this Secure3DAuthenticationResponseParams.

        Customer web browser session data.  # noqa: E501

        :param session_data: The session_data of this Secure3DAuthenticationResponseParams.  # noqa: E501
        :type: str
        """

        self._session_data = session_data

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
        if not isinstance(other, Secure3DAuthenticationResponseParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
