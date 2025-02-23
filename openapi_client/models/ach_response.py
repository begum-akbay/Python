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


class AchResponse(object):
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
        'response_code': 'str',
        'approval_code': 'str',
        'reference_number': 'str',
        'preferred_flag': 'str',
        'transaction_status': 'str'
    }

    attribute_map = {
        'response_code': 'responseCode',
        'approval_code': 'approvalCode',
        'reference_number': 'referenceNumber',
        'preferred_flag': 'preferredFlag',
        'transaction_status': 'transactionStatus'
    }

    def __init__(self, response_code=None, approval_code=None, reference_number=None, preferred_flag=None, transaction_status=None):  # noqa: E501
        """AchResponse - a model defined in OpenAPI"""  # noqa: E501

        self._response_code = None
        self._approval_code = None
        self._reference_number = None
        self._preferred_flag = None
        self._transaction_status = None
        self.discriminator = None

        if response_code is not None:
            self.response_code = response_code
        if approval_code is not None:
            self.approval_code = approval_code
        if reference_number is not None:
            self.reference_number = reference_number
        if preferred_flag is not None:
            self.preferred_flag = preferred_flag
        if transaction_status is not None:
            self.transaction_status = transaction_status

    @property
    def response_code(self):
        """Gets the response_code of this AchResponse.  # noqa: E501

        Response code for TeleCheck authentication decision in the sale response message.  # noqa: E501

        :return: The response_code of this AchResponse.  # noqa: E501
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this AchResponse.

        Response code for TeleCheck authentication decision in the sale response message.  # noqa: E501

        :param response_code: The response_code of this AchResponse.  # noqa: E501
        :type: str
        """
        if response_code is not None and len(response_code) > 2:
            raise ValueError("Invalid value for `response_code`, length must be less than or equal to `2`")  # noqa: E501

        self._response_code = response_code

    @property
    def approval_code(self):
        """Gets the approval_code of this AchResponse.  # noqa: E501

        Code provided if check is approved.  # noqa: E501

        :return: The approval_code of this AchResponse.  # noqa: E501
        :rtype: str
        """
        return self._approval_code

    @approval_code.setter
    def approval_code(self, approval_code):
        """Sets the approval_code of this AchResponse.

        Code provided if check is approved.  # noqa: E501

        :param approval_code: The approval_code of this AchResponse.  # noqa: E501
        :type: str
        """
        if approval_code is not None and len(approval_code) > 4:
            raise ValueError("Invalid value for `approval_code`, length must be less than or equal to `4`")  # noqa: E501

        self._approval_code = approval_code

    @property
    def reference_number(self):
        """Gets the reference_number of this AchResponse.  # noqa: E501

        Reference number.  # noqa: E501

        :return: The reference_number of this AchResponse.  # noqa: E501
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this AchResponse.

        Reference number.  # noqa: E501

        :param reference_number: The reference_number of this AchResponse.  # noqa: E501
        :type: str
        """

        self._reference_number = reference_number

    @property
    def preferred_flag(self):
        """Gets the preferred_flag of this AchResponse.  # noqa: E501

        Preferred flag.  # noqa: E501

        :return: The preferred_flag of this AchResponse.  # noqa: E501
        :rtype: str
        """
        return self._preferred_flag

    @preferred_flag.setter
    def preferred_flag(self, preferred_flag):
        """Sets the preferred_flag of this AchResponse.

        Preferred flag.  # noqa: E501

        :param preferred_flag: The preferred_flag of this AchResponse.  # noqa: E501
        :type: str
        """
        # if preferred_flag is not None and len(preferred_flag) > 1:
        #     raise ValueError("Invalid value for `preferred_flag`, length must be less than or equal to `1`")  # noqa: E501

        self._preferred_flag = preferred_flag

    @property
    def transaction_status(self):
        """Gets the transaction_status of this AchResponse.  # noqa: E501

        Indicates the result of the requested authorization and is returned in the sale response.  # noqa: E501

        :return: The transaction_status of this AchResponse.  # noqa: E501
        :rtype: str
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status):
        """Sets the transaction_status of this AchResponse.

        Indicates the result of the requested authorization and is returned in the sale response.  # noqa: E501

        :param transaction_status: The transaction_status of this AchResponse.  # noqa: E501
        :type: str
        """
        # if transaction_status is not None and len(transaction_status) > 1:
        #     raise ValueError("Invalid value for `transaction_status`, length must be less than or equal to `1`")  # noqa: E501

        self._transaction_status = transaction_status

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
        if not isinstance(other, AchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
