# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PrefixOperations:
    """PrefixOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.peering.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get(
        self,
        resource_group_name: str,
        peering_service_name: str,
        prefix_name: str,
        expand: Optional[str] = None,
        **kwargs
    ) -> "models.PeeringServicePrefix":
        """Gets an existing prefix with the specified name under the given subscription, resource group and peering service.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param peering_service_name: The name of the peering service.
        :type peering_service_name: str
        :param prefix_name: The name of the prefix.
        :type prefix_name: str
        :param expand: The properties to be expanded.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PeeringServicePrefix or the result of cls(response)
        :rtype: ~azure.mgmt.peering.models.PeeringServicePrefix
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PeeringServicePrefix"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-04-01"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'peeringServiceName': self._serialize.url("peering_service_name", peering_service_name, 'str'),
            'prefixName': self._serialize.url("prefix_name", prefix_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PeeringServicePrefix', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName}'}  # type: ignore

    async def create_or_update(
        self,
        resource_group_name: str,
        peering_service_name: str,
        prefix_name: str,
        prefix: Optional[str] = None,
        peering_service_prefix_key: Optional[str] = None,
        **kwargs
    ) -> "models.PeeringServicePrefix":
        """Creates a new prefix with the specified name under the given subscription, resource group and peering service.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param peering_service_name: The name of the peering service.
        :type peering_service_name: str
        :param prefix_name: The name of the prefix.
        :type prefix_name: str
        :param prefix: The prefix from which your traffic originates.
        :type prefix: str
        :param peering_service_prefix_key: The peering service prefix key.
        :type peering_service_prefix_key: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PeeringServicePrefix or the result of cls(response)
        :rtype: ~azure.mgmt.peering.models.PeeringServicePrefix
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PeeringServicePrefix"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _peering_service_prefix = models.PeeringServicePrefix(prefix=prefix, peering_service_prefix_key=peering_service_prefix_key)
        api_version = "2020-04-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'peeringServiceName': self._serialize.url("peering_service_name", peering_service_name, 'str'),
            'prefixName': self._serialize.url("prefix_name", prefix_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_peering_service_prefix, 'PeeringServicePrefix')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PeeringServicePrefix', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('PeeringServicePrefix', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName}'}  # type: ignore

    async def delete(
        self,
        resource_group_name: str,
        peering_service_name: str,
        prefix_name: str,
        **kwargs
    ) -> None:
        """Deletes an existing prefix with the specified name under the given subscription, resource group and peering service.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param peering_service_name: The name of the peering service.
        :type peering_service_name: str
        :param prefix_name: The name of the prefix.
        :type prefix_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-04-01"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'peeringServiceName': self._serialize.url("peering_service_name", peering_service_name, 'str'),
            'prefixName': self._serialize.url("prefix_name", prefix_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName}'}  # type: ignore

    def list_by_peering_service(
        self,
        resource_group_name: str,
        peering_service_name: str,
        expand: Optional[str] = None,
        **kwargs
    ) -> AsyncIterable["models.PeeringServicePrefixListResult"]:
        """Lists all prefixes under the given subscription, resource group and peering service.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param peering_service_name: The name of the peering service.
        :type peering_service_name: str
        :param expand: The properties to be expanded.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of PeeringServicePrefixListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.peering.models.PeeringServicePrefixListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PeeringServicePrefixListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-04-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_peering_service.metadata['url']  # type: ignore
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'peeringServiceName': self._serialize.url("peering_service_name", peering_service_name, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PeeringServicePrefixListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_peering_service.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes'}  # type: ignore
