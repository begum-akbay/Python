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


class Background(object):
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
        'top_bar': 'TopBar',
        'body': 'Body',
        'content': 'Content',
        'borders': 'Borders'
    }

    attribute_map = {
        'top_bar': 'topBar',
        'body': 'body',
        'content': 'content',
        'borders': 'borders'
    }

    def __init__(self, top_bar=None, body=None, content=None, borders=None):  # noqa: E501
        """Background - a model defined in OpenAPI"""  # noqa: E501

        self._top_bar = None
        self._body = None
        self._content = None
        self._borders = None
        self.discriminator = None

        if top_bar is not None:
            self.top_bar = top_bar
        if body is not None:
            self.body = body
        if content is not None:
            self.content = content
        if borders is not None:
            self.borders = borders

    @property
    def top_bar(self):
        """Gets the top_bar of this Background.  # noqa: E501


        :return: The top_bar of this Background.  # noqa: E501
        :rtype: TopBar
        """
        return self._top_bar

    @top_bar.setter
    def top_bar(self, top_bar):
        """Sets the top_bar of this Background.


        :param top_bar: The top_bar of this Background.  # noqa: E501
        :type: TopBar
        """

        self._top_bar = top_bar

    @property
    def body(self):
        """Gets the body of this Background.  # noqa: E501


        :return: The body of this Background.  # noqa: E501
        :rtype: Body
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Background.


        :param body: The body of this Background.  # noqa: E501
        :type: Body
        """

        self._body = body

    @property
    def content(self):
        """Gets the content of this Background.  # noqa: E501


        :return: The content of this Background.  # noqa: E501
        :rtype: Content
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Background.


        :param content: The content of this Background.  # noqa: E501
        :type: Content
        """

        self._content = content

    @property
    def borders(self):
        """Gets the borders of this Background.  # noqa: E501


        :return: The borders of this Background.  # noqa: E501
        :rtype: Borders
        """
        return self._borders

    @borders.setter
    def borders(self, borders):
        """Sets the borders of this Background.


        :param borders: The borders of this Background.  # noqa: E501
        :type: Borders
        """

        self._borders = borders

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
        if not isinstance(other, Background):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
