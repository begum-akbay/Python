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


class TransactionResponseAuthenticationRedirectParams(object):
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
        'pa_req': 'str',
        'term_url': 'str',
        'md': 'str'
    }

    attribute_map = {
        'pa_req': 'PaReq',
        'term_url': 'TermUrl',
        'md': 'MD'
    }

    def __init__(self, pa_req=None, term_url=None, md=None):  # noqa: E501
        """TransactionResponseAuthenticationRedirectParams - a model defined in Swagger"""  # noqa: E501

        self._pa_req = None
        self._term_url = None
        self._md = None
        self.discriminator = None

        if pa_req is not None:
            self.pa_req = pa_req
        if term_url is not None:
            self.term_url = term_url
        if md is not None:
            self.md = md

    @property
    def pa_req(self):
        """Gets the pa_req of this TransactionResponseAuthenticationRedirectParams.  # noqa: E501


        :return: The pa_req of this TransactionResponseAuthenticationRedirectParams.  # noqa: E501
        :rtype: str
        """
        return self._pa_req

    @pa_req.setter
    def pa_req(self, pa_req):
        """Sets the pa_req of this TransactionResponseAuthenticationRedirectParams.


        :param pa_req: The pa_req of this TransactionResponseAuthenticationRedirectParams.  # noqa: E501
        :type: str
        """

        self._pa_req = pa_req

    @property
    def term_url(self):
        """Gets the term_url of this TransactionResponseAuthenticationRedirectParams.  # noqa: E501


        :return: The term_url of this TransactionResponseAuthenticationRedirectParams.  # noqa: E501
        :rtype: str
        """
        return self._term_url

    @term_url.setter
    def term_url(self, term_url):
        """Sets the term_url of this TransactionResponseAuthenticationRedirectParams.


        :param term_url: The term_url of this TransactionResponseAuthenticationRedirectParams.  # noqa: E501
        :type: str
        """

        self._term_url = term_url

    @property
    def md(self):
        """Gets the md of this TransactionResponseAuthenticationRedirectParams.  # noqa: E501


        :return: The md of this TransactionResponseAuthenticationRedirectParams.  # noqa: E501
        :rtype: str
        """
        return self._md

    @md.setter
    def md(self, md):
        """Sets the md of this TransactionResponseAuthenticationRedirectParams.


        :param md: The md of this TransactionResponseAuthenticationRedirectParams.  # noqa: E501
        :type: str
        """

        self._md = md

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
        if not isinstance(other, TransactionResponseAuthenticationRedirectParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
