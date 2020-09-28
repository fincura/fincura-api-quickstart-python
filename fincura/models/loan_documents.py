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


class LoanDocuments(object):
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
        'status': 'str',
        'created_date': 'datetime',
        'filename': 'str',
        'statement_types': 'list[object]',
        'custom_attributes': 'object'
    }

    attribute_map = {
        'uuid': 'uuid',
        'status': 'status',
        'created_date': 'created_date',
        'filename': 'filename',
        'statement_types': 'statement_types',
        'custom_attributes': 'custom_attributes'
    }

    def __init__(self, uuid=None, status=None, created_date=None, filename=None, statement_types=["OTHER"], custom_attributes=None, local_vars_configuration=None):  # noqa: E501
        """LoanDocuments - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._status = None
        self._created_date = None
        self._filename = None
        self._statement_types = None
        self._custom_attributes = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if status is not None:
            self.status = status
        if created_date is not None:
            self.created_date = created_date
        if filename is not None:
            self.filename = filename
        if statement_types is not None:
            self.statement_types = statement_types
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes

    @property
    def uuid(self):
        """Gets the uuid of this LoanDocuments.  # noqa: E501


        :return: The uuid of this LoanDocuments.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this LoanDocuments.


        :param uuid: The uuid of this LoanDocuments.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def status(self):
        """Gets the status of this LoanDocuments.  # noqa: E501


        :return: The status of this LoanDocuments.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LoanDocuments.


        :param status: The status of this LoanDocuments.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def created_date(self):
        """Gets the created_date of this LoanDocuments.  # noqa: E501


        :return: The created_date of this LoanDocuments.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this LoanDocuments.


        :param created_date: The created_date of this LoanDocuments.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def filename(self):
        """Gets the filename of this LoanDocuments.  # noqa: E501


        :return: The filename of this LoanDocuments.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this LoanDocuments.


        :param filename: The filename of this LoanDocuments.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                filename is not None and len(filename) > 200):
            raise ValueError("Invalid value for `filename`, length must be less than or equal to `200`")  # noqa: E501

        self._filename = filename

    @property
    def statement_types(self):
        """Gets the statement_types of this LoanDocuments.  # noqa: E501


        :return: The statement_types of this LoanDocuments.  # noqa: E501
        :rtype: list[object]
        """
        return self._statement_types

    @statement_types.setter
    def statement_types(self, statement_types):
        """Sets the statement_types of this LoanDocuments.


        :param statement_types: The statement_types of this LoanDocuments.  # noqa: E501
        :type: list[object]
        """

        self._statement_types = statement_types

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this LoanDocuments.  # noqa: E501


        :return: The custom_attributes of this LoanDocuments.  # noqa: E501
        :rtype: object
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this LoanDocuments.


        :param custom_attributes: The custom_attributes of this LoanDocuments.  # noqa: E501
        :type: object
        """

        self._custom_attributes = custom_attributes

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
        if not isinstance(other, LoanDocuments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoanDocuments):
            return True

        return self.to_dict() != other.to_dict()
