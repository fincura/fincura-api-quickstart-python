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


class DocumentFileCreate(object):
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
        'borrower_uuid': 'str',
        'media_type': 'str',
        'filename': 'str',
        'statements': 'list[DocumentFileCreateStatements]',
        'upload_url': 'str',
        'external_id': 'str',
        'custom_attributes': 'object'
    }

    attribute_map = {
        'uuid': 'uuid',
        'status': 'status',
        'created_date': 'created_date',
        'borrower_uuid': 'borrower_uuid',
        'media_type': 'media_type',
        'filename': 'filename',
        'statements': 'statements',
        'upload_url': 'upload_url',
        'external_id': 'external_id',
        'custom_attributes': 'custom_attributes'
    }

    def __init__(self, uuid=None, status=None, created_date=None, borrower_uuid=None, media_type=None, filename=None, statements=None, upload_url=None, external_id=None, custom_attributes=None, local_vars_configuration=None):  # noqa: E501
        """DocumentFileCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._status = None
        self._created_date = None
        self._borrower_uuid = None
        self._media_type = None
        self._filename = None
        self._statements = None
        self._upload_url = None
        self._external_id = None
        self._custom_attributes = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if status is not None:
            self.status = status
        if created_date is not None:
            self.created_date = created_date
        self.borrower_uuid = borrower_uuid
        self.media_type = media_type
        if filename is not None:
            self.filename = filename
        if statements is not None:
            self.statements = statements
        if upload_url is not None:
            self.upload_url = upload_url
        if external_id is not None:
            self.external_id = external_id
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes

    @property
    def uuid(self):
        """Gets the uuid of this DocumentFileCreate.  # noqa: E501


        :return: The uuid of this DocumentFileCreate.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DocumentFileCreate.


        :param uuid: The uuid of this DocumentFileCreate.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def status(self):
        """Gets the status of this DocumentFileCreate.  # noqa: E501


        :return: The status of this DocumentFileCreate.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DocumentFileCreate.


        :param status: The status of this DocumentFileCreate.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def created_date(self):
        """Gets the created_date of this DocumentFileCreate.  # noqa: E501


        :return: The created_date of this DocumentFileCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this DocumentFileCreate.


        :param created_date: The created_date of this DocumentFileCreate.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def borrower_uuid(self):
        """Gets the borrower_uuid of this DocumentFileCreate.  # noqa: E501

        UUID of the borrower for this file. (see [Borrowers](#tag/Borrowers))  # noqa: E501

        :return: The borrower_uuid of this DocumentFileCreate.  # noqa: E501
        :rtype: str
        """
        return self._borrower_uuid

    @borrower_uuid.setter
    def borrower_uuid(self, borrower_uuid):
        """Sets the borrower_uuid of this DocumentFileCreate.

        UUID of the borrower for this file. (see [Borrowers](#tag/Borrowers))  # noqa: E501

        :param borrower_uuid: The borrower_uuid of this DocumentFileCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and borrower_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `borrower_uuid`, must not be `None`")  # noqa: E501

        self._borrower_uuid = borrower_uuid

    @property
    def media_type(self):
        """Gets the media_type of this DocumentFileCreate.  # noqa: E501

        [MIME type](https://developer.mozilla.org/en-US/docs/Glossary/MIME_type) of the file  # noqa: E501

        :return: The media_type of this DocumentFileCreate.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this DocumentFileCreate.

        [MIME type](https://developer.mozilla.org/en-US/docs/Glossary/MIME_type) of the file  # noqa: E501

        :param media_type: The media_type of this DocumentFileCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and media_type is None:  # noqa: E501
            raise ValueError("Invalid value for `media_type`, must not be `None`")  # noqa: E501
        allowed_values = ["application/pdf", "application/x-pdf", "application/vnd.ms-excel", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "image/png", "image/gif", "image/jpeg"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and media_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `media_type` ({0}), must be one of {1}"  # noqa: E501
                .format(media_type, allowed_values)
            )

        self._media_type = media_type

    @property
    def filename(self):
        """Gets the filename of this DocumentFileCreate.  # noqa: E501

        Used to reference the original filename. Defaults to `document.{MEDIA TYPE FILE EXTENSION}` e.g. fye_2020.pdf  # noqa: E501

        :return: The filename of this DocumentFileCreate.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this DocumentFileCreate.

        Used to reference the original filename. Defaults to `document.{MEDIA TYPE FILE EXTENSION}` e.g. fye_2020.pdf  # noqa: E501

        :param filename: The filename of this DocumentFileCreate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                filename is not None and len(filename) > 200):
            raise ValueError("Invalid value for `filename`, length must be less than or equal to `200`")  # noqa: E501

        self._filename = filename

    @property
    def statements(self):
        """Gets the statements of this DocumentFileCreate.  # noqa: E501


        :return: The statements of this DocumentFileCreate.  # noqa: E501
        :rtype: list[DocumentFileCreateStatements]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """Sets the statements of this DocumentFileCreate.


        :param statements: The statements of this DocumentFileCreate.  # noqa: E501
        :type: list[DocumentFileCreateStatements]
        """

        self._statements = statements

    @property
    def upload_url(self):
        """Gets the upload_url of this DocumentFileCreate.  # noqa: E501


        :return: The upload_url of this DocumentFileCreate.  # noqa: E501
        :rtype: str
        """
        return self._upload_url

    @upload_url.setter
    def upload_url(self, upload_url):
        """Sets the upload_url of this DocumentFileCreate.


        :param upload_url: The upload_url of this DocumentFileCreate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                upload_url is not None and len(upload_url) > 2500):
            raise ValueError("Invalid value for `upload_url`, length must be less than or equal to `2500`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                upload_url is not None and not re.search(r'^(?:[a-z0-9\.\-\+]*):\/\/(?:[^\s:@\/]+(?::[^\s:@\/]*)?@)?(?:(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}|\[[0-9a-f:\.]+\]|([a-z¡-￿0-9](?:[a-z¡-￿0-9-]{0,61}[a-z¡-￿0-9])?(?:\.(?!-)[a-z¡-￿0-9-]{1,63}(?<!-))*\.(?!-)(?:[a-z¡-￿-]{2,63}|xn--[a-z0-9]{1,59})(?<!-)\.?|localhost))(?::\d{2,5})?(?:[\/?#][^\s]*)?\Z', upload_url)):  # noqa: E501
            raise ValueError(r"Invalid value for `upload_url`, must be a follow pattern or equal to `/^(?:[a-z0-9\.\-\+]*):\/\/(?:[^\s:@\/]+(?::[^\s:@\/]*)?@)?(?:(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}|\[[0-9a-f:\.]+\]|([a-z¡-￿0-9](?:[a-z¡-￿0-9-]{0,61}[a-z¡-￿0-9])?(?:\.(?!-)[a-z¡-￿0-9-]{1,63}(?<!-))*\.(?!-)(?:[a-z¡-￿-]{2,63}|xn--[a-z0-9]{1,59})(?<!-)\.?|localhost))(?::\d{2,5})?(?:[\/?#][^\s]*)?\Z/`")  # noqa: E501

        self._upload_url = upload_url

    @property
    def external_id(self):
        """Gets the external_id of this DocumentFileCreate.  # noqa: E501

        External ID is used to uniquely identify a record from your system in our system. Must be unique across records.  # noqa: E501

        :return: The external_id of this DocumentFileCreate.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this DocumentFileCreate.

        External ID is used to uniquely identify a record from your system in our system. Must be unique across records.  # noqa: E501

        :param external_id: The external_id of this DocumentFileCreate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                external_id is not None and len(external_id) > 255):
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `255`")  # noqa: E501

        self._external_id = external_id

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this DocumentFileCreate.  # noqa: E501


        :return: The custom_attributes of this DocumentFileCreate.  # noqa: E501
        :rtype: object
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this DocumentFileCreate.


        :param custom_attributes: The custom_attributes of this DocumentFileCreate.  # noqa: E501
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
        if not isinstance(other, DocumentFileCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentFileCreate):
            return True

        return self.to_dict() != other.to_dict()