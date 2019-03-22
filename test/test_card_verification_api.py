# coding: utf-8

"""
    Payment Gateway API Specification.

    Payment Gateway API for payment processing. Version 6.4.0.20181018.001   # noqa: E501

    OpenAPI spec version: 6.4.0.20181018.001
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.card_verification_api import CardVerificationApi  # noqa: E501
from openapi_client.rest import ApiException


class TestCardVerificationApi(unittest.TestCase):
    """CardVerificationApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.card_verification_api.CardVerificationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_verify_card(self):
        """Test case for verify_card

        Verify a payment card.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
