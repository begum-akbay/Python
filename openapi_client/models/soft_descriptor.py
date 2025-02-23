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


class SoftDescriptor(object):
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
        'dynamic_merchant_name': 'str',
        'customer_service_number': 'str',
        'mcc': 'str',
        'dynamic_address': 'Address'
    }

    attribute_map = {
        'dynamic_merchant_name': 'dynamicMerchantName',
        'customer_service_number': 'customerServiceNumber',
        'mcc': 'mcc',
        'dynamic_address': 'dynamicAddress'
    }

    def __init__(self, dynamic_merchant_name=None, customer_service_number=None, mcc=None, dynamic_address=None):  # noqa: E501
        """SoftDescriptor - a model defined in OpenAPI"""  # noqa: E501

        self._dynamic_merchant_name = None
        self._customer_service_number = None
        self._mcc = None
        self._dynamic_address = None
        self.discriminator = None

        self.dynamic_merchant_name = dynamic_merchant_name
        if customer_service_number is not None:
            self.customer_service_number = customer_service_number
        if mcc is not None:
            self.mcc = mcc
        if dynamic_address is not None:
            self.dynamic_address = dynamic_address

    @property
    def dynamic_merchant_name(self):
        """Gets the dynamic_merchant_name of this SoftDescriptor.  # noqa: E501

        Store \"doing-business-as\" name.  # noqa: E501

        :return: The dynamic_merchant_name of this SoftDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_merchant_name

    @dynamic_merchant_name.setter
    def dynamic_merchant_name(self, dynamic_merchant_name):
        """Sets the dynamic_merchant_name of this SoftDescriptor.

        Store \"doing-business-as\" name.  # noqa: E501

        :param dynamic_merchant_name: The dynamic_merchant_name of this SoftDescriptor.  # noqa: E501
        :type: str
        """
        if dynamic_merchant_name is None:
            raise ValueError("Invalid value for `dynamic_merchant_name`, must not be `None`")  # noqa: E501
        if dynamic_merchant_name is not None and not re.search(r'^(?!\s*$).+', dynamic_merchant_name):  # noqa: E501
            raise ValueError(r"Invalid value for `dynamic_merchant_name`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._dynamic_merchant_name = dynamic_merchant_name

    @property
    def customer_service_number(self):
        """Gets the customer_service_number of this SoftDescriptor.  # noqa: E501

        Customer service phone number information that is passed to the issuer (it may appear on the cardholder’s statement) or if merchant wants to pass information that differs from the information stored on our master File.  # noqa: E501

        :return: The customer_service_number of this SoftDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._customer_service_number

    @customer_service_number.setter
    def customer_service_number(self, customer_service_number):
        """Sets the customer_service_number of this SoftDescriptor.

        Customer service phone number information that is passed to the issuer (it may appear on the cardholder’s statement) or if merchant wants to pass information that differs from the information stored on our master File.  # noqa: E501

        :param customer_service_number: The customer_service_number of this SoftDescriptor.  # noqa: E501
        :type: str
        """
        if customer_service_number is not None and len(customer_service_number) > 10:
            raise ValueError("Invalid value for `customer_service_number`, length must be less than or equal to `10`")  # noqa: E501
        if customer_service_number is not None and not re.search(r'^[0-9]+$', customer_service_number):  # noqa: E501
            raise ValueError(r"Invalid value for `customer_service_number`, must be a follow pattern or equal to `/^[0-9]+$/`")  # noqa: E501

        self._customer_service_number = customer_service_number

    @property
    def mcc(self):
        """Gets the mcc of this SoftDescriptor.  # noqa: E501

        The 4-digit merchant category code (MCC). The merchant might be associated with multiple MCCs. In that case the MCC provided here will be the one that better describes the current transaction.  # noqa: E501

        :return: The mcc of this SoftDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc):
        """Sets the mcc of this SoftDescriptor.

        The 4-digit merchant category code (MCC). The merchant might be associated with multiple MCCs. In that case the MCC provided here will be the one that better describes the current transaction.  # noqa: E501

        :param mcc: The mcc of this SoftDescriptor.  # noqa: E501
        :type: str
        """
        if mcc is not None and len(mcc) > 4:
            raise ValueError("Invalid value for `mcc`, length must be less than or equal to `4`")  # noqa: E501

        self._mcc = mcc

    @property
    def dynamic_address(self):
        """Gets the dynamic_address of this SoftDescriptor.  # noqa: E501


        :return: The dynamic_address of this SoftDescriptor.  # noqa: E501
        :rtype: Address
        """
        return self._dynamic_address

    @dynamic_address.setter
    def dynamic_address(self, dynamic_address):
        """Sets the dynamic_address of this SoftDescriptor.


        :param dynamic_address: The dynamic_address of this SoftDescriptor.  # noqa: E501
        :type: Address
        """

        self._dynamic_address = dynamic_address

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
        if not isinstance(other, SoftDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
