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
        'purchase_order_number': 'str',
        'operator_id': 'str',
        'sales_system_id': 'str',
        'ipg_deferred_auth': 'bool',
        'high_risk_purchase_indicator': 'bool',
        'receipts': 'list[ReceiptRequestInfo]',
        'sca_exemption_type': 'str',
        'sca_visa_merchant_id': 'str'
    }

    attribute_map = {
        'comments': 'comments',
        'invoice_number': 'invoiceNumber',
        'purchase_order_number': 'purchaseOrderNumber',
        'operator_id': 'operatorId',
        'sales_system_id': 'salesSystemId',
        'ipg_deferred_auth': 'ipgDeferredAuth',
        'high_risk_purchase_indicator': 'highRiskPurchaseIndicator',
        'receipts': 'receipts',
        'sca_exemption_type': 'scaExemptionType',
        'sca_visa_merchant_id': 'scaVisaMerchantID'
    }

    def __init__(self, comments=None, invoice_number=None, purchase_order_number=None, operator_id=None, sales_system_id=None, ipg_deferred_auth=None, high_risk_purchase_indicator=None, receipts=None, sca_exemption_type=None, sca_visa_merchant_id=None):  # noqa: E501
        """AdditionalDetails - a model defined in OpenAPI"""  # noqa: E501

        self._comments = None
        self._invoice_number = None
        self._purchase_order_number = None
        self._operator_id = None
        self._sales_system_id = None
        self._ipg_deferred_auth = None
        self._high_risk_purchase_indicator = None
        self._receipts = None
        self._sca_exemption_type = None
        self._sca_visa_merchant_id = None
        self.discriminator = None

        if comments is not None:
            self.comments = comments
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if operator_id is not None:
            self.operator_id = operator_id
        if sales_system_id is not None:
            self.sales_system_id = sales_system_id
        if ipg_deferred_auth is not None:
            self.ipg_deferred_auth = ipg_deferred_auth
        if high_risk_purchase_indicator is not None:
            self.high_risk_purchase_indicator = high_risk_purchase_indicator
        if receipts is not None:
            self.receipts = receipts
        if sca_exemption_type is not None:
            self.sca_exemption_type = sca_exemption_type
        if sca_visa_merchant_id is not None:
            self.sca_visa_merchant_id = sca_visa_merchant_id

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

    @property
    def operator_id(self):
        """Gets the operator_id of this AdditionalDetails.  # noqa: E501

        The operator ID.  # noqa: E501

        :return: The operator_id of this AdditionalDetails.  # noqa: E501
        :rtype: str
        """
        return self._operator_id

    @operator_id.setter
    def operator_id(self, operator_id):
        """Sets the operator_id of this AdditionalDetails.

        The operator ID.  # noqa: E501

        :param operator_id: The operator_id of this AdditionalDetails.  # noqa: E501
        :type: str
        """
        if operator_id is not None and len(operator_id) > 35:
            raise ValueError("Invalid value for `operator_id`, length must be less than or equal to `35`")  # noqa: E501
        if operator_id is not None and not re.search(r'^\S$|^\S.*\S$', operator_id):  # noqa: E501
            raise ValueError(r"Invalid value for `operator_id`, must be a follow pattern or equal to `/^\S$|^\S.*\S$/`")  # noqa: E501

        self._operator_id = operator_id

    @property
    def sales_system_id(self):
        """Gets the sales_system_id of this AdditionalDetails.  # noqa: E501

        The sales system ID.  # noqa: E501

        :return: The sales_system_id of this AdditionalDetails.  # noqa: E501
        :rtype: str
        """
        return self._sales_system_id

    @sales_system_id.setter
    def sales_system_id(self, sales_system_id):
        """Sets the sales_system_id of this AdditionalDetails.

        The sales system ID.  # noqa: E501

        :param sales_system_id: The sales_system_id of this AdditionalDetails.  # noqa: E501
        :type: str
        """
        if sales_system_id is not None and len(sales_system_id) > 50:
            raise ValueError("Invalid value for `sales_system_id`, length must be less than or equal to `50`")  # noqa: E501
        if sales_system_id is not None and not re.search(r'^\S$|^\S.*\S$', sales_system_id):  # noqa: E501
            raise ValueError(r"Invalid value for `sales_system_id`, must be a follow pattern or equal to `/^\S$|^\S.*\S$/`")  # noqa: E501

        self._sales_system_id = sales_system_id

    @property
    def ipg_deferred_auth(self):
        """Gets the ipg_deferred_auth of this AdditionalDetails.  # noqa: E501

        Indicates if the particular transaction is a deferred authorization.  # noqa: E501

        :return: The ipg_deferred_auth of this AdditionalDetails.  # noqa: E501
        :rtype: bool
        """
        return self._ipg_deferred_auth

    @ipg_deferred_auth.setter
    def ipg_deferred_auth(self, ipg_deferred_auth):
        """Sets the ipg_deferred_auth of this AdditionalDetails.

        Indicates if the particular transaction is a deferred authorization.  # noqa: E501

        :param ipg_deferred_auth: The ipg_deferred_auth of this AdditionalDetails.  # noqa: E501
        :type: bool
        """

        self._ipg_deferred_auth = ipg_deferred_auth

    @property
    def high_risk_purchase_indicator(self):
        """Gets the high_risk_purchase_indicator of this AdditionalDetails.  # noqa: E501

        this is highRiskPurchaseIndicator.  # noqa: E501

        :return: The high_risk_purchase_indicator of this AdditionalDetails.  # noqa: E501
        :rtype: bool
        """
        return self._high_risk_purchase_indicator

    @high_risk_purchase_indicator.setter
    def high_risk_purchase_indicator(self, high_risk_purchase_indicator):
        """Sets the high_risk_purchase_indicator of this AdditionalDetails.

        this is highRiskPurchaseIndicator.  # noqa: E501

        :param high_risk_purchase_indicator: The high_risk_purchase_indicator of this AdditionalDetails.  # noqa: E501
        :type: bool
        """

        self._high_risk_purchase_indicator = high_risk_purchase_indicator

    @property
    def receipts(self):
        """Gets the receipts of this AdditionalDetails.  # noqa: E501

        Provides request information that is necessary to generate receipts.  # noqa: E501

        :return: The receipts of this AdditionalDetails.  # noqa: E501
        :rtype: list[ReceiptRequestInfo]
        """
        return self._receipts

    @receipts.setter
    def receipts(self, receipts):
        """Sets the receipts of this AdditionalDetails.

        Provides request information that is necessary to generate receipts.  # noqa: E501

        :param receipts: The receipts of this AdditionalDetails.  # noqa: E501
        :type: list[ReceiptRequestInfo]
        """

        self._receipts = receipts

    @property
    def sca_exemption_type(self):
        """Gets the sca_exemption_type of this AdditionalDetails.  # noqa: E501

        Strong customer authentication exemption type indicator.  # noqa: E501

        :return: The sca_exemption_type of this AdditionalDetails.  # noqa: E501
        :rtype: str
        """
        return self._sca_exemption_type

    @sca_exemption_type.setter
    def sca_exemption_type(self, sca_exemption_type):
        """Sets the sca_exemption_type of this AdditionalDetails.

        Strong customer authentication exemption type indicator.  # noqa: E501

        :param sca_exemption_type: The sca_exemption_type of this AdditionalDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["Low Value Exemption", "TRA Exemption", "Trusted Merchant Exemption", "SCP Exemption", "Delegated Authentication"]  # noqa: E501
        if sca_exemption_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sca_exemption_type` ({0}), must be one of {1}"  # noqa: E501
                .format(sca_exemption_type, allowed_values)
            )

        self._sca_exemption_type = sca_exemption_type

    @property
    def sca_visa_merchant_id(self):
        """Gets the sca_visa_merchant_id of this AdditionalDetails.  # noqa: E501

        Eight-character Visa merchant identifier (VMID) assigned by Visa, required for trusted merchant and delegated authentication.  # noqa: E501

        :return: The sca_visa_merchant_id of this AdditionalDetails.  # noqa: E501
        :rtype: str
        """
        return self._sca_visa_merchant_id

    @sca_visa_merchant_id.setter
    def sca_visa_merchant_id(self, sca_visa_merchant_id):
        """Sets the sca_visa_merchant_id of this AdditionalDetails.

        Eight-character Visa merchant identifier (VMID) assigned by Visa, required for trusted merchant and delegated authentication.  # noqa: E501

        :param sca_visa_merchant_id: The sca_visa_merchant_id of this AdditionalDetails.  # noqa: E501
        :type: str
        """
        if sca_visa_merchant_id is not None and len(sca_visa_merchant_id) > 8:
            raise ValueError("Invalid value for `sca_visa_merchant_id`, length must be less than or equal to `8`")  # noqa: E501

        self._sca_visa_merchant_id = sca_visa_merchant_id

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
