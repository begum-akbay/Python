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


class SplitShipment(object):
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
        'total_count': 'int',
        'final_shipment': 'bool'
    }

    attribute_map = {
        'total_count': 'totalCount',
        'final_shipment': 'finalShipment'
    }

    def __init__(self, total_count=None, final_shipment=False):  # noqa: E501
        """SplitShipment - a model defined in OpenAPI"""  # noqa: E501

        self._total_count = None
        self._final_shipment = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if final_shipment is not None:
            self.final_shipment = final_shipment

    @property
    def total_count(self):
        """Gets the total_count of this SplitShipment.  # noqa: E501

        Total count of the shipment, can be set at preauth or the first postauth.  # noqa: E501

        :return: The total_count of this SplitShipment.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this SplitShipment.

        Total count of the shipment, can be set at preauth or the first postauth.  # noqa: E501

        :param total_count: The total_count of this SplitShipment.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def final_shipment(self):
        """Gets the final_shipment of this SplitShipment.  # noqa: E501

        Indicates whether the transaction is the final shipment.  # noqa: E501

        :return: The final_shipment of this SplitShipment.  # noqa: E501
        :rtype: bool
        """
        return self._final_shipment

    @final_shipment.setter
    def final_shipment(self, final_shipment):
        """Sets the final_shipment of this SplitShipment.

        Indicates whether the transaction is the final shipment.  # noqa: E501

        :param final_shipment: The final_shipment of this SplitShipment.  # noqa: E501
        :type: bool
        """

        self._final_shipment = final_shipment

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
        if not isinstance(other, SplitShipment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
