# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    OpenAPI spec version: 6.6.0.20190329.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ProcessorData(object):
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
        'reference_number': 'str',
        'authorization_code': 'str',
        'response_code': 'str',
        'network': 'str',
        'association_response_code': 'str',
        'response_message': 'str',
        'avs_response': 'AVSResponse',
        'security_code_response': 'str',
        'merchant_advice_code_indicator': 'str'
    }

    attribute_map = {
        'reference_number': 'referenceNumber',
        'authorization_code': 'authorizationCode',
        'response_code': 'responseCode',
        'network': 'network',
        'association_response_code': 'associationResponseCode',
        'response_message': 'responseMessage',
        'avs_response': 'avsResponse',
        'security_code_response': 'securityCodeResponse',
        'merchant_advice_code_indicator': 'merchantAdviceCodeIndicator'
    }

    def __init__(self, reference_number=None, authorization_code=None, response_code=None, network=None, association_response_code=None, response_message=None, avs_response=None, security_code_response=None, merchant_advice_code_indicator=None):  # noqa: E501
        """ProcessorData - a model defined in OpenAPI"""  # noqa: E501

        self._reference_number = None
        self._authorization_code = None
        self._response_code = None
        self._network = None
        self._association_response_code = None
        self._response_message = None
        self._avs_response = None
        self._security_code_response = None
        self._merchant_advice_code_indicator = None
        self.discriminator = None

        if reference_number is not None:
            self.reference_number = reference_number
        if authorization_code is not None:
            self.authorization_code = authorization_code
        if response_code is not None:
            self.response_code = response_code
        if network is not None:
            self.network = network
        if association_response_code is not None:
            self.association_response_code = association_response_code
        if response_message is not None:
            self.response_message = response_message
        if avs_response is not None:
            self.avs_response = avs_response
        if security_code_response is not None:
            self.security_code_response = security_code_response
        if merchant_advice_code_indicator is not None:
            self.merchant_advice_code_indicator = merchant_advice_code_indicator

    @property
    def reference_number(self):
        """Gets the reference_number of this ProcessorData.  # noqa: E501

        Reference transaction ID.  # noqa: E501

        :return: The reference_number of this ProcessorData.  # noqa: E501
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this ProcessorData.

        Reference transaction ID.  # noqa: E501

        :param reference_number: The reference_number of this ProcessorData.  # noqa: E501
        :type: str
        """

        self._reference_number = reference_number

    @property
    def authorization_code(self):
        """Gets the authorization_code of this ProcessorData.  # noqa: E501

        Code returned to confirm transaction.  # noqa: E501

        :return: The authorization_code of this ProcessorData.  # noqa: E501
        :rtype: str
        """
        return self._authorization_code

    @authorization_code.setter
    def authorization_code(self, authorization_code):
        """Sets the authorization_code of this ProcessorData.

        Code returned to confirm transaction.  # noqa: E501

        :param authorization_code: The authorization_code of this ProcessorData.  # noqa: E501
        :type: str
        """

        self._authorization_code = authorization_code

    @property
    def response_code(self):
        """Gets the response_code of this ProcessorData.  # noqa: E501

        Response code from endpoints.  # noqa: E501

        :return: The response_code of this ProcessorData.  # noqa: E501
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this ProcessorData.

        Response code from endpoints.  # noqa: E501

        :param response_code: The response_code of this ProcessorData.  # noqa: E501
        :type: str
        """

        self._response_code = response_code

    @property
    def network(self):
        """Gets the network of this ProcessorData.  # noqa: E501

        Network used for transaction.  # noqa: E501

        :return: The network of this ProcessorData.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this ProcessorData.

        Network used for transaction.  # noqa: E501

        :param network: The network of this ProcessorData.  # noqa: E501
        :type: str
        """

        self._network = network

    @property
    def association_response_code(self):
        """Gets the association_response_code of this ProcessorData.  # noqa: E501

        Raw response code from issuer.  # noqa: E501

        :return: The association_response_code of this ProcessorData.  # noqa: E501
        :rtype: str
        """
        return self._association_response_code

    @association_response_code.setter
    def association_response_code(self, association_response_code):
        """Sets the association_response_code of this ProcessorData.

        Raw response code from issuer.  # noqa: E501

        :param association_response_code: The association_response_code of this ProcessorData.  # noqa: E501
        :type: str
        """

        self._association_response_code = association_response_code

    @property
    def response_message(self):
        """Gets the response_message of this ProcessorData.  # noqa: E501

        Message returned from endpoints.  # noqa: E501

        :return: The response_message of this ProcessorData.  # noqa: E501
        :rtype: str
        """
        return self._response_message

    @response_message.setter
    def response_message(self, response_message):
        """Sets the response_message of this ProcessorData.

        Message returned from endpoints.  # noqa: E501

        :param response_message: The response_message of this ProcessorData.  # noqa: E501
        :type: str
        """

        self._response_message = response_message

    @property
    def avs_response(self):
        """Gets the avs_response of this ProcessorData.  # noqa: E501


        :return: The avs_response of this ProcessorData.  # noqa: E501
        :rtype: AVSResponse
        """
        return self._avs_response

    @avs_response.setter
    def avs_response(self, avs_response):
        """Sets the avs_response of this ProcessorData.


        :param avs_response: The avs_response of this ProcessorData.  # noqa: E501
        :type: AVSResponse
        """

        self._avs_response = avs_response

    @property
    def security_code_response(self):
        """Gets the security_code_response of this ProcessorData.  # noqa: E501

        Code returned for CVV.  # noqa: E501

        :return: The security_code_response of this ProcessorData.  # noqa: E501
        :rtype: str
        """
        return self._security_code_response

    @security_code_response.setter
    def security_code_response(self, security_code_response):
        """Sets the security_code_response of this ProcessorData.

        Code returned for CVV.  # noqa: E501

        :param security_code_response: The security_code_response of this ProcessorData.  # noqa: E501
        :type: str
        """
        allowed_values = ["MATCHED", "NOT_MATCHED", "NOT_PROCESSED", "NOT_PRESENT", "NOT_CERTIFIED"]  # noqa: E501
        if security_code_response not in allowed_values:
            raise ValueError(
                "Invalid value for `security_code_response` ({0}), must be one of {1}"  # noqa: E501
                .format(security_code_response, allowed_values)
            )

        self._security_code_response = security_code_response

    @property
    def merchant_advice_code_indicator(self):
        """Gets the merchant_advice_code_indicator of this ProcessorData.  # noqa: E501

        Code to map merchant advice code to ISO specification.  # noqa: E501

        :return: The merchant_advice_code_indicator of this ProcessorData.  # noqa: E501
        :rtype: str
        """
        return self._merchant_advice_code_indicator

    @merchant_advice_code_indicator.setter
    def merchant_advice_code_indicator(self, merchant_advice_code_indicator):
        """Sets the merchant_advice_code_indicator of this ProcessorData.

        Code to map merchant advice code to ISO specification.  # noqa: E501

        :param merchant_advice_code_indicator: The merchant_advice_code_indicator of this ProcessorData.  # noqa: E501
        :type: str
        """
        if merchant_advice_code_indicator is not None and not re.search(r'[0-9]{2}', merchant_advice_code_indicator):  # noqa: E501
            raise ValueError(r"Invalid value for `merchant_advice_code_indicator`, must be a follow pattern or equal to `/[0-9]{2}/`")  # noqa: E501

        self._merchant_advice_code_indicator = merchant_advice_code_indicator

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
        if not isinstance(other, ProcessorData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
