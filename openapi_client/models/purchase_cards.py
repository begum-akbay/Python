# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.10.1.20200226.002
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PurchaseCards(object):
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
        'level2': 'PurchaseCardsLevel2',
        'level3': 'PurchaseCardsLevel3'
    }

    attribute_map = {
        'level2': 'Level2',
        'level3': 'Level3'
    }

    def __init__(self, level2=None, level3=None):  # noqa: E501
        """PurchaseCards - a model defined in OpenAPI"""  # noqa: E501

        self._level2 = None
        self._level3 = None
        self.discriminator = None

        if level2 is not None:
            self.level2 = level2
        if level3 is not None:
            self.level3 = level3

    @property
    def level2(self):
        """Gets the level2 of this PurchaseCards.  # noqa: E501


        :return: The level2 of this PurchaseCards.  # noqa: E501
        :rtype: PurchaseCardsLevel2
        """
        return self._level2

    @level2.setter
    def level2(self, level2):
        """Sets the level2 of this PurchaseCards.


        :param level2: The level2 of this PurchaseCards.  # noqa: E501
        :type: PurchaseCardsLevel2
        """

        self._level2 = level2

    @property
    def level3(self):
        """Gets the level3 of this PurchaseCards.  # noqa: E501


        :return: The level3 of this PurchaseCards.  # noqa: E501
        :rtype: PurchaseCardsLevel3
        """
        return self._level3

    @level3.setter
    def level3(self, level3):
        """Sets the level3 of this PurchaseCards.


        :param level3: The level3 of this PurchaseCards.  # noqa: E501
        :type: PurchaseCardsLevel3
        """

        self._level3 = level3

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
        if not isinstance(other, PurchaseCards):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
