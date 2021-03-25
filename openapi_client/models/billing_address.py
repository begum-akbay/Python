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


class BillingAddress(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'middle_name': 'str',
        'street': 'str',
        'street2': 'str',
        'state_province': 'str',
        'city': 'str',
        'country': 'str',
        'phone': 'Phone',
        'zip_postal_code': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'middle_name': 'middleName',
        'street': 'street',
        'street2': 'street2',
        'state_province': 'stateProvince',
        'city': 'city',
        'country': 'country',
        'phone': 'phone',
        'zip_postal_code': 'zipPostalCode'
    }

    def __init__(self, first_name=None, last_name=None, middle_name=None, street=None, street2=None, state_province=None, city=None, country=None, phone=None, zip_postal_code=None):  # noqa: E501
        """BillingAddress - a model defined in OpenAPI"""  # noqa: E501

        self._first_name = None
        self._last_name = None
        self._middle_name = None
        self._street = None
        self._street2 = None
        self._state_province = None
        self._city = None
        self._country = None
        self._phone = None
        self._zip_postal_code = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if middle_name is not None:
            self.middle_name = middle_name
        self.street = street
        if street2 is not None:
            self.street2 = street2
        if state_province is not None:
            self.state_province = state_province
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if phone is not None:
            self.phone = phone
        if zip_postal_code is not None:
            self.zip_postal_code = zip_postal_code

    @property
    def first_name(self):
        """Gets the first_name of this BillingAddress.  # noqa: E501

        First name.  # noqa: E501

        :return: The first_name of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this BillingAddress.

        First name.  # noqa: E501

        :param first_name: The first_name of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this BillingAddress.  # noqa: E501

        Last name.  # noqa: E501

        :return: The last_name of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this BillingAddress.

        Last name.  # noqa: E501

        :param last_name: The last_name of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def middle_name(self):
        """Gets the middle_name of this BillingAddress.  # noqa: E501

        Middle name.  # noqa: E501

        :return: The middle_name of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this BillingAddress.

        Middle name.  # noqa: E501

        :param middle_name: The middle_name of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def street(self):
        """Gets the street of this BillingAddress.  # noqa: E501

        First line of street address.  # noqa: E501

        :return: The street of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this BillingAddress.

        First line of street address.  # noqa: E501

        :param street: The street of this BillingAddress.  # noqa: E501
        :type: str
        """
        if street is None:
            raise ValueError("Invalid value for `street`, must not be `None`")  # noqa: E501
        if street is not None and not re.search(r'^(?!\s*$).+', street):  # noqa: E501
            raise ValueError(r"Invalid value for `street`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._street = street

    @property
    def street2(self):
        """Gets the street2 of this BillingAddress.  # noqa: E501

        Second line of street address.  # noqa: E501

        :return: The street2 of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._street2

    @street2.setter
    def street2(self, street2):
        """Sets the street2 of this BillingAddress.

        Second line of street address.  # noqa: E501

        :param street2: The street2 of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._street2 = street2

    @property
    def state_province(self):
        """Gets the state_province of this BillingAddress.  # noqa: E501

        State or province.  # noqa: E501

        :return: The state_province of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._state_province

    @state_province.setter
    def state_province(self, state_province):
        """Sets the state_province of this BillingAddress.

        State or province.  # noqa: E501

        :param state_province: The state_province of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._state_province = state_province

    @property
    def city(self):
        """Gets the city of this BillingAddress.  # noqa: E501

        City.  # noqa: E501

        :return: The city of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this BillingAddress.

        City.  # noqa: E501

        :param city: The city of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this BillingAddress.  # noqa: E501

        Country.  # noqa: E501

        :return: The country of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this BillingAddress.

        Country.  # noqa: E501

        :param country: The country of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def phone(self):
        """Gets the phone of this BillingAddress.  # noqa: E501


        :return: The phone of this BillingAddress.  # noqa: E501
        :rtype: Phone
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this BillingAddress.


        :param phone: The phone of this BillingAddress.  # noqa: E501
        :type: Phone
        """

        self._phone = phone

    @property
    def zip_postal_code(self):
        """Gets the zip_postal_code of this BillingAddress.  # noqa: E501

        Postal code.  # noqa: E501

        :return: The zip_postal_code of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._zip_postal_code

    @zip_postal_code.setter
    def zip_postal_code(self, zip_postal_code):
        """Sets the zip_postal_code of this BillingAddress.

        Postal code.  # noqa: E501

        :param zip_postal_code: The zip_postal_code of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._zip_postal_code = zip_postal_code

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
        if not isinstance(other, BillingAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
