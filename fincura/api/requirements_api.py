# coding: utf-8

"""
    Fincura Integration API

    This [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer) allows you to interact with the Fincura processing and insights engine.   # Authentication  This API uses API keys generated from a Fincura User account. To get access to your User account, speak with you Fincura account manager.  # Accepted Media Types  | File&nbsp;Type&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Extension(s)     | Content-Type(s) | | -------------------------------- |-------------- | ------------ | | PDF File | .pdf | `application/pdf` , `application/x-pdf` | | Excel File | .xls | `application/vnd.ms-excel`  | | Excel File | .xlsx | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`  | | PNG Image | .png | `image/png`  | | GIF Image | .gif | `image/gif`  | | JPG Image | .jpg, .jpeg | `image/jpeg`  | | GIF Image | .gif | `image/gif`  |   # Getting Started  1. [Create a Borrower](#operation/createBorrower)  2. [Add a file](#operation/createDocumentFile) for that Borrower. 3. Analyze in the Fincura App  ****  # noqa: E501

    The version of the OpenAPI document: 1.2.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fincura.api_client import ApiClient
from fincura.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RequirementsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_financial_requirement(self, **kwargs):  # noqa: E501
        """Create a new FinancialRequirement  # noqa: E501

        Create a new FinancialRequirement record  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_financial_requirement(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param FinancialRequirement financial_requirement:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: FinancialRequirement
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_financial_requirement_with_http_info(**kwargs)  # noqa: E501

    def create_financial_requirement_with_http_info(self, **kwargs):  # noqa: E501
        """Create a new FinancialRequirement  # noqa: E501

        Create a new FinancialRequirement record  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_financial_requirement_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param FinancialRequirement financial_requirement:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(FinancialRequirement, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'financial_requirement'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_financial_requirement" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'financial_requirement' in local_var_params:
            body_params = local_var_params['financial_requirement']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_Key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/financial-requirement', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FinancialRequirement',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_financial_requirements(self, **kwargs):  # noqa: E501
        """List FinancialRequirements  # noqa: E501

        List FinancialRequirement records  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_financial_requirements(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param str borrower_uuid: Borrower to filter results for
        :param str search: A search term.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_financial_requirements_with_http_info(**kwargs)  # noqa: E501

    def list_financial_requirements_with_http_info(self, **kwargs):  # noqa: E501
        """List FinancialRequirements  # noqa: E501

        List FinancialRequirement records  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_financial_requirements_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param str borrower_uuid: Borrower to filter results for
        :param str search: A search term.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2004, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'offset',
            'borrower_uuid',
            'search'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_financial_requirements" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'borrower_uuid' in local_var_params and local_var_params['borrower_uuid'] is not None:  # noqa: E501
            query_params.append(('borrower_uuid', local_var_params['borrower_uuid']))  # noqa: E501
        if 'search' in local_var_params and local_var_params['search'] is not None:  # noqa: E501
            query_params.append(('search', local_var_params['search']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_Key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/financial-requirement', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def partial_update_financial_requirement(self, uuid, **kwargs):  # noqa: E501
        """Update a FinancialRequirement  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_financial_requirement(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uuid: (required)
        :param str borrower_uuid: Borrower to filter results for
        :param str search: A search term.
        :param FinancialRequirement financial_requirement:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: FinancialRequirement
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.partial_update_financial_requirement_with_http_info(uuid, **kwargs)  # noqa: E501

    def partial_update_financial_requirement_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Update a FinancialRequirement  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_financial_requirement_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uuid: (required)
        :param str borrower_uuid: Borrower to filter results for
        :param str search: A search term.
        :param FinancialRequirement financial_requirement:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(FinancialRequirement, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'uuid',
            'borrower_uuid',
            'search',
            'financial_requirement'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method partial_update_financial_requirement" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in local_var_params or  # noqa: E501
                                                        local_var_params['uuid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `uuid` when calling `partial_update_financial_requirement`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in local_var_params:
            path_params['uuid'] = local_var_params['uuid']  # noqa: E501

        query_params = []
        if 'borrower_uuid' in local_var_params and local_var_params['borrower_uuid'] is not None:  # noqa: E501
            query_params.append(('borrower_uuid', local_var_params['borrower_uuid']))  # noqa: E501
        if 'search' in local_var_params and local_var_params['search'] is not None:  # noqa: E501
            query_params.append(('search', local_var_params['search']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'financial_requirement' in local_var_params:
            body_params = local_var_params['financial_requirement']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_Key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/financial-requirement/{uuid}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FinancialRequirement',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_financial_requirement(self, uuid, **kwargs):  # noqa: E501
        """Retrieve a FinancialRequirement  # noqa: E501

        Retrieve a FinancialRequirement  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_financial_requirement(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uuid: (required)
        :param str borrower_uuid: Borrower to filter results for
        :param str search: A search term.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: FinancialRequirement
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.retrieve_financial_requirement_with_http_info(uuid, **kwargs)  # noqa: E501

    def retrieve_financial_requirement_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve a FinancialRequirement  # noqa: E501

        Retrieve a FinancialRequirement  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_financial_requirement_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uuid: (required)
        :param str borrower_uuid: Borrower to filter results for
        :param str search: A search term.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(FinancialRequirement, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'uuid',
            'borrower_uuid',
            'search'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_financial_requirement" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in local_var_params or  # noqa: E501
                                                        local_var_params['uuid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `uuid` when calling `retrieve_financial_requirement`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in local_var_params:
            path_params['uuid'] = local_var_params['uuid']  # noqa: E501

        query_params = []
        if 'borrower_uuid' in local_var_params and local_var_params['borrower_uuid'] is not None:  # noqa: E501
            query_params.append(('borrower_uuid', local_var_params['borrower_uuid']))  # noqa: E501
        if 'search' in local_var_params and local_var_params['search'] is not None:  # noqa: E501
            query_params.append(('search', local_var_params['search']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_Key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/financial-requirement/{uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FinancialRequirement',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
