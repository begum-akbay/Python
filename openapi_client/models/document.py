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


class Document(object):
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
        'type': 'str',
        'number': 'str'
    }

    attribute_map = {
        'type': 'type',
        'number': 'number'
    }

    def __init__(self, type=None, number=None):  # noqa: E501
        """Document - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._number = None
        self.discriminator = None

        self.type = type
        self.number = number

    @property
    def type(self):
        """Gets the type of this Document.  # noqa: E501

        Document type.  # noqa: E501

        :return: The type of this Document.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Document.

        Document type.  # noqa: E501

        :param type: The type of this Document.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["NATIONAL_IDENTITY", "SINGLE_TAX_IDENTIFICATION", "SINGLE_CODE_OF_LABOR_IDENTIFICATION", "BOOK_ENLISTMENT", "CIVIC_NOTEBOOK", "PASSPORT"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def number(self):
        """Gets the number of this Document.  # noqa: E501

        Document number.  # noqa: E501

        :return: The number of this Document.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Document.

        Document number.  # noqa: E501

        :param number: The number of this Document.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501
        if number is not None and len(number) > 30:
            raise ValueError("Invalid value for `number`, length must be less than or equal to `30`")  # noqa: E501
        if number is not None and not re.search(r'^(?!\s*$).+', number):  # noqa: E501
            raise ValueError(r"Invalid value for `number`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._number = number

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
        if not isinstance(other, Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
