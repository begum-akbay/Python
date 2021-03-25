# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.1.0.20210122.001
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.payment_token_api import PaymentTokenApi  # noqa: E501
from openapi_client.rest import ApiException


class TestPaymentTokenApi(unittest.TestCase):
    """PaymentTokenApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.payment_token_api.PaymentTokenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_payment_token(self):
        """Test case for create_payment_token

        Create a payment token from a payment card.  # noqa: E501
        """
        pass

    def test_delete_payment_token(self):
        """Test case for delete_payment_token

        Delete a payment token.  # noqa: E501
        """
        pass

    def test_get_payment_token_details(self):
        """Test case for get_payment_token_details

        Get payment card details associated with token.  # noqa: E501
        """
        pass

    def test_update_payment_token(self):
        """Test case for update_payment_token

        Update one or more payment tokens.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
