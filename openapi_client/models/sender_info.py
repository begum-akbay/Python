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


class SenderInfo(object):
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
        'street_address': 'str',
        'city': 'str',
        'state_code': 'str',
        'country_code': 'str',
        'postal_code': 'str',
        'phone_number': 'str',
        'birth_date': 'str',
        'reference_number': 'str',
        'account_number': 'str'
    }

    attribute_map = {
        'name': 'name',
        'street_address': 'streetAddress',
        'city': 'city',
        'state_code': 'stateCode',
        'country_code': 'countryCode',
        'postal_code': 'postalCode',
        'phone_number': 'phoneNumber',
        'birth_date': 'birthDate',
        'reference_number': 'referenceNumber',
        'account_number': 'accountNumber'
    }

    def __init__(self, name=None, street_address=None, city=None, state_code=None, country_code=None, postal_code=None, phone_number=None, birth_date=None, reference_number=None, account_number=None):  # noqa: E501
        """SenderInfo - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._street_address = None
        self._city = None
        self._state_code = None
        self._country_code = None
        self._postal_code = None
        self._phone_number = None
        self._birth_date = None
        self._reference_number = None
        self._account_number = None
        self.discriminator = None

        self.name = name
        self.street_address = street_address
        self.city = city
        self.state_code = state_code
        self.country_code = country_code
        self.postal_code = postal_code
        self.phone_number = phone_number
        if birth_date is not None:
            self.birth_date = birth_date
        self.reference_number = reference_number
        self.account_number = account_number

    @property
    def name(self):
        """Gets the name of this SenderInfo.  # noqa: E501

        Sender name.  # noqa: E501

        :return: The name of this SenderInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SenderInfo.

        Sender name.  # noqa: E501

        :param name: The name of this SenderInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 30:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `30`")  # noqa: E501
        if name is not None and not re.search(r'^(?!\s*$).+', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._name = name

    @property
    def street_address(self):
        """Gets the street_address of this SenderInfo.  # noqa: E501

        Sender street address.  # noqa: E501

        :return: The street_address of this SenderInfo.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this SenderInfo.

        Sender street address.  # noqa: E501

        :param street_address: The street_address of this SenderInfo.  # noqa: E501
        :type: str
        """
        if street_address is None:
            raise ValueError("Invalid value for `street_address`, must not be `None`")  # noqa: E501
        if street_address is not None and len(street_address) > 50:
            raise ValueError("Invalid value for `street_address`, length must be less than or equal to `50`")  # noqa: E501
        if street_address is not None and not re.search(r'^(?!\s*$).+', street_address):  # noqa: E501
            raise ValueError(r"Invalid value for `street_address`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._street_address = street_address

    @property
    def city(self):
        """Gets the city of this SenderInfo.  # noqa: E501

        Sender city.  # noqa: E501

        :return: The city of this SenderInfo.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this SenderInfo.

        Sender city.  # noqa: E501

        :param city: The city of this SenderInfo.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501
        if city is not None and len(city) > 25:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `25`")  # noqa: E501
        if city is not None and not re.search(r'^(?!\s*$).+', city):  # noqa: E501
            raise ValueError(r"Invalid value for `city`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._city = city

    @property
    def state_code(self):
        """Gets the state_code of this SenderInfo.  # noqa: E501

        Sender state.  # noqa: E501

        :return: The state_code of this SenderInfo.  # noqa: E501
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """Sets the state_code of this SenderInfo.

        Sender state.  # noqa: E501

        :param state_code: The state_code of this SenderInfo.  # noqa: E501
        :type: str
        """
        if state_code is None:
            raise ValueError("Invalid value for `state_code`, must not be `None`")  # noqa: E501
        if state_code is not None and not re.search(r'[A-Z]{2}', state_code):  # noqa: E501
            raise ValueError(r"Invalid value for `state_code`, must be a follow pattern or equal to `/[A-Z]{2}/`")  # noqa: E501

        self._state_code = state_code

    @property
    def country_code(self):
        """Gets the country_code of this SenderInfo.  # noqa: E501

        Sender country code.  # noqa: E501

        :return: The country_code of this SenderInfo.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this SenderInfo.

        Sender country code.  # noqa: E501

        :param country_code: The country_code of this SenderInfo.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501
        if country_code is not None and not re.search(r'[A-Z]{2}', country_code):  # noqa: E501
            raise ValueError(r"Invalid value for `country_code`, must be a follow pattern or equal to `/[A-Z]{2}/`")  # noqa: E501

        self._country_code = country_code

    @property
    def postal_code(self):
        """Gets the postal_code of this SenderInfo.  # noqa: E501

        Sender postal code.  # noqa: E501

        :return: The postal_code of this SenderInfo.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this SenderInfo.

        Sender postal code.  # noqa: E501

        :param postal_code: The postal_code of this SenderInfo.  # noqa: E501
        :type: str
        """
        if postal_code is None:
            raise ValueError("Invalid value for `postal_code`, must not be `None`")  # noqa: E501
        if postal_code is not None and len(postal_code) > 5:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `5`")  # noqa: E501
        if postal_code is not None and not re.search(r'^(?!\s*$).+', postal_code):  # noqa: E501
            raise ValueError(r"Invalid value for `postal_code`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def phone_number(self):
        """Gets the phone_number of this SenderInfo.  # noqa: E501

        Sender phone number.  # noqa: E501

        :return: The phone_number of this SenderInfo.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this SenderInfo.

        Sender phone number.  # noqa: E501

        :param phone_number: The phone_number of this SenderInfo.  # noqa: E501
        :type: str
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501
        if phone_number is not None and not re.search(r'[0-9]{10}', phone_number):  # noqa: E501
            raise ValueError(r"Invalid value for `phone_number`, must be a follow pattern or equal to `/[0-9]{10}/`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def birth_date(self):
        """Gets the birth_date of this SenderInfo.  # noqa: E501

        Sender date of birth (YYYYMMDD).  # noqa: E501

        :return: The birth_date of this SenderInfo.  # noqa: E501
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this SenderInfo.

        Sender date of birth (YYYYMMDD).  # noqa: E501

        :param birth_date: The birth_date of this SenderInfo.  # noqa: E501
        :type: str
        """
        if birth_date is not None and not re.search(r'^([0-9]{4})(1[0-2]|0[1-9])(3[01]|0[1-9]|[12][0-9])$', birth_date):  # noqa: E501
            raise ValueError(r"Invalid value for `birth_date`, must be a follow pattern or equal to `/^([0-9]{4})(1[0-2]|0[1-9])(3[01]|0[1-9]|[12][0-9])$/`")  # noqa: E501

        self._birth_date = birth_date

    @property
    def reference_number(self):
        """Gets the reference_number of this SenderInfo.  # noqa: E501

        Sender reference number.  # noqa: E501

        :return: The reference_number of this SenderInfo.  # noqa: E501
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this SenderInfo.

        Sender reference number.  # noqa: E501

        :param reference_number: The reference_number of this SenderInfo.  # noqa: E501
        :type: str
        """
        if reference_number is None:
            raise ValueError("Invalid value for `reference_number`, must not be `None`")  # noqa: E501
        if reference_number is not None and len(reference_number) > 19:
            raise ValueError("Invalid value for `reference_number`, length must be less than or equal to `19`")  # noqa: E501
        if reference_number is not None and not re.search(r'^(?!\s*$).+', reference_number):  # noqa: E501
            raise ValueError(r"Invalid value for `reference_number`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._reference_number = reference_number

    @property
    def account_number(self):
        """Gets the account_number of this SenderInfo.  # noqa: E501

        Sender account number.  # noqa: E501

        :return: The account_number of this SenderInfo.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this SenderInfo.

        Sender account number.  # noqa: E501

        :param account_number: The account_number of this SenderInfo.  # noqa: E501
        :type: str
        """
        if account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501
        if account_number is not None and len(account_number) > 19:
            raise ValueError("Invalid value for `account_number`, length must be less than or equal to `19`")  # noqa: E501
        if account_number is not None and not re.search(r'^(?!\s*$).+', account_number):  # noqa: E501
            raise ValueError(r"Invalid value for `account_number`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._account_number = account_number

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
        if not isinstance(other, SenderInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
