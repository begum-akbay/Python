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

from swagger_client.models.address import Address  # noqa: F401,E501
from swagger_client.models.contact import Contact  # noqa: F401,E501


class Billing(object):
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
        'name': 'str',
        'personal_number': 'str',
        'birth_date': 'date',
        'gender': 'str',
        'contact': 'Contact',
        'address': 'Address'
    }

    attribute_map = {
        'name': 'name',
        'personal_number': 'personalNumber',
        'birth_date': 'birthDate',
        'gender': 'gender',
        'contact': 'contact',
        'address': 'address'
    }

    def __init__(self, name=None, personal_number=None, birth_date=None, gender=None, contact=None, address=None):  # noqa: E501
        """Billing - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._personal_number = None
        self._birth_date = None
        self._gender = None
        self._contact = None
        self._address = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if personal_number is not None:
            self.personal_number = personal_number
        if birth_date is not None:
            self.birth_date = birth_date
        if gender is not None:
            self.gender = gender
        if contact is not None:
            self.contact = contact
        if address is not None:
            self.address = address

    @property
    def name(self):
        """Gets the name of this Billing.  # noqa: E501


        :return: The name of this Billing.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Billing.


        :param name: The name of this Billing.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 96:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `96`")  # noqa: E501

        self._name = name

    @property
    def personal_number(self):
        """Gets the personal_number of this Billing.  # noqa: E501


        :return: The personal_number of this Billing.  # noqa: E501
        :rtype: str
        """
        return self._personal_number

    @personal_number.setter
    def personal_number(self, personal_number):
        """Sets the personal_number of this Billing.


        :param personal_number: The personal_number of this Billing.  # noqa: E501
        :type: str
        """

        self._personal_number = personal_number

    @property
    def birth_date(self):
        """Gets the birth_date of this Billing.  # noqa: E501


        :return: The birth_date of this Billing.  # noqa: E501
        :rtype: date
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this Billing.


        :param birth_date: The birth_date of this Billing.  # noqa: E501
        :type: date
        """

        self._birth_date = birth_date

    @property
    def gender(self):
        """Gets the gender of this Billing.  # noqa: E501


        :return: The gender of this Billing.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Billing.


        :param gender: The gender of this Billing.  # noqa: E501
        :type: str
        """
        allowed_values = ["MALE", "FEMALE", "UNKNOWN"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"  # noqa: E501
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def contact(self):
        """Gets the contact of this Billing.  # noqa: E501


        :return: The contact of this Billing.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Billing.


        :param contact: The contact of this Billing.  # noqa: E501
        :type: Contact
        """

        self._contact = contact

    @property
    def address(self):
        """Gets the address of this Billing.  # noqa: E501


        :return: The address of this Billing.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Billing.


        :param address: The address of this Billing.  # noqa: E501
        :type: Address
        """

        self._address = address

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
        if not isinstance(other, Billing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
