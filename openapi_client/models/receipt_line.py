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


class ReceiptLine(object):
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
        'end_of_line': 'bool',
        'text': 'str'
    }

    attribute_map = {
        'end_of_line': 'endOfLine',
        'text': 'text'
    }

    def __init__(self, end_of_line=True, text=None):  # noqa: E501
        """ReceiptLine - a model defined in OpenAPI"""  # noqa: E501

        self._end_of_line = None
        self._text = None
        self.discriminator = None

        if end_of_line is not None:
            self.end_of_line = end_of_line
        self.text = text

    @property
    def end_of_line(self):
        """Gets the end_of_line of this ReceiptLine.  # noqa: E501

        Flag to indicate if the text ends at the end of this receipt line.  # noqa: E501

        :return: The end_of_line of this ReceiptLine.  # noqa: E501
        :rtype: bool
        """
        return self._end_of_line

    @end_of_line.setter
    def end_of_line(self, end_of_line):
        """Sets the end_of_line of this ReceiptLine.

        Flag to indicate if the text ends at the end of this receipt line.  # noqa: E501

        :param end_of_line: The end_of_line of this ReceiptLine.  # noqa: E501
        :type: bool
        """

        self._end_of_line = end_of_line

    @property
    def text(self):
        """Gets the text of this ReceiptLine.  # noqa: E501

        Text that represents a line of the actual receipt data, that can be printed out.  # noqa: E501

        :return: The text of this ReceiptLine.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ReceiptLine.

        Text that represents a line of the actual receipt data, that can be printed out.  # noqa: E501

        :param text: The text of this ReceiptLine.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

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
        if not isinstance(other, ReceiptLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
