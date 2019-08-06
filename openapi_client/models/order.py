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


class Order(object):
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
        'order_id': 'str',
        'billing': 'Billing',
        'shipping': 'Shipping',
        'industry_specific_extensions': 'IndustrySpecificExtensions',
        'purchase_card': 'PurchaseCards',
        'installment_options': 'InstallmentOptions',
        'soft_descriptor': 'SoftDescriptor',
        'additional_details': 'AdditionalDetails'
    }

    attribute_map = {
        'order_id': 'orderId',
        'billing': 'billing',
        'shipping': 'shipping',
        'industry_specific_extensions': 'industrySpecificExtensions',
        'purchase_card': 'purchaseCard',
        'installment_options': 'installmentOptions',
        'soft_descriptor': 'softDescriptor',
        'additional_details': 'additionalDetails'
    }

    def __init__(self, order_id=None, billing=None, shipping=None, industry_specific_extensions=None, purchase_card=None, installment_options=None, soft_descriptor=None, additional_details=None):  # noqa: E501
        """Order - a model defined in OpenAPI"""  # noqa: E501

        self._order_id = None
        self._billing = None
        self._shipping = None
        self._industry_specific_extensions = None
        self._purchase_card = None
        self._installment_options = None
        self._soft_descriptor = None
        self._additional_details = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if billing is not None:
            self.billing = billing
        if shipping is not None:
            self.shipping = shipping
        if industry_specific_extensions is not None:
            self.industry_specific_extensions = industry_specific_extensions
        if purchase_card is not None:
            self.purchase_card = purchase_card
        if installment_options is not None:
            self.installment_options = installment_options
        if soft_descriptor is not None:
            self.soft_descriptor = soft_descriptor
        if additional_details is not None:
            self.additional_details = additional_details

    @property
    def order_id(self):
        """Gets the order_id of this Order.  # noqa: E501

        Client Order ID if supplied by client.  # noqa: E501

        :return: The order_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Order.

        Client Order ID if supplied by client.  # noqa: E501

        :param order_id: The order_id of this Order.  # noqa: E501
        :type: str
        """
        if order_id is not None and len(order_id) > 100:
            raise ValueError("Invalid value for `order_id`, length must be less than or equal to `100`")  # noqa: E501

        self._order_id = order_id

    @property
    def billing(self):
        """Gets the billing of this Order.  # noqa: E501


        :return: The billing of this Order.  # noqa: E501
        :rtype: Billing
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this Order.


        :param billing: The billing of this Order.  # noqa: E501
        :type: Billing
        """

        self._billing = billing

    @property
    def shipping(self):
        """Gets the shipping of this Order.  # noqa: E501


        :return: The shipping of this Order.  # noqa: E501
        :rtype: Shipping
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this Order.


        :param shipping: The shipping of this Order.  # noqa: E501
        :type: Shipping
        """

        self._shipping = shipping

    @property
    def industry_specific_extensions(self):
        """Gets the industry_specific_extensions of this Order.  # noqa: E501


        :return: The industry_specific_extensions of this Order.  # noqa: E501
        :rtype: IndustrySpecificExtensions
        """
        return self._industry_specific_extensions

    @industry_specific_extensions.setter
    def industry_specific_extensions(self, industry_specific_extensions):
        """Sets the industry_specific_extensions of this Order.


        :param industry_specific_extensions: The industry_specific_extensions of this Order.  # noqa: E501
        :type: IndustrySpecificExtensions
        """

        self._industry_specific_extensions = industry_specific_extensions

    @property
    def purchase_card(self):
        """Gets the purchase_card of this Order.  # noqa: E501


        :return: The purchase_card of this Order.  # noqa: E501
        :rtype: PurchaseCards
        """
        return self._purchase_card

    @purchase_card.setter
    def purchase_card(self, purchase_card):
        """Sets the purchase_card of this Order.


        :param purchase_card: The purchase_card of this Order.  # noqa: E501
        :type: PurchaseCards
        """

        self._purchase_card = purchase_card

    @property
    def installment_options(self):
        """Gets the installment_options of this Order.  # noqa: E501


        :return: The installment_options of this Order.  # noqa: E501
        :rtype: InstallmentOptions
        """
        return self._installment_options

    @installment_options.setter
    def installment_options(self, installment_options):
        """Sets the installment_options of this Order.


        :param installment_options: The installment_options of this Order.  # noqa: E501
        :type: InstallmentOptions
        """

        self._installment_options = installment_options

    @property
    def soft_descriptor(self):
        """Gets the soft_descriptor of this Order.  # noqa: E501


        :return: The soft_descriptor of this Order.  # noqa: E501
        :rtype: SoftDescriptor
        """
        return self._soft_descriptor

    @soft_descriptor.setter
    def soft_descriptor(self, soft_descriptor):
        """Sets the soft_descriptor of this Order.


        :param soft_descriptor: The soft_descriptor of this Order.  # noqa: E501
        :type: SoftDescriptor
        """

        self._soft_descriptor = soft_descriptor

    @property
    def additional_details(self):
        """Gets the additional_details of this Order.  # noqa: E501


        :return: The additional_details of this Order.  # noqa: E501
        :rtype: AdditionalDetails
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """Sets the additional_details of this Order.


        :param additional_details: The additional_details of this Order.  # noqa: E501
        :type: AdditionalDetails
        """

        self._additional_details = additional_details

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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
