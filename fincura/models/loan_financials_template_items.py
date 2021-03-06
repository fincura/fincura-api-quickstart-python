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


class LoanFinancialsTemplateItems(object):
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
        'ref': 'str',
        'label': 'str',
        'item_type': 'str',
        'text_format': 'str',
        'original_equation': 'str',
        'equation_override': 'str',
        'line_item_id': 'int',
        'display_bold': 'bool'
    }

    attribute_map = {
        'ref': 'ref',
        'label': 'label',
        'item_type': 'item_type',
        'text_format': 'text_format',
        'original_equation': 'original_equation',
        'equation_override': 'equation_override',
        'line_item_id': 'line_item_id',
        'display_bold': 'display_bold'
    }

    def __init__(self, ref=None, label=None, item_type=None, text_format=None, original_equation=None, equation_override=None, line_item_id=None, display_bold=None, local_vars_configuration=None):  # noqa: E501
        """LoanFinancialsTemplateItems - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ref = None
        self._label = None
        self._item_type = None
        self._text_format = None
        self._original_equation = None
        self._equation_override = None
        self._line_item_id = None
        self._display_bold = None
        self.discriminator = None

        if ref is not None:
            self.ref = ref
        if label is not None:
            self.label = label
        if item_type is not None:
            self.item_type = item_type
        if text_format is not None:
            self.text_format = text_format
        if original_equation is not None:
            self.original_equation = original_equation
        if equation_override is not None:
            self.equation_override = equation_override
        if line_item_id is not None:
            self.line_item_id = line_item_id
        if display_bold is not None:
            self.display_bold = display_bold

    @property
    def ref(self):
        """Gets the ref of this LoanFinancialsTemplateItems.  # noqa: E501


        :return: The ref of this LoanFinancialsTemplateItems.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this LoanFinancialsTemplateItems.


        :param ref: The ref of this LoanFinancialsTemplateItems.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def label(self):
        """Gets the label of this LoanFinancialsTemplateItems.  # noqa: E501


        :return: The label of this LoanFinancialsTemplateItems.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this LoanFinancialsTemplateItems.


        :param label: The label of this LoanFinancialsTemplateItems.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def item_type(self):
        """Gets the item_type of this LoanFinancialsTemplateItems.  # noqa: E501


        :return: The item_type of this LoanFinancialsTemplateItems.  # noqa: E501
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this LoanFinancialsTemplateItems.


        :param item_type: The item_type of this LoanFinancialsTemplateItems.  # noqa: E501
        :type: str
        """

        self._item_type = item_type

    @property
    def text_format(self):
        """Gets the text_format of this LoanFinancialsTemplateItems.  # noqa: E501


        :return: The text_format of this LoanFinancialsTemplateItems.  # noqa: E501
        :rtype: str
        """
        return self._text_format

    @text_format.setter
    def text_format(self, text_format):
        """Sets the text_format of this LoanFinancialsTemplateItems.


        :param text_format: The text_format of this LoanFinancialsTemplateItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["NUMBER", "PERCENT", "DAYS", "RATIO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and text_format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `text_format` ({0}), must be one of {1}"  # noqa: E501
                .format(text_format, allowed_values)
            )

        self._text_format = text_format

    @property
    def original_equation(self):
        """Gets the original_equation of this LoanFinancialsTemplateItems.  # noqa: E501


        :return: The original_equation of this LoanFinancialsTemplateItems.  # noqa: E501
        :rtype: str
        """
        return self._original_equation

    @original_equation.setter
    def original_equation(self, original_equation):
        """Sets the original_equation of this LoanFinancialsTemplateItems.


        :param original_equation: The original_equation of this LoanFinancialsTemplateItems.  # noqa: E501
        :type: str
        """

        self._original_equation = original_equation

    @property
    def equation_override(self):
        """Gets the equation_override of this LoanFinancialsTemplateItems.  # noqa: E501


        :return: The equation_override of this LoanFinancialsTemplateItems.  # noqa: E501
        :rtype: str
        """
        return self._equation_override

    @equation_override.setter
    def equation_override(self, equation_override):
        """Sets the equation_override of this LoanFinancialsTemplateItems.


        :param equation_override: The equation_override of this LoanFinancialsTemplateItems.  # noqa: E501
        :type: str
        """

        self._equation_override = equation_override

    @property
    def line_item_id(self):
        """Gets the line_item_id of this LoanFinancialsTemplateItems.  # noqa: E501


        :return: The line_item_id of this LoanFinancialsTemplateItems.  # noqa: E501
        :rtype: int
        """
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        """Sets the line_item_id of this LoanFinancialsTemplateItems.


        :param line_item_id: The line_item_id of this LoanFinancialsTemplateItems.  # noqa: E501
        :type: int
        """

        self._line_item_id = line_item_id

    @property
    def display_bold(self):
        """Gets the display_bold of this LoanFinancialsTemplateItems.  # noqa: E501


        :return: The display_bold of this LoanFinancialsTemplateItems.  # noqa: E501
        :rtype: bool
        """
        return self._display_bold

    @display_bold.setter
    def display_bold(self, display_bold):
        """Sets the display_bold of this LoanFinancialsTemplateItems.


        :param display_bold: The display_bold of this LoanFinancialsTemplateItems.  # noqa: E501
        :type: bool
        """

        self._display_bold = display_bold

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
        if not isinstance(other, LoanFinancialsTemplateItems):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoanFinancialsTemplateItems):
            return True

        return self.to_dict() != other.to_dict()
