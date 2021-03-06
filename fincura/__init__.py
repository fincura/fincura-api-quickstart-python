# coding: utf-8

# flake8: noqa

"""
    Fincura Integration API

    This [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer) allows you to interact with the Fincura processing and insights engine.   # Authentication  This API uses API keys generated from a Fincura User account. To get access to your User account, speak with you Fincura account manager.  # Accepted Media Types  | File&nbsp;Type&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Extension(s)     | Content-Type(s) | | -------------------------------- |-------------- | ------------ | | PDF File | .pdf | `application/pdf` , `application/x-pdf` | | Excel File | .xls | `application/vnd.ms-excel`  | | Excel File | .xlsx | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`  | | PNG Image | .png | `image/png`  | | GIF Image | .gif | `image/gif`  | | JPG Image | .jpg, .jpeg | `image/jpeg`  | | GIF Image | .gif | `image/gif`  |   # Getting Started  1. [Create a Borrower](#operation/createBorrower)  2. [Add a file](#operation/createDocumentFile) for that Borrower. 3. Analyze in the Fincura App  ****  # noqa: E501

    The version of the OpenAPI document: 1.2.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from fincura.api.api_key_api import ApiKeyApi
from fincura.api.borrowers_api import BorrowersApi
from fincura.api.data_views_api import DataViewsApi
from fincura.api.embedded_workflows_api import EmbeddedWorkflowsApi
from fincura.api.files_api import FilesApi
from fincura.api.loans_api import LoansApi
from fincura.api.portfolios_api import PortfoliosApi
from fincura.api.requirements_api import RequirementsApi
from fincura.api.webhooks_api import WebhooksApi

# import ApiClient
from fincura.api_client import ApiClient
from fincura.configuration import Configuration
from fincura.exceptions import OpenApiException
from fincura.exceptions import ApiTypeError
from fincura.exceptions import ApiValueError
from fincura.exceptions import ApiKeyError
from fincura.exceptions import ApiException
# import models into sdk package
from fincura.models.api_key import ApiKey
from fincura.models.borrower import Borrower
from fincura.models.data_view import DataView
from fincura.models.data_view_calculated_value import DataViewCalculatedValue
from fincura.models.data_view_calculated_value_line_item import DataViewCalculatedValueLineItem
from fincura.models.data_view_cell_format import DataViewCellFormat
from fincura.models.data_view_cells import DataViewCells
from fincura.models.data_view_columns import DataViewColumns
from fincura.models.data_view_row_format import DataViewRowFormat
from fincura.models.data_view_rows import DataViewRows
from fincura.models.document_file_create import DocumentFileCreate
from fincura.models.document_file_create_statements import DocumentFileCreateStatements
from fincura.models.document_file_read import DocumentFileRead
from fincura.models.embedded_workflow import EmbeddedWorkflow
from fincura.models.embedded_workflow_ui_controls import EmbeddedWorkflowUiControls
from fincura.models.financial_requirement import FinancialRequirement
from fincura.models.financial_requirement_rules import FinancialRequirementRules
from fincura.models.inline_response200 import InlineResponse200
from fincura.models.inline_response2001 import InlineResponse2001
from fincura.models.inline_response2002 import InlineResponse2002
from fincura.models.inline_response2003 import InlineResponse2003
from fincura.models.inline_response2004 import InlineResponse2004
from fincura.models.inline_response2005 import InlineResponse2005
from fincura.models.loan import Loan
from fincura.models.loan_borrower_info import LoanBorrowerInfo
from fincura.models.loan_compliance_info import LoanComplianceInfo
from fincura.models.loan_documents import LoanDocuments
from fincura.models.loan_financials import LoanFinancials
from fincura.models.loan_financials_calculated_value import LoanFinancialsCalculatedValue
from fincura.models.loan_financials_cells import LoanFinancialsCells
from fincura.models.loan_financials_data_columns import LoanFinancialsDataColumns
from fincura.models.loan_financials_template_items import LoanFinancialsTemplateItems
from fincura.models.loan_guarantors import LoanGuarantors
from fincura.models.loan_periods import LoanPeriods
from fincura.models.portfolio import Portfolio
from fincura.models.webhook import Webhook

