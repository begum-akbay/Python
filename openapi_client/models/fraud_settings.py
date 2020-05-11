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


class FraudSettings(object):
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
        'blocked_items': 'BlockedItems',
        'maximum_purchase_amount': 'list[MaximumPurchaseAmount]',
        'lockout_time': 'LockoutTime',
        'country_profile': 'CountryProfile'
    }

    attribute_map = {
        'blocked_items': 'blockedItems',
        'maximum_purchase_amount': 'maximumPurchaseAmount',
        'lockout_time': 'lockoutTime',
        'country_profile': 'countryProfile'
    }

    def __init__(self, blocked_items=None, maximum_purchase_amount=None, lockout_time=None, country_profile=None):  # noqa: E501
        """FraudSettings - a model defined in OpenAPI"""  # noqa: E501

        self._blocked_items = None
        self._maximum_purchase_amount = None
        self._lockout_time = None
        self._country_profile = None
        self.discriminator = None

        if blocked_items is not None:
            self.blocked_items = blocked_items
        if maximum_purchase_amount is not None:
            self.maximum_purchase_amount = maximum_purchase_amount
        if lockout_time is not None:
            self.lockout_time = lockout_time
        if country_profile is not None:
            self.country_profile = country_profile

    @property
    def blocked_items(self):
        """Gets the blocked_items of this FraudSettings.  # noqa: E501


        :return: The blocked_items of this FraudSettings.  # noqa: E501
        :rtype: BlockedItems
        """
        return self._blocked_items

    @blocked_items.setter
    def blocked_items(self, blocked_items):
        """Sets the blocked_items of this FraudSettings.


        :param blocked_items: The blocked_items of this FraudSettings.  # noqa: E501
        :type: BlockedItems
        """

        self._blocked_items = blocked_items

    @property
    def maximum_purchase_amount(self):
        """Gets the maximum_purchase_amount of this FraudSettings.  # noqa: E501


        :return: The maximum_purchase_amount of this FraudSettings.  # noqa: E501
        :rtype: list[MaximumPurchaseAmount]
        """
        return self._maximum_purchase_amount

    @maximum_purchase_amount.setter
    def maximum_purchase_amount(self, maximum_purchase_amount):
        """Sets the maximum_purchase_amount of this FraudSettings.


        :param maximum_purchase_amount: The maximum_purchase_amount of this FraudSettings.  # noqa: E501
        :type: list[MaximumPurchaseAmount]
        """

        self._maximum_purchase_amount = maximum_purchase_amount

    @property
    def lockout_time(self):
        """Gets the lockout_time of this FraudSettings.  # noqa: E501


        :return: The lockout_time of this FraudSettings.  # noqa: E501
        :rtype: LockoutTime
        """
        return self._lockout_time

    @lockout_time.setter
    def lockout_time(self, lockout_time):
        """Sets the lockout_time of this FraudSettings.


        :param lockout_time: The lockout_time of this FraudSettings.  # noqa: E501
        :type: LockoutTime
        """

        self._lockout_time = lockout_time

    @property
    def country_profile(self):
        """Gets the country_profile of this FraudSettings.  # noqa: E501


        :return: The country_profile of this FraudSettings.  # noqa: E501
        :rtype: CountryProfile
        """
        return self._country_profile

    @country_profile.setter
    def country_profile(self, country_profile):
        """Sets the country_profile of this FraudSettings.


        :param country_profile: The country_profile of this FraudSettings.  # noqa: E501
        :type: CountryProfile
        """

        self._country_profile = country_profile

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
        if not isinstance(other, FraudSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
