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


class Shipping(object):
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
        'name': 'str',
        'contact': 'Contact',
        'address': 'Address'
    }

    attribute_map = {
        'name': 'name',
        'contact': 'contact',
        'address': 'address'
    }

    def __init__(self, name=None, contact=None, address=None):  # noqa: E501
        """Shipping - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._contact = None
        self._address = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if contact is not None:
            self.contact = contact
        if address is not None:
            self.address = address

    @property
    def name(self):
        """Gets the name of this Shipping.  # noqa: E501

        Name of customer for shipping.  # noqa: E501

        :return: The name of this Shipping.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Shipping.

        Name of customer for shipping.  # noqa: E501

        :param name: The name of this Shipping.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 96:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `96`")  # noqa: E501

        self._name = name

    @property
    def contact(self):
        """Gets the contact of this Shipping.  # noqa: E501


        :return: The contact of this Shipping.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Shipping.


        :param contact: The contact of this Shipping.  # noqa: E501
        :type: Contact
        """

        self._contact = contact

    @property
    def address(self):
        """Gets the address of this Shipping.  # noqa: E501


        :return: The address of this Shipping.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Shipping.


        :param address: The address of this Shipping.  # noqa: E501
        :type: Address
        """

        self._address = address

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
        if not isinstance(other, Shipping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
