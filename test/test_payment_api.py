# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.14.0.20201015.001
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.payment_api import PaymentApi  # noqa: E501
from openapi_client.rest import ApiException


class TestPaymentApi(unittest.TestCase):
    """PaymentApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.payment_api.PaymentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_finalize_secure_transaction(self):
        """Test case for finalize_secure_transaction

        Update a 3DSecure or UnionPay payment and continue processing.  # noqa: E501
        """
        pass

    def test_submit_primary_transaction(self):
        """Test case for submit_primary_transaction

        Generate a primary transaction.  # noqa: E501
        """
        pass

    def test_submit_secondary_transaction(self):
        """Test case for submit_secondary_transaction

        Perform a secondary transaction.  # noqa: E501
        """
        pass

    def test_transaction_inquiry(self):
        """Test case for transaction_inquiry

        Retrieve the state of a transaction.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
