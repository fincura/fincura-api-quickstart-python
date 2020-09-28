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


class Loan(object):
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
        'uuid': 'str',
        'title': 'str',
        'description': 'str',
        'created_date': 'datetime',
        'external_id': 'str',
        'borrower_uuid': 'str',
        'borrower_info': 'LoanBorrowerInfo',
        'principal': 'float',
        'interest_rate': 'float',
        'interest_type': 'str',
        'term_months': 'int',
        'payment_type': 'str',
        'state': 'str',
        'payment_status': 'str',
        'start_date': 'date',
        'end_date': 'date',
        'monthly_payment': 'float',
        'payments_remaining': 'int',
        'outstanding_principal': 'float',
        'interest_accrued': 'float',
        'loan_to_value': 'float',
        'scorecard': 'bool',
        'collateral_type': 'str',
        'collateral_value': 'float',
        'collateral_life_months': 'int',
        'residual_value': 'float',
        'balloon_payment': 'float',
        'last_payment_date': 'date',
        'compliance_info': 'LoanComplianceInfo',
        'template_uuid': 'str',
        'periods': 'list[LoanPeriods]',
        'documents': 'list[LoanDocuments]',
        'financials': 'LoanFinancials',
        'guarantors': 'list[LoanGuarantors]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'title': 'title',
        'description': 'description',
        'created_date': 'created_date',
        'external_id': 'external_id',
        'borrower_uuid': 'borrower_uuid',
        'borrower_info': 'borrower_info',
        'principal': 'principal',
        'interest_rate': 'interest_rate',
        'interest_type': 'interest_type',
        'term_months': 'term_months',
        'payment_type': 'payment_type',
        'state': 'state',
        'payment_status': 'payment_status',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'monthly_payment': 'monthly_payment',
        'payments_remaining': 'payments_remaining',
        'outstanding_principal': 'outstanding_principal',
        'interest_accrued': 'interest_accrued',
        'loan_to_value': 'loan_to_value',
        'scorecard': 'scorecard',
        'collateral_type': 'collateral_type',
        'collateral_value': 'collateral_value',
        'collateral_life_months': 'collateral_life_months',
        'residual_value': 'residual_value',
        'balloon_payment': 'balloon_payment',
        'last_payment_date': 'last_payment_date',
        'compliance_info': 'compliance_info',
        'template_uuid': 'template_uuid',
        'periods': 'periods',
        'documents': 'documents',
        'financials': 'financials',
        'guarantors': 'guarantors'
    }

    def __init__(self, uuid=None, title=None, description=None, created_date=None, external_id=None, borrower_uuid=None, borrower_info=None, principal=None, interest_rate=None, interest_type=None, term_months=None, payment_type=None, state=None, payment_status=None, start_date=None, end_date=None, monthly_payment=None, payments_remaining=None, outstanding_principal=None, interest_accrued=None, loan_to_value=None, scorecard=None, collateral_type=None, collateral_value=None, collateral_life_months=None, residual_value=None, balloon_payment=None, last_payment_date=None, compliance_info=None, template_uuid=None, periods=None, documents=None, financials=None, guarantors=None, local_vars_configuration=None):  # noqa: E501
        """Loan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._title = None
        self._description = None
        self._created_date = None
        self._external_id = None
        self._borrower_uuid = None
        self._borrower_info = None
        self._principal = None
        self._interest_rate = None
        self._interest_type = None
        self._term_months = None
        self._payment_type = None
        self._state = None
        self._payment_status = None
        self._start_date = None
        self._end_date = None
        self._monthly_payment = None
        self._payments_remaining = None
        self._outstanding_principal = None
        self._interest_accrued = None
        self._loan_to_value = None
        self._scorecard = None
        self._collateral_type = None
        self._collateral_value = None
        self._collateral_life_months = None
        self._residual_value = None
        self._balloon_payment = None
        self._last_payment_date = None
        self._compliance_info = None
        self._template_uuid = None
        self._periods = None
        self._documents = None
        self._financials = None
        self._guarantors = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        self.title = title
        self.description = description
        if created_date is not None:
            self.created_date = created_date
        self.external_id = external_id
        self.borrower_uuid = borrower_uuid
        self.borrower_info = borrower_info
        self.principal = principal
        if interest_rate is not None:
            self.interest_rate = interest_rate
        self.interest_type = interest_type
        self.term_months = term_months
        self.payment_type = payment_type
        if state is not None:
            self.state = state
        if payment_status is not None:
            self.payment_status = payment_status
        self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if monthly_payment is not None:
            self.monthly_payment = monthly_payment
        if payments_remaining is not None:
            self.payments_remaining = payments_remaining
        if outstanding_principal is not None:
            self.outstanding_principal = outstanding_principal
        if interest_accrued is not None:
            self.interest_accrued = interest_accrued
        if loan_to_value is not None:
            self.loan_to_value = loan_to_value
        self.scorecard = scorecard
        if collateral_type is not None:
            self.collateral_type = collateral_type
        self.collateral_value = collateral_value
        if collateral_life_months is not None:
            self.collateral_life_months = collateral_life_months
        self.residual_value = residual_value
        self.balloon_payment = balloon_payment
        self.last_payment_date = last_payment_date
        self.compliance_info = compliance_info
        if template_uuid is not None:
            self.template_uuid = template_uuid
        if periods is not None:
            self.periods = periods
        if documents is not None:
            self.documents = documents
        if financials is not None:
            self.financials = financials
        if guarantors is not None:
            self.guarantors = guarantors

    @property
    def uuid(self):
        """Gets the uuid of this Loan.  # noqa: E501


        :return: The uuid of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Loan.


        :param uuid: The uuid of this Loan.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def title(self):
        """Gets the title of this Loan.  # noqa: E501

        Title of the Loan. Must be unique for the Borrower  # noqa: E501

        :return: The title of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Loan.

        Title of the Loan. Must be unique for the Borrower  # noqa: E501

        :param title: The title of this Loan.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) > 200):
            raise ValueError("Invalid value for `title`, length must be less than or equal to `200`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this Loan.  # noqa: E501


        :return: The description of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Loan.


        :param description: The description of this Loan.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created_date(self):
        """Gets the created_date of this Loan.  # noqa: E501


        :return: The created_date of this Loan.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Loan.


        :param created_date: The created_date of this Loan.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def external_id(self):
        """Gets the external_id of this Loan.  # noqa: E501

        External ID is used to uniquely identify a record from your system in our system. Must be unique across records.  # noqa: E501

        :return: The external_id of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Loan.

        External ID is used to uniquely identify a record from your system in our system. Must be unique across records.  # noqa: E501

        :param external_id: The external_id of this Loan.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                external_id is not None and len(external_id) > 250):
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `250`")  # noqa: E501

        self._external_id = external_id

    @property
    def borrower_uuid(self):
        """Gets the borrower_uuid of this Loan.  # noqa: E501

        UUID of the borrower for this loan. (see [Borrowers](#tag/Borrowers))  # noqa: E501

        :return: The borrower_uuid of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._borrower_uuid

    @borrower_uuid.setter
    def borrower_uuid(self, borrower_uuid):
        """Sets the borrower_uuid of this Loan.

        UUID of the borrower for this loan. (see [Borrowers](#tag/Borrowers))  # noqa: E501

        :param borrower_uuid: The borrower_uuid of this Loan.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and borrower_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `borrower_uuid`, must not be `None`")  # noqa: E501

        self._borrower_uuid = borrower_uuid

    @property
    def borrower_info(self):
        """Gets the borrower_info of this Loan.  # noqa: E501


        :return: The borrower_info of this Loan.  # noqa: E501
        :rtype: LoanBorrowerInfo
        """
        return self._borrower_info

    @borrower_info.setter
    def borrower_info(self, borrower_info):
        """Sets the borrower_info of this Loan.


        :param borrower_info: The borrower_info of this Loan.  # noqa: E501
        :type: LoanBorrowerInfo
        """
        if self.local_vars_configuration.client_side_validation and borrower_info is None:  # noqa: E501
            raise ValueError("Invalid value for `borrower_info`, must not be `None`")  # noqa: E501

        self._borrower_info = borrower_info

    @property
    def principal(self):
        """Gets the principal of this Loan.  # noqa: E501

        Original principal value  # noqa: E501

        :return: The principal of this Loan.  # noqa: E501
        :rtype: float
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this Loan.

        Original principal value  # noqa: E501

        :param principal: The principal of this Loan.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and principal is None:  # noqa: E501
            raise ValueError("Invalid value for `principal`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                principal is not None and principal > 1000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `principal`, must be a value less than or equal to `1000000000000000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                principal is not None and principal < 0):  # noqa: E501
            raise ValueError("Invalid value for `principal`, must be a value greater than or equal to `0`")  # noqa: E501

        self._principal = principal

    @property
    def interest_rate(self):
        """Gets the interest_rate of this Loan.  # noqa: E501


        :return: The interest_rate of this Loan.  # noqa: E501
        :rtype: float
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this Loan.


        :param interest_rate: The interest_rate of this Loan.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                interest_rate is not None and interest_rate > 100):  # noqa: E501
            raise ValueError("Invalid value for `interest_rate`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                interest_rate is not None and interest_rate < 0):  # noqa: E501
            raise ValueError("Invalid value for `interest_rate`, must be a value greater than or equal to `0`")  # noqa: E501

        self._interest_rate = interest_rate

    @property
    def interest_type(self):
        """Gets the interest_type of this Loan.  # noqa: E501


        :return: The interest_type of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._interest_type

    @interest_type.setter
    def interest_type(self, interest_type):
        """Sets the interest_type of this Loan.


        :param interest_type: The interest_type of this Loan.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and interest_type is None:  # noqa: E501
            raise ValueError("Invalid value for `interest_type`, must not be `None`")  # noqa: E501
        allowed_values = ["FIXED", "ADJUSTABLE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and interest_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `interest_type` ({0}), must be one of {1}"  # noqa: E501
                .format(interest_type, allowed_values)
            )

        self._interest_type = interest_type

    @property
    def term_months(self):
        """Gets the term_months of this Loan.  # noqa: E501


        :return: The term_months of this Loan.  # noqa: E501
        :rtype: int
        """
        return self._term_months

    @term_months.setter
    def term_months(self, term_months):
        """Sets the term_months of this Loan.


        :param term_months: The term_months of this Loan.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and term_months is None:  # noqa: E501
            raise ValueError("Invalid value for `term_months`, must not be `None`")  # noqa: E501

        self._term_months = term_months

    @property
    def payment_type(self):
        """Gets the payment_type of this Loan.  # noqa: E501


        :return: The payment_type of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this Loan.


        :param payment_type: The payment_type of this Loan.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and payment_type is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_type`, must not be `None`")  # noqa: E501
        allowed_values = ["PRINCIPAL_AND_INTEREST", "PRINCIPAL_PLUS_INTEREST", "IO_PERIOD", "BALLON"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and payment_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `payment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_type, allowed_values)
            )

        self._payment_type = payment_type

    @property
    def state(self):
        """Gets the state of this Loan.  # noqa: E501


        :return: The state of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Loan.


        :param state: The state of this Loan.  # noqa: E501
        :type: str
        """
        allowed_values = ["PROPOSED", "BOOKED_ACTIVE", "BOOKED_PAID_OFF", "DECLINED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def payment_status(self):
        """Gets the payment_status of this Loan.  # noqa: E501


        :return: The payment_status of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        """Sets the payment_status of this Loan.


        :param payment_status: The payment_status of this Loan.  # noqa: E501
        :type: str
        """
        allowed_values = ["CURRENT", "GRACE_PERIOD", "DELINQUENT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and payment_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `payment_status` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_status, allowed_values)
            )

        self._payment_status = payment_status

    @property
    def start_date(self):
        """Gets the start_date of this Loan.  # noqa: E501


        :return: The start_date of this Loan.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Loan.


        :param start_date: The start_date of this Loan.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Loan.  # noqa: E501

        Loan end date. Calculated field  # noqa: E501

        :return: The end_date of this Loan.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Loan.

        Loan end date. Calculated field  # noqa: E501

        :param end_date: The end_date of this Loan.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def monthly_payment(self):
        """Gets the monthly_payment of this Loan.  # noqa: E501

        calculated field  # noqa: E501

        :return: The monthly_payment of this Loan.  # noqa: E501
        :rtype: float
        """
        return self._monthly_payment

    @monthly_payment.setter
    def monthly_payment(self, monthly_payment):
        """Sets the monthly_payment of this Loan.

        calculated field  # noqa: E501

        :param monthly_payment: The monthly_payment of this Loan.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                monthly_payment is not None and monthly_payment > 1000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `monthly_payment`, must be a value less than or equal to `1000000000000000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                monthly_payment is not None and monthly_payment < -1000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `monthly_payment`, must be a value greater than or equal to `-1000000000000000000`")  # noqa: E501

        self._monthly_payment = monthly_payment

    @property
    def payments_remaining(self):
        """Gets the payments_remaining of this Loan.  # noqa: E501

        Calculated field  # noqa: E501

        :return: The payments_remaining of this Loan.  # noqa: E501
        :rtype: int
        """
        return self._payments_remaining

    @payments_remaining.setter
    def payments_remaining(self, payments_remaining):
        """Sets the payments_remaining of this Loan.

        Calculated field  # noqa: E501

        :param payments_remaining: The payments_remaining of this Loan.  # noqa: E501
        :type: int
        """

        self._payments_remaining = payments_remaining

    @property
    def outstanding_principal(self):
        """Gets the outstanding_principal of this Loan.  # noqa: E501

        calculated field  # noqa: E501

        :return: The outstanding_principal of this Loan.  # noqa: E501
        :rtype: float
        """
        return self._outstanding_principal

    @outstanding_principal.setter
    def outstanding_principal(self, outstanding_principal):
        """Sets the outstanding_principal of this Loan.

        calculated field  # noqa: E501

        :param outstanding_principal: The outstanding_principal of this Loan.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                outstanding_principal is not None and outstanding_principal > 1000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `outstanding_principal`, must be a value less than or equal to `1000000000000000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                outstanding_principal is not None and outstanding_principal < -1000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `outstanding_principal`, must be a value greater than or equal to `-1000000000000000000`")  # noqa: E501

        self._outstanding_principal = outstanding_principal

    @property
    def interest_accrued(self):
        """Gets the interest_accrued of this Loan.  # noqa: E501

        calculated field  # noqa: E501

        :return: The interest_accrued of this Loan.  # noqa: E501
        :rtype: float
        """
        return self._interest_accrued

    @interest_accrued.setter
    def interest_accrued(self, interest_accrued):
        """Sets the interest_accrued of this Loan.

        calculated field  # noqa: E501

        :param interest_accrued: The interest_accrued of this Loan.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                interest_accrued is not None and interest_accrued > 1000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `interest_accrued`, must be a value less than or equal to `1000000000000000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                interest_accrued is not None and interest_accrued < -1000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `interest_accrued`, must be a value greater than or equal to `-1000000000000000000`")  # noqa: E501

        self._interest_accrued = interest_accrued

    @property
    def loan_to_value(self):
        """Gets the loan_to_value of this Loan.  # noqa: E501

        calculated field  # noqa: E501

        :return: The loan_to_value of this Loan.  # noqa: E501
        :rtype: float
        """
        return self._loan_to_value

    @loan_to_value.setter
    def loan_to_value(self, loan_to_value):
        """Sets the loan_to_value of this Loan.

        calculated field  # noqa: E501

        :param loan_to_value: The loan_to_value of this Loan.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                loan_to_value is not None and loan_to_value > 10000):  # noqa: E501
            raise ValueError("Invalid value for `loan_to_value`, must be a value less than or equal to `10000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                loan_to_value is not None and loan_to_value < -10000):  # noqa: E501
            raise ValueError("Invalid value for `loan_to_value`, must be a value greater than or equal to `-10000`")  # noqa: E501

        self._loan_to_value = loan_to_value

    @property
    def scorecard(self):
        """Gets the scorecard of this Loan.  # noqa: E501


        :return: The scorecard of this Loan.  # noqa: E501
        :rtype: bool
        """
        return self._scorecard

    @scorecard.setter
    def scorecard(self, scorecard):
        """Sets the scorecard of this Loan.


        :param scorecard: The scorecard of this Loan.  # noqa: E501
        :type: bool
        """

        self._scorecard = scorecard

    @property
    def collateral_type(self):
        """Gets the collateral_type of this Loan.  # noqa: E501


        :return: The collateral_type of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._collateral_type

    @collateral_type.setter
    def collateral_type(self, collateral_type):
        """Sets the collateral_type of this Loan.


        :param collateral_type: The collateral_type of this Loan.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "CASH", "AR", "IP", "REAL_ESTATE", "EQUIPMENT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and collateral_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `collateral_type` ({0}), must be one of {1}"  # noqa: E501
                .format(collateral_type, allowed_values)
            )

        self._collateral_type = collateral_type

    @property
    def collateral_value(self):
        """Gets the collateral_value of this Loan.  # noqa: E501


        :return: The collateral_value of this Loan.  # noqa: E501
        :rtype: float
        """
        return self._collateral_value

    @collateral_value.setter
    def collateral_value(self, collateral_value):
        """Sets the collateral_value of this Loan.


        :param collateral_value: The collateral_value of this Loan.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                collateral_value is not None and collateral_value > 1000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `collateral_value`, must be a value less than or equal to `1000000000000000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                collateral_value is not None and collateral_value < 0):  # noqa: E501
            raise ValueError("Invalid value for `collateral_value`, must be a value greater than or equal to `0`")  # noqa: E501

        self._collateral_value = collateral_value

    @property
    def collateral_life_months(self):
        """Gets the collateral_life_months of this Loan.  # noqa: E501

        The life of the collateral in months  # noqa: E501

        :return: The collateral_life_months of this Loan.  # noqa: E501
        :rtype: int
        """
        return self._collateral_life_months

    @collateral_life_months.setter
    def collateral_life_months(self, collateral_life_months):
        """Sets the collateral_life_months of this Loan.

        The life of the collateral in months  # noqa: E501

        :param collateral_life_months: The collateral_life_months of this Loan.  # noqa: E501
        :type: int
        """

        self._collateral_life_months = collateral_life_months

    @property
    def residual_value(self):
        """Gets the residual_value of this Loan.  # noqa: E501


        :return: The residual_value of this Loan.  # noqa: E501
        :rtype: float
        """
        return self._residual_value

    @residual_value.setter
    def residual_value(self, residual_value):
        """Sets the residual_value of this Loan.


        :param residual_value: The residual_value of this Loan.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                residual_value is not None and residual_value > 1000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `residual_value`, must be a value less than or equal to `1000000000000000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                residual_value is not None and residual_value < 0):  # noqa: E501
            raise ValueError("Invalid value for `residual_value`, must be a value greater than or equal to `0`")  # noqa: E501

        self._residual_value = residual_value

    @property
    def balloon_payment(self):
        """Gets the balloon_payment of this Loan.  # noqa: E501


        :return: The balloon_payment of this Loan.  # noqa: E501
        :rtype: float
        """
        return self._balloon_payment

    @balloon_payment.setter
    def balloon_payment(self, balloon_payment):
        """Sets the balloon_payment of this Loan.


        :param balloon_payment: The balloon_payment of this Loan.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                balloon_payment is not None and balloon_payment > 1000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `balloon_payment`, must be a value less than or equal to `1000000000000000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                balloon_payment is not None and balloon_payment < 0):  # noqa: E501
            raise ValueError("Invalid value for `balloon_payment`, must be a value greater than or equal to `0`")  # noqa: E501

        self._balloon_payment = balloon_payment

    @property
    def last_payment_date(self):
        """Gets the last_payment_date of this Loan.  # noqa: E501


        :return: The last_payment_date of this Loan.  # noqa: E501
        :rtype: date
        """
        return self._last_payment_date

    @last_payment_date.setter
    def last_payment_date(self, last_payment_date):
        """Sets the last_payment_date of this Loan.


        :param last_payment_date: The last_payment_date of this Loan.  # noqa: E501
        :type: date
        """

        self._last_payment_date = last_payment_date

    @property
    def compliance_info(self):
        """Gets the compliance_info of this Loan.  # noqa: E501


        :return: The compliance_info of this Loan.  # noqa: E501
        :rtype: LoanComplianceInfo
        """
        return self._compliance_info

    @compliance_info.setter
    def compliance_info(self, compliance_info):
        """Sets the compliance_info of this Loan.


        :param compliance_info: The compliance_info of this Loan.  # noqa: E501
        :type: LoanComplianceInfo
        """
        if self.local_vars_configuration.client_side_validation and compliance_info is None:  # noqa: E501
            raise ValueError("Invalid value for `compliance_info`, must not be `None`")  # noqa: E501

        self._compliance_info = compliance_info

    @property
    def template_uuid(self):
        """Gets the template_uuid of this Loan.  # noqa: E501

        DSRC template to use for finanical information  # noqa: E501

        :return: The template_uuid of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._template_uuid

    @template_uuid.setter
    def template_uuid(self, template_uuid):
        """Sets the template_uuid of this Loan.

        DSRC template to use for finanical information  # noqa: E501

        :param template_uuid: The template_uuid of this Loan.  # noqa: E501
        :type: str
        """

        self._template_uuid = template_uuid

    @property
    def periods(self):
        """Gets the periods of this Loan.  # noqa: E501

        ReportingPeriod's to include in the loan financial information  # noqa: E501

        :return: The periods of this Loan.  # noqa: E501
        :rtype: list[LoanPeriods]
        """
        return self._periods

    @periods.setter
    def periods(self, periods):
        """Sets the periods of this Loan.

        ReportingPeriod's to include in the loan financial information  # noqa: E501

        :param periods: The periods of this Loan.  # noqa: E501
        :type: list[LoanPeriods]
        """

        self._periods = periods

    @property
    def documents(self):
        """Gets the documents of this Loan.  # noqa: E501

        Additional DocumentFile's to be included with loan information  # noqa: E501

        :return: The documents of this Loan.  # noqa: E501
        :rtype: list[LoanDocuments]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this Loan.

        Additional DocumentFile's to be included with loan information  # noqa: E501

        :param documents: The documents of this Loan.  # noqa: E501
        :type: list[LoanDocuments]
        """

        self._documents = documents

    @property
    def financials(self):
        """Gets the financials of this Loan.  # noqa: E501


        :return: The financials of this Loan.  # noqa: E501
        :rtype: LoanFinancials
        """
        return self._financials

    @financials.setter
    def financials(self, financials):
        """Sets the financials of this Loan.


        :param financials: The financials of this Loan.  # noqa: E501
        :type: LoanFinancials
        """

        self._financials = financials

    @property
    def guarantors(self):
        """Gets the guarantors of this Loan.  # noqa: E501


        :return: The guarantors of this Loan.  # noqa: E501
        :rtype: list[LoanGuarantors]
        """
        return self._guarantors

    @guarantors.setter
    def guarantors(self, guarantors):
        """Sets the guarantors of this Loan.


        :param guarantors: The guarantors of this Loan.  # noqa: E501
        :type: list[LoanGuarantors]
        """

        self._guarantors = guarantors

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
        if not isinstance(other, Loan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Loan):
            return True

        return self.to_dict() != other.to_dict()
