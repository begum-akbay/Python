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


class Address(object):
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
        'company': 'str',
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'region': 'str',
        'postal_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'company': 'company',
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'region': 'region',
        'postal_code': 'postalCode',
        'country': 'country'
    }

    def __init__(self, company=None, address1=None, address2=None, city=None, region=None, postal_code=None, country=None):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501

        self._company = None
        self._address1 = None
        self._address2 = None
        self._city = None
        self._region = None
        self._postal_code = None
        self._country = None
        self.discriminator = None

        if company is not None:
            self.company = company
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if region is not None:
            self.region = region
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country

    @property
    def company(self):
        """Gets the company of this Address.  # noqa: E501

        Company name associated with the address.  # noqa: E501

        :return: The company of this Address.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Address.

        Company name associated with the address.  # noqa: E501

        :param company: The company of this Address.  # noqa: E501
        :type: str
        """
        if company is not None and len(company) > 96:
            raise ValueError("Invalid value for `company`, length must be less than or equal to `96`")  # noqa: E501

        self._company = company

    @property
    def address1(self):
        """Gets the address1 of this Address.  # noqa: E501

        First line of the street address.  # noqa: E501

        :return: The address1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this Address.

        First line of the street address.  # noqa: E501

        :param address1: The address1 of this Address.  # noqa: E501
        :type: str
        """
        if address1 is not None and len(address1) > 96:
            raise ValueError("Invalid value for `address1`, length must be less than or equal to `96`")  # noqa: E501

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this Address.  # noqa: E501

        Second line of the street address.  # noqa: E501

        :return: The address2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Address.

        Second line of the street address.  # noqa: E501

        :param address2: The address2 of this Address.  # noqa: E501
        :type: str
        """
        if address2 is not None and len(address2) > 96:
            raise ValueError("Invalid value for `address2`, length must be less than or equal to `96`")  # noqa: E501

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

        City or locality.  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

        City or locality.  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """
        if city is not None and len(city) > 96:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `96`")  # noqa: E501

        self._city = city

    @property
    def region(self):
        """Gets the region of this Address.  # noqa: E501

        State or province.  # noqa: E501

        :return: The region of this Address.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Address.

        State or province.  # noqa: E501

        :param region: The region of this Address.  # noqa: E501
        :type: str
        """
        if region is not None and len(region) > 96:
            raise ValueError("Invalid value for `region`, length must be less than or equal to `96`")  # noqa: E501

        self._region = region

    @property
    def postal_code(self):
        """Gets the postal_code of this Address.  # noqa: E501

        ZIP code or postal code.  # noqa: E501

        :return: The postal_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Address.

        ZIP code or postal code.  # noqa: E501

        :param postal_code: The postal_code of this Address.  # noqa: E501
        :type: str
        """
        if postal_code is not None and len(postal_code) > 24:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `24`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501

        ISO-3166-1  ALPHA-2, ALPHA-3, numeric or full country name. In the case of PaySecure endpoints, pass the country code in an ISO format.  # noqa: E501

        :return: The country of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.

        ISO-3166-1  ALPHA-2, ALPHA-3, numeric or full country name. In the case of PaySecure endpoints, pass the country code in an ISO format.  # noqa: E501

        :param country: The country of this Address.  # noqa: E501
        :type: str
        """
        if country is not None and len(country) > 32:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `32`")  # noqa: E501

        self._country = country

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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
