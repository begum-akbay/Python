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


class StoredCredential(object):
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
        'sequence': 'str',
        'scheduled': 'bool',
        'referenced_scheme_transaction_id': 'str',
        'initiator': 'str'
    }

    attribute_map = {
        'sequence': 'sequence',
        'scheduled': 'scheduled',
        'referenced_scheme_transaction_id': 'referencedSchemeTransactionId',
        'initiator': 'initiator'
    }

    def __init__(self, sequence=None, scheduled=None, referenced_scheme_transaction_id=None, initiator=None):  # noqa: E501
        """StoredCredential - a model defined in OpenAPI"""  # noqa: E501

        self._sequence = None
        self._scheduled = None
        self._referenced_scheme_transaction_id = None
        self._initiator = None
        self.discriminator = None

        self.sequence = sequence
        self.scheduled = scheduled
        if referenced_scheme_transaction_id is not None:
            self.referenced_scheme_transaction_id = referenced_scheme_transaction_id
        if initiator is not None:
            self.initiator = initiator

    @property
    def sequence(self):
        """Gets the sequence of this StoredCredential.  # noqa: E501

        Indicates if the transaction is first or subsequent. Valid values are 'FIRST' and 'SUBSEQUENT'.  # noqa: E501

        :return: The sequence of this StoredCredential.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this StoredCredential.

        Indicates if the transaction is first or subsequent. Valid values are 'FIRST' and 'SUBSEQUENT'.  # noqa: E501

        :param sequence: The sequence of this StoredCredential.  # noqa: E501
        :type: str
        """
        if sequence is None:
            raise ValueError("Invalid value for `sequence`, must not be `None`")  # noqa: E501
        allowed_values = ["FIRST", "SUBSEQUENT"]  # noqa: E501
        if sequence not in allowed_values:
            raise ValueError(
                "Invalid value for `sequence` ({0}), must be one of {1}"  # noqa: E501
                .format(sequence, allowed_values)
            )

        self._sequence = sequence

    @property
    def scheduled(self):
        """Gets the scheduled of this StoredCredential.  # noqa: E501

        Indicates if the transaction is scheduled or part of an installment.  # noqa: E501

        :return: The scheduled of this StoredCredential.  # noqa: E501
        :rtype: bool
        """
        return self._scheduled

    @scheduled.setter
    def scheduled(self, scheduled):
        """Sets the scheduled of this StoredCredential.

        Indicates if the transaction is scheduled or part of an installment.  # noqa: E501

        :param scheduled: The scheduled of this StoredCredential.  # noqa: E501
        :type: bool
        """
        if scheduled is None:
            raise ValueError("Invalid value for `scheduled`, must not be `None`")  # noqa: E501

        self._scheduled = scheduled

    @property
    def referenced_scheme_transaction_id(self):
        """Gets the referenced_scheme_transaction_id of this StoredCredential.  # noqa: E501

        The transaction ID received from schemes for the initial transaction. May be required if sequence is 'SUBSEQUENT'.  # noqa: E501

        :return: The referenced_scheme_transaction_id of this StoredCredential.  # noqa: E501
        :rtype: str
        """
        return self._referenced_scheme_transaction_id

    @referenced_scheme_transaction_id.setter
    def referenced_scheme_transaction_id(self, referenced_scheme_transaction_id):
        """Sets the referenced_scheme_transaction_id of this StoredCredential.

        The transaction ID received from schemes for the initial transaction. May be required if sequence is 'SUBSEQUENT'.  # noqa: E501

        :param referenced_scheme_transaction_id: The referenced_scheme_transaction_id of this StoredCredential.  # noqa: E501
        :type: str
        """
        if referenced_scheme_transaction_id is not None and len(referenced_scheme_transaction_id) > 50:
            raise ValueError("Invalid value for `referenced_scheme_transaction_id`, length must be less than or equal to `50`")  # noqa: E501

        self._referenced_scheme_transaction_id = referenced_scheme_transaction_id

    @property
    def initiator(self):
        """Gets the initiator of this StoredCredential.  # noqa: E501

        Indicates whether it is a merchant-initiated or explicitly consented to by card holder. Valid values are 'MERCHANT' and 'CARDHOLDER'.  # noqa: E501

        :return: The initiator of this StoredCredential.  # noqa: E501
        :rtype: str
        """
        return self._initiator

    @initiator.setter
    def initiator(self, initiator):
        """Sets the initiator of this StoredCredential.

        Indicates whether it is a merchant-initiated or explicitly consented to by card holder. Valid values are 'MERCHANT' and 'CARDHOLDER'.  # noqa: E501

        :param initiator: The initiator of this StoredCredential.  # noqa: E501
        :type: str
        """
        allowed_values = ["MERCHANT", "CARDHOLDER"]  # noqa: E501
        if initiator not in allowed_values:
            raise ValueError(
                "Invalid value for `initiator` ({0}), must be one of {1}"  # noqa: E501
                .format(initiator, allowed_values)
            )

        self._initiator = initiator

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
        if not isinstance(other, StoredCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
