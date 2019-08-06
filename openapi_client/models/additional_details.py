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


class AdditionalDetails(object):
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
        'comments': 'str',
        'invoice_number': 'str',
        'purchase_order_number': 'str'
    }

    attribute_map = {
        'comments': 'comments',
        'invoice_number': 'invoiceNumber',
        'purchase_order_number': 'purchaseOrderNumber'
    }

    def __init__(self, comments=None, invoice_number=None, purchase_order_number=None):  # noqa: E501
        """AdditionalDetails - a model defined in OpenAPI"""  # noqa: E501

        self._comments = None
        self._invoice_number = None
        self._purchase_order_number = None
        self.discriminator = None

        if comments is not None:
            self.comments = comments
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number

    @property
    def comments(self):
        """Gets the comments of this AdditionalDetails.  # noqa: E501

        Comments for the payment.  # noqa: E501

        :return: The comments of this AdditionalDetails.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this AdditionalDetails.

        Comments for the payment.  # noqa: E501

        :param comments: The comments of this AdditionalDetails.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 1024:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `1024`")  # noqa: E501

        self._comments = comments

    @property
    def invoice_number(self):
        """Gets the invoice_number of this AdditionalDetails.  # noqa: E501

        Invoice number.  # noqa: E501

        :return: The invoice_number of this AdditionalDetails.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this AdditionalDetails.

        Invoice number.  # noqa: E501

        :param invoice_number: The invoice_number of this AdditionalDetails.  # noqa: E501
        :type: str
        """
        if invoice_number is not None and len(invoice_number) > 48:
            raise ValueError("Invalid value for `invoice_number`, length must be less than or equal to `48`")  # noqa: E501

        self._invoice_number = invoice_number

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this AdditionalDetails.  # noqa: E501

        Purchase order number.  # noqa: E501

        :return: The purchase_order_number of this AdditionalDetails.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this AdditionalDetails.

        Purchase order number.  # noqa: E501

        :param purchase_order_number: The purchase_order_number of this AdditionalDetails.  # noqa: E501
        :type: str
        """
        if purchase_order_number is not None and len(purchase_order_number) > 128:
            raise ValueError("Invalid value for `purchase_order_number`, length must be less than or equal to `128`")  # noqa: E501

        self._purchase_order_number = purchase_order_number

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
        if not isinstance(other, AdditionalDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
