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


class ReferencedOrderPaymentTokenizationRequestAllOf(object):
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
        'request_type': 'str',
        'store_id': 'str',
        'billing_address': 'Address',
        'create_token': 'CreatePaymentToken',
        'account_verification': 'bool',
        'referenced_order_id': 'str'
    }

    attribute_map = {
        'request_type': 'requestType',
        'store_id': 'storeId',
        'billing_address': 'billingAddress',
        'create_token': 'createToken',
        'account_verification': 'accountVerification',
        'referenced_order_id': 'referencedOrderId'
    }

    def __init__(self, request_type=None, store_id=None, billing_address=None, create_token=None, account_verification=False, referenced_order_id=None):  # noqa: E501
        """ReferencedOrderPaymentTokenizationRequestAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._request_type = None
        self._store_id = None
        self._billing_address = None
        self._create_token = None
        self._account_verification = None
        self._referenced_order_id = None
        self.discriminator = None

        if request_type is not None:
            self.request_type = request_type
        if store_id is not None:
            self.store_id = store_id
        if billing_address is not None:
            self.billing_address = billing_address
        if create_token is not None:
            self.create_token = create_token
        if account_verification is not None:
            self.account_verification = account_verification
        self.referenced_order_id = referenced_order_id

    @property
    def request_type(self):
        """Gets the request_type of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501

        Object name of tokenization request.  # noqa: E501

        :return: The request_type of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this ReferencedOrderPaymentTokenizationRequestAllOf.

        Object name of tokenization request.  # noqa: E501

        :param request_type: The request_type of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501
        :type: str
        """

        self._request_type = request_type

    @property
    def store_id(self):
        """Gets the store_id of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501

        An optional outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :return: The store_id of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this ReferencedOrderPaymentTokenizationRequestAllOf.

        An optional outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :param store_id: The store_id of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = store_id

    @property
    def billing_address(self):
        """Gets the billing_address of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501


        :return: The billing_address of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this ReferencedOrderPaymentTokenizationRequestAllOf.


        :param billing_address: The billing_address of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501
        :type: Address
        """

        self._billing_address = billing_address

    @property
    def create_token(self):
        """Gets the create_token of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501


        :return: The create_token of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501
        :rtype: CreatePaymentToken
        """
        return self._create_token

    @create_token.setter
    def create_token(self, create_token):
        """Sets the create_token of this ReferencedOrderPaymentTokenizationRequestAllOf.


        :param create_token: The create_token of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501
        :type: CreatePaymentToken
        """

        self._create_token = create_token

    @property
    def account_verification(self):
        """Gets the account_verification of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501

        If the account should be verified prior to token creation.  # noqa: E501

        :return: The account_verification of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._account_verification

    @account_verification.setter
    def account_verification(self, account_verification):
        """Sets the account_verification of this ReferencedOrderPaymentTokenizationRequestAllOf.

        If the account should be verified prior to token creation.  # noqa: E501

        :param account_verification: The account_verification of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501
        :type: bool
        """

        self._account_verification = account_verification

    @property
    def referenced_order_id(self):
        """Gets the referenced_order_id of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501

        Retrieves the payment instrument information from an existing order.  # noqa: E501

        :return: The referenced_order_id of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._referenced_order_id

    @referenced_order_id.setter
    def referenced_order_id(self, referenced_order_id):
        """Sets the referenced_order_id of this ReferencedOrderPaymentTokenizationRequestAllOf.

        Retrieves the payment instrument information from an existing order.  # noqa: E501

        :param referenced_order_id: The referenced_order_id of this ReferencedOrderPaymentTokenizationRequestAllOf.  # noqa: E501
        :type: str
        """
        if referenced_order_id is None:
            raise ValueError("Invalid value for `referenced_order_id`, must not be `None`")  # noqa: E501
        if referenced_order_id is not None and not re.search(r'^(?!\s*$).+', referenced_order_id):  # noqa: E501
            raise ValueError(r"Invalid value for `referenced_order_id`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._referenced_order_id = referenced_order_id

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
        if not isinstance(other, ReferencedOrderPaymentTokenizationRequestAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
