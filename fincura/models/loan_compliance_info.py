# coding: utf-8

"""
    Fincura Integration API

    This [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer) allows you to interact with the Fincura processing and insights engine.   # Authentication  This API uses API keys generated from a Fincura User account. To get access to your User account, speak with you Fincura account manager.  # Accepted Media Types  | File&nbsp;Type&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Extension(s)     | Content-Type(s) | | -------------------------------- |-------------- | ------------ | | PDF File | .pdf | `application/pdf` , `application/x-pdf` | | Excel File | .xls | `application/vnd.ms-excel`  | | Excel File | .xlsx | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`  | | PNG Image | .png | `image/png`  | | GIF Image | .gif | `image/gif`  | | JPG Image | .jpg, .jpeg | `image/jpeg`  | | GIF Image | .gif | `image/gif`  |   # Getting Started  1. [Create a Borrower](#operation/createBorrower)  2. [Add a file](#operation/createDocumentFile) for that Borrower. 3. Analyze in the Fincura App  ****  # noqa: E501

    The version of the OpenAPI document: 1.2.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fincura.configuration import Configuration


class LoanComplianceInfo(object):
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
        'ofac_sanctions': 'bool',
        'pacer_bankruptcies': 'bool',
        'state_court_claims': 'bool',
        'divisions_of_corp_report': 'bool'
    }

    attribute_map = {
        'ofac_sanctions': 'ofac_sanctions',
        'pacer_bankruptcies': 'pacer_bankruptcies',
        'state_court_claims': 'state_court_claims',
        'divisions_of_corp_report': 'divisions_of_corp_report'
    }

    def __init__(self, ofac_sanctions=None, pacer_bankruptcies=None, state_court_claims=None, divisions_of_corp_report=None, local_vars_configuration=None):  # noqa: E501
        """LoanComplianceInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ofac_sanctions = None
        self._pacer_bankruptcies = None
        self._state_court_claims = None
        self._divisions_of_corp_report = None
        self.discriminator = None

        if ofac_sanctions is not None:
            self.ofac_sanctions = ofac_sanctions
        if pacer_bankruptcies is not None:
            self.pacer_bankruptcies = pacer_bankruptcies
        if state_court_claims is not None:
            self.state_court_claims = state_court_claims
        if divisions_of_corp_report is not None:
            self.divisions_of_corp_report = divisions_of_corp_report

    @property
    def ofac_sanctions(self):
        """Gets the ofac_sanctions of this LoanComplianceInfo.  # noqa: E501


        :return: The ofac_sanctions of this LoanComplianceInfo.  # noqa: E501
        :rtype: bool
        """
        return self._ofac_sanctions

    @ofac_sanctions.setter
    def ofac_sanctions(self, ofac_sanctions):
        """Sets the ofac_sanctions of this LoanComplianceInfo.


        :param ofac_sanctions: The ofac_sanctions of this LoanComplianceInfo.  # noqa: E501
        :type: bool
        """

        self._ofac_sanctions = ofac_sanctions

    @property
    def pacer_bankruptcies(self):
        """Gets the pacer_bankruptcies of this LoanComplianceInfo.  # noqa: E501


        :return: The pacer_bankruptcies of this LoanComplianceInfo.  # noqa: E501
        :rtype: bool
        """
        return self._pacer_bankruptcies

    @pacer_bankruptcies.setter
    def pacer_bankruptcies(self, pacer_bankruptcies):
        """Sets the pacer_bankruptcies of this LoanComplianceInfo.


        :param pacer_bankruptcies: The pacer_bankruptcies of this LoanComplianceInfo.  # noqa: E501
        :type: bool
        """

        self._pacer_bankruptcies = pacer_bankruptcies

    @property
    def state_court_claims(self):
        """Gets the state_court_claims of this LoanComplianceInfo.  # noqa: E501


        :return: The state_court_claims of this LoanComplianceInfo.  # noqa: E501
        :rtype: bool
        """
        return self._state_court_claims

    @state_court_claims.setter
    def state_court_claims(self, state_court_claims):
        """Sets the state_court_claims of this LoanComplianceInfo.


        :param state_court_claims: The state_court_claims of this LoanComplianceInfo.  # noqa: E501
        :type: bool
        """

        self._state_court_claims = state_court_claims

    @property
    def divisions_of_corp_report(self):
        """Gets the divisions_of_corp_report of this LoanComplianceInfo.  # noqa: E501


        :return: The divisions_of_corp_report of this LoanComplianceInfo.  # noqa: E501
        :rtype: bool
        """
        return self._divisions_of_corp_report

    @divisions_of_corp_report.setter
    def divisions_of_corp_report(self, divisions_of_corp_report):
        """Sets the divisions_of_corp_report of this LoanComplianceInfo.


        :param divisions_of_corp_report: The divisions_of_corp_report of this LoanComplianceInfo.  # noqa: E501
        :type: bool
        """

        self._divisions_of_corp_report = divisions_of_corp_report

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
        if not isinstance(other, LoanComplianceInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoanComplianceInfo):
            return True

        return self.to_dict() != other.to_dict()
