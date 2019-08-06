# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.6.0.20190507.002
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Contact(object):
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
        'phone': 'str',
        'mobile_phone': 'str',
        'fax': 'str',
        'email': 'str'
    }

    attribute_map = {
        'phone': 'phone',
        'mobile_phone': 'mobilePhone',
        'fax': 'fax',
        'email': 'email'
    }

    def __init__(self, phone=None, mobile_phone=None, fax=None, email=None):  # noqa: E501
        """Contact - a model defined in OpenAPI"""  # noqa: E501

        self._phone = None
        self._mobile_phone = None
        self._fax = None
        self._email = None
        self.discriminator = None

        if phone is not None:
            self.phone = phone
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if fax is not None:
            self.fax = fax
        if email is not None:
            self.email = email

    @property
    def phone(self):
        """Gets the phone of this Contact.  # noqa: E501

        Primary phone number.  # noqa: E501

        :return: The phone of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Contact.

        Primary phone number.  # noqa: E501

        :param phone: The phone of this Contact.  # noqa: E501
        :type: str
        """
        if phone is not None and len(phone) > 32:
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `32`")  # noqa: E501

        self._phone = phone

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this Contact.  # noqa: E501

        Mobile phone number.  # noqa: E501

        :return: The mobile_phone of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this Contact.

        Mobile phone number.  # noqa: E501

        :param mobile_phone: The mobile_phone of this Contact.  # noqa: E501
        :type: str
        """
        if mobile_phone is not None and len(mobile_phone) > 32:
            raise ValueError("Invalid value for `mobile_phone`, length must be less than or equal to `32`")  # noqa: E501

        self._mobile_phone = mobile_phone

    @property
    def fax(self):
        """Gets the fax of this Contact.  # noqa: E501

        Fax number.  # noqa: E501

        :return: The fax of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this Contact.

        Fax number.  # noqa: E501

        :param fax: The fax of this Contact.  # noqa: E501
        :type: str
        """
        if fax is not None and len(fax) > 32:
            raise ValueError("Invalid value for `fax`, length must be less than or equal to `32`")  # noqa: E501

        self._fax = fax

    @property
    def email(self):
        """Gets the email of this Contact.  # noqa: E501

        Email address.  # noqa: E501

        :return: The email of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Contact.

        Email address.  # noqa: E501

        :param email: The email of this Contact.  # noqa: E501
        :type: str
        """
        if email is not None and len(email) > 254:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501

        self._email = email

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
        if not isinstance(other, Contact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
