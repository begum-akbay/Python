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


class Sepa(object):
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
        'iban': 'str',
        'name': 'str',
        'country': 'str',
        'email': 'str',
        'mandate': 'SepaMandate'
    }

    attribute_map = {
        'iban': 'iban',
        'name': 'name',
        'country': 'country',
        'email': 'email',
        'mandate': 'mandate'
    }

    def __init__(self, iban=None, name=None, country=None, email=None, mandate=None):  # noqa: E501
        """Sepa - a model defined in OpenAPI"""  # noqa: E501

        self._iban = None
        self._name = None
        self._country = None
        self._email = None
        self._mandate = None
        self.discriminator = None

        self.iban = iban
        self.name = name
        self.country = country
        if email is not None:
            self.email = email
        self.mandate = mandate

    @property
    def iban(self):
        """Gets the iban of this Sepa.  # noqa: E501

        Bank account in IBAN format.  # noqa: E501

        :return: The iban of this Sepa.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this Sepa.

        Bank account in IBAN format.  # noqa: E501

        :param iban: The iban of this Sepa.  # noqa: E501
        :type: str
        """
        if iban is None:
            raise ValueError("Invalid value for `iban`, must not be `None`")  # noqa: E501
        if iban is not None and len(iban) > 34:
            raise ValueError("Invalid value for `iban`, length must be less than or equal to `34`")  # noqa: E501
        if iban is not None and not re.search(r'^(?!\s*$).+', iban):  # noqa: E501
            raise ValueError(r"Invalid value for `iban`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._iban = iban

    @property
    def name(self):
        """Gets the name of this Sepa.  # noqa: E501

        The name of the payer.  # noqa: E501

        :return: The name of this Sepa.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Sepa.

        The name of the payer.  # noqa: E501

        :param name: The name of this Sepa.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 96:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `96`")  # noqa: E501
        if name is not None and not re.search(r'^(?!\s*$).+', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._name = name

    @property
    def country(self):
        """Gets the country of this Sepa.  # noqa: E501

        Country of residence of the payer using the ISO 3166 standard.  # noqa: E501

        :return: The country of this Sepa.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Sepa.

        Country of residence of the payer using the ISO 3166 standard.  # noqa: E501

        :param country: The country of this Sepa.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501
        if country is not None and len(country) > 3:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `3`")  # noqa: E501
        if country is not None and not re.search(r'^(?!\s*$).+', country):  # noqa: E501
            raise ValueError(r"Invalid value for `country`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._country = country

    @property
    def email(self):
        """Gets the email of this Sepa.  # noqa: E501

        The email address of the payer.  # noqa: E501

        :return: The email of this Sepa.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Sepa.

        The email address of the payer.  # noqa: E501

        :param email: The email of this Sepa.  # noqa: E501
        :type: str
        """
        if email is not None and len(email) > 254:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501

        self._email = email

    @property
    def mandate(self):
        """Gets the mandate of this Sepa.  # noqa: E501


        :return: The mandate of this Sepa.  # noqa: E501
        :rtype: SepaMandate
        """
        return self._mandate

    @mandate.setter
    def mandate(self, mandate):
        """Sets the mandate of this Sepa.


        :param mandate: The mandate of this Sepa.  # noqa: E501
        :type: SepaMandate
        """
        if mandate is None:
            raise ValueError("Invalid value for `mandate`, must not be `None`")  # noqa: E501

        self._mandate = mandate

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
        if not isinstance(other, Sepa):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
