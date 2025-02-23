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


class PurchaseCardsLevel2(object):
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
        'customer_reference_id': 'str',
        'supplier_invoice_number': 'str',
        'supplier_vat_registration_number': 'str',
        'total_discount_amount_and_rate': 'AdditionalAmountRate',
        'vat_shipping_amount_and_rate': 'AdditionalAmountRate'
    }

    attribute_map = {
        'customer_reference_id': 'customerReferenceID',
        'supplier_invoice_number': 'supplierInvoiceNumber',
        'supplier_vat_registration_number': 'supplierVATRegistrationNumber',
        'total_discount_amount_and_rate': 'totalDiscountAmountAndRate',
        'vat_shipping_amount_and_rate': 'vatShippingAmountAndRate'
    }

    def __init__(self, customer_reference_id=None, supplier_invoice_number=None, supplier_vat_registration_number=None, total_discount_amount_and_rate=None, vat_shipping_amount_and_rate=None):  # noqa: E501
        """PurchaseCardsLevel2 - a model defined in OpenAPI"""  # noqa: E501

        self._customer_reference_id = None
        self._supplier_invoice_number = None
        self._supplier_vat_registration_number = None
        self._total_discount_amount_and_rate = None
        self._vat_shipping_amount_and_rate = None
        self.discriminator = None

        if customer_reference_id is not None:
            self.customer_reference_id = customer_reference_id
        if supplier_invoice_number is not None:
            self.supplier_invoice_number = supplier_invoice_number
        if supplier_vat_registration_number is not None:
            self.supplier_vat_registration_number = supplier_vat_registration_number
        if total_discount_amount_and_rate is not None:
            self.total_discount_amount_and_rate = total_discount_amount_and_rate
        if vat_shipping_amount_and_rate is not None:
            self.vat_shipping_amount_and_rate = vat_shipping_amount_and_rate

    @property
    def customer_reference_id(self):
        """Gets the customer_reference_id of this PurchaseCardsLevel2.  # noqa: E501

        Customer code/customer reference ID.  # noqa: E501

        :return: The customer_reference_id of this PurchaseCardsLevel2.  # noqa: E501
        :rtype: str
        """
        return self._customer_reference_id

    @customer_reference_id.setter
    def customer_reference_id(self, customer_reference_id):
        """Sets the customer_reference_id of this PurchaseCardsLevel2.

        Customer code/customer reference ID.  # noqa: E501

        :param customer_reference_id: The customer_reference_id of this PurchaseCardsLevel2.  # noqa: E501
        :type: str
        """
        if customer_reference_id is not None and len(customer_reference_id) > 20:
            raise ValueError("Invalid value for `customer_reference_id`, length must be less than or equal to `20`")  # noqa: E501

        self._customer_reference_id = customer_reference_id

    @property
    def supplier_invoice_number(self):
        """Gets the supplier_invoice_number of this PurchaseCardsLevel2.  # noqa: E501

        Purchase identifier/merchant-related data.  # noqa: E501

        :return: The supplier_invoice_number of this PurchaseCardsLevel2.  # noqa: E501
        :rtype: str
        """
        return self._supplier_invoice_number

    @supplier_invoice_number.setter
    def supplier_invoice_number(self, supplier_invoice_number):
        """Sets the supplier_invoice_number of this PurchaseCardsLevel2.

        Purchase identifier/merchant-related data.  # noqa: E501

        :param supplier_invoice_number: The supplier_invoice_number of this PurchaseCardsLevel2.  # noqa: E501
        :type: str
        """
        if supplier_invoice_number is not None and len(supplier_invoice_number) > 30:
            raise ValueError("Invalid value for `supplier_invoice_number`, length must be less than or equal to `30`")  # noqa: E501

        self._supplier_invoice_number = supplier_invoice_number

    @property
    def supplier_vat_registration_number(self):
        """Gets the supplier_vat_registration_number of this PurchaseCardsLevel2.  # noqa: E501

        Merchant VAT registration/single business reference number/merchant tax ID or corporation VAT number.  # noqa: E501

        :return: The supplier_vat_registration_number of this PurchaseCardsLevel2.  # noqa: E501
        :rtype: str
        """
        return self._supplier_vat_registration_number

    @supplier_vat_registration_number.setter
    def supplier_vat_registration_number(self, supplier_vat_registration_number):
        """Sets the supplier_vat_registration_number of this PurchaseCardsLevel2.

        Merchant VAT registration/single business reference number/merchant tax ID or corporation VAT number.  # noqa: E501

        :param supplier_vat_registration_number: The supplier_vat_registration_number of this PurchaseCardsLevel2.  # noqa: E501
        :type: str
        """
        if supplier_vat_registration_number is not None and len(supplier_vat_registration_number) > 30:
            raise ValueError("Invalid value for `supplier_vat_registration_number`, length must be less than or equal to `30`")  # noqa: E501

        self._supplier_vat_registration_number = supplier_vat_registration_number

    @property
    def total_discount_amount_and_rate(self):
        """Gets the total_discount_amount_and_rate of this PurchaseCardsLevel2.  # noqa: E501


        :return: The total_discount_amount_and_rate of this PurchaseCardsLevel2.  # noqa: E501
        :rtype: AdditionalAmountRate
        """
        return self._total_discount_amount_and_rate

    @total_discount_amount_and_rate.setter
    def total_discount_amount_and_rate(self, total_discount_amount_and_rate):
        """Sets the total_discount_amount_and_rate of this PurchaseCardsLevel2.


        :param total_discount_amount_and_rate: The total_discount_amount_and_rate of this PurchaseCardsLevel2.  # noqa: E501
        :type: AdditionalAmountRate
        """

        self._total_discount_amount_and_rate = total_discount_amount_and_rate

    @property
    def vat_shipping_amount_and_rate(self):
        """Gets the vat_shipping_amount_and_rate of this PurchaseCardsLevel2.  # noqa: E501


        :return: The vat_shipping_amount_and_rate of this PurchaseCardsLevel2.  # noqa: E501
        :rtype: AdditionalAmountRate
        """
        return self._vat_shipping_amount_and_rate

    @vat_shipping_amount_and_rate.setter
    def vat_shipping_amount_and_rate(self, vat_shipping_amount_and_rate):
        """Sets the vat_shipping_amount_and_rate of this PurchaseCardsLevel2.


        :param vat_shipping_amount_and_rate: The vat_shipping_amount_and_rate of this PurchaseCardsLevel2.  # noqa: E501
        :type: AdditionalAmountRate
        """

        self._vat_shipping_amount_and_rate = vat_shipping_amount_and_rate

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
        if not isinstance(other, PurchaseCardsLevel2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
