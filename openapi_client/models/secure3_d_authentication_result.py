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


class Secure3DAuthenticationResult(object):
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
        'authentication_type': 'str',
        'cavv': 'str',
        'xid': 'str',
        'ds_transaction_id': 'str',
        'authentication_response': 'str',
        'transaction_status': 'str'
    }

    attribute_map = {
        'authentication_type': 'authenticationType',
        'cavv': 'cavv',
        'xid': 'xid',
        'ds_transaction_id': 'dsTransactionId',
        'authentication_response': 'authenticationResponse',
        'transaction_status': 'transactionStatus'
    }

    def __init__(self, authentication_type=None, cavv=None, xid=None, ds_transaction_id=None, authentication_response=None, transaction_status=None):  # noqa: E501
        """Secure3DAuthenticationResult - a model defined in OpenAPI"""  # noqa: E501

        self._authentication_type = None
        self._cavv = None
        self._xid = None
        self._ds_transaction_id = None
        self._authentication_response = None
        self._transaction_status = None
        self.discriminator = None

        self.authentication_type = authentication_type
        if cavv is not None:
            self.cavv = cavv
        if xid is not None:
            self.xid = xid
        if ds_transaction_id is not None:
            self.ds_transaction_id = ds_transaction_id
        if authentication_response is not None:
            self.authentication_response = authentication_response
        if transaction_status is not None:
            self.transaction_status = transaction_status

    @property
    def authentication_type(self):
        """Gets the authentication_type of this Secure3DAuthenticationResult.  # noqa: E501

        Specifies the version of 3DS to be used where authentication was managed outside of the gateway.  # noqa: E501

        :return: The authentication_type of this Secure3DAuthenticationResult.  # noqa: E501
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this Secure3DAuthenticationResult.

        Specifies the version of 3DS to be used where authentication was managed outside of the gateway.  # noqa: E501

        :param authentication_type: The authentication_type of this Secure3DAuthenticationResult.  # noqa: E501
        :type: str
        """
        if authentication_type is None:
            raise ValueError("Invalid value for `authentication_type`, must not be `None`")  # noqa: E501

        self._authentication_type = authentication_type

    @property
    def cavv(self):
        """Gets the cavv of this Secure3DAuthenticationResult.  # noqa: E501

        The Cardholder Authentication Verification Value (CAVV) is a cryptographic value derived by the issuer during payment authentication that can provide evidence of the results of payment authentication during an online purchase.  # noqa: E501

        :return: The cavv of this Secure3DAuthenticationResult.  # noqa: E501
        :rtype: str
        """
        return self._cavv

    @cavv.setter
    def cavv(self, cavv):
        """Sets the cavv of this Secure3DAuthenticationResult.

        The Cardholder Authentication Verification Value (CAVV) is a cryptographic value derived by the issuer during payment authentication that can provide evidence of the results of payment authentication during an online purchase.  # noqa: E501

        :param cavv: The cavv of this Secure3DAuthenticationResult.  # noqa: E501
        :type: str
        """
        if cavv is not None and len(cavv) > 32:
            raise ValueError("Invalid value for `cavv`, length must be less than or equal to `32`")  # noqa: E501
        if cavv is not None and len(cavv) < 20:
            raise ValueError("Invalid value for `cavv`, length must be greater than or equal to `20`")  # noqa: E501

        self._cavv = cavv

    @property
    def xid(self):
        """Gets the xid of this Secure3DAuthenticationResult.  # noqa: E501

        The transaction identifier (XID) is a unique tracking number set by the merchant.  # noqa: E501

        :return: The xid of this Secure3DAuthenticationResult.  # noqa: E501
        :rtype: str
        """
        return self._xid

    @xid.setter
    def xid(self, xid):
        """Sets the xid of this Secure3DAuthenticationResult.

        The transaction identifier (XID) is a unique tracking number set by the merchant.  # noqa: E501

        :param xid: The xid of this Secure3DAuthenticationResult.  # noqa: E501
        :type: str
        """
        if xid is not None and len(xid) > 32:
            raise ValueError("Invalid value for `xid`, length must be less than or equal to `32`")  # noqa: E501
        if xid is not None and len(xid) < 20:
            raise ValueError("Invalid value for `xid`, length must be greater than or equal to `20`")  # noqa: E501

        self._xid = xid

    @property
    def ds_transaction_id(self):
        """Gets the ds_transaction_id of this Secure3DAuthenticationResult.  # noqa: E501

        The response transaction UUID from the DS (directory server)  # noqa: E501

        :return: The ds_transaction_id of this Secure3DAuthenticationResult.  # noqa: E501
        :rtype: str
        """
        return self._ds_transaction_id

    @ds_transaction_id.setter
    def ds_transaction_id(self, ds_transaction_id):
        """Sets the ds_transaction_id of this Secure3DAuthenticationResult.

        The response transaction UUID from the DS (directory server)  # noqa: E501

        :param ds_transaction_id: The ds_transaction_id of this Secure3DAuthenticationResult.  # noqa: E501
        :type: str
        """

        self._ds_transaction_id = ds_transaction_id

    @property
    def authentication_response(self):
        """Gets the authentication_response of this Secure3DAuthenticationResult.  # noqa: E501

        The result of authentication attempt returned by the 3D Secure authentication process (ARes).  # noqa: E501

        :return: The authentication_response of this Secure3DAuthenticationResult.  # noqa: E501
        :rtype: str
        """
        return self._authentication_response

    @authentication_response.setter
    def authentication_response(self, authentication_response):
        """Sets the authentication_response of this Secure3DAuthenticationResult.

        The result of authentication attempt returned by the 3D Secure authentication process (ARes).  # noqa: E501

        :param authentication_response: The authentication_response of this Secure3DAuthenticationResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "N", "U", "Y", "C", "R"]  # noqa: E501
        if authentication_response not in allowed_values:
            raise ValueError(
                "Invalid value for `authentication_response` ({0}), must be one of {1}"  # noqa: E501
                .format(authentication_response, allowed_values)
            )

        self._authentication_response = authentication_response

    @property
    def transaction_status(self):
        """Gets the transaction_status of this Secure3DAuthenticationResult.  # noqa: E501

        The transaction status as returned by the 3D Secure authentication process. (CRes)  # noqa: E501

        :return: The transaction_status of this Secure3DAuthenticationResult.  # noqa: E501
        :rtype: str
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status):
        """Sets the transaction_status of this Secure3DAuthenticationResult.

        The transaction status as returned by the 3D Secure authentication process. (CRes)  # noqa: E501

        :param transaction_status: The transaction_status of this Secure3DAuthenticationResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "N", "U", "Y", "C", "R"]  # noqa: E501
        if transaction_status not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_status` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_status, allowed_values)
            )

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
        if not isinstance(other, Secure3DAuthenticationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
