# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.1.0.20210122.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BackgroundColor(object):
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
        'header': 'Header',
        'content': 'Content',
        'footer': 'Footer'
    }

    attribute_map = {
        'header': 'header',
        'content': 'content',
        'footer': 'footer'
    }

    def __init__(self, header=None, content=None, footer=None):  # noqa: E501
        """BackgroundColor - a model defined in OpenAPI"""  # noqa: E501

        self._header = None
        self._content = None
        self._footer = None
        self.discriminator = None

        if header is not None:
            self.header = header
        if content is not None:
            self.content = content
        if footer is not None:
            self.footer = footer

    @property
    def header(self):
        """Gets the header of this BackgroundColor.  # noqa: E501


        :return: The header of this BackgroundColor.  # noqa: E501
        :rtype: Header
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this BackgroundColor.


        :param header: The header of this BackgroundColor.  # noqa: E501
        :type: Header
        """

        self._header = header

    @property
    def content(self):
        """Gets the content of this BackgroundColor.  # noqa: E501


        :return: The content of this BackgroundColor.  # noqa: E501
        :rtype: Content
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this BackgroundColor.


        :param content: The content of this BackgroundColor.  # noqa: E501
        :type: Content
        """

        self._content = content

    @property
    def footer(self):
        """Gets the footer of this BackgroundColor.  # noqa: E501


        :return: The footer of this BackgroundColor.  # noqa: E501
        :rtype: Footer
        """
        return self._footer

    @footer.setter
    def footer(self, footer):
        """Sets the footer of this BackgroundColor.


        :param footer: The footer of this BackgroundColor.  # noqa: E501
        :type: Footer
        """

        self._footer = footer

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
        if not isinstance(other, BackgroundColor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
