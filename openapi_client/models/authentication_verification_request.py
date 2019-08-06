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


class AuthenticationVerificationRequest(object):
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
        'store_id': 'str',
        'request_type': 'str',
        'security_code': 'str',
        'billing_address': 'Address'
    }

    attribute_map = {
        'store_id': 'storeId',
        'request_type': 'requestType',
        'security_code': 'securityCode',
        'billing_address': 'billingAddress'
    }

    discriminator_value_class_map = {
        'UnionPayAuthenticationVerificationRequest': 'UnionPayAuthenticationVerificationRequest',
        'Secure3dAuthenticationVerificationRequest': 'Secure3dAuthenticationVerificationRequest'
    }

    def __init__(self, store_id=None, request_type=None, security_code=None, billing_address=None):  # noqa: E501
        """AuthenticationVerificationRequest - a model defined in OpenAPI"""  # noqa: E501

        self._store_id = None
        self._request_type = None
        self._security_code = None
        self._billing_address = None
        self.discriminator = 'request_type'

        if store_id is not None:
            self.store_id = store_id
        self.request_type = request_type
        if security_code is not None:
            self.security_code = security_code
        if billing_address is not None:
            self.billing_address = billing_address

    @property
    def store_id(self):
        """Gets the store_id of this AuthenticationVerificationRequest.  # noqa: E501

        An optional Outlet ID for clients that support multiple stores in the same developer app.  # noqa: E501

        :return: The store_id of this AuthenticationVerificationRequest.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this AuthenticationVerificationRequest.

        An optional Outlet ID for clients that support multiple stores in the same developer app.  # noqa: E501

        :param store_id: The store_id of this AuthenticationVerificationRequest.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def request_type(self):
        """Gets the request_type of this AuthenticationVerificationRequest.  # noqa: E501

        Object name of the authentication verification request.  # noqa: E501

        :return: The request_type of this AuthenticationVerificationRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this AuthenticationVerificationRequest.

        Object name of the authentication verification request.  # noqa: E501

        :param request_type: The request_type of this AuthenticationVerificationRequest.  # noqa: E501
        :type: str
        """
        if request_type is None:
            raise ValueError("Invalid value for `request_type`, must not be `None`")  # noqa: E501

        self._request_type = request_type

    @property
    def security_code(self):
        """Gets the security_code of this AuthenticationVerificationRequest.  # noqa: E501

        Card security code if required by merchant.  # noqa: E501

        :return: The security_code of this AuthenticationVerificationRequest.  # noqa: E501
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """Sets the security_code of this AuthenticationVerificationRequest.

        Card security code if required by merchant.  # noqa: E501

        :param security_code: The security_code of this AuthenticationVerificationRequest.  # noqa: E501
        :type: str
        """

        self._security_code = security_code

    @property
    def billing_address(self):
        """Gets the billing_address of this AuthenticationVerificationRequest.  # noqa: E501


        :return: The billing_address of this AuthenticationVerificationRequest.  # noqa: E501
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this AuthenticationVerificationRequest.


        :param billing_address: The billing_address of this AuthenticationVerificationRequest.  # noqa: E501
        :type: Address
        """

        self._billing_address = billing_address

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, AuthenticationVerificationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
