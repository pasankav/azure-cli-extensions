# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ReceivedRouteOperations(object):
    """ReceivedRouteOperations operations.

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

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_peering(
        self,
        resource_group_name,  # type: str
        peering_name,  # type: str
        prefix=None,  # type: Optional[str]
        as_path=None,  # type: Optional[str]
        origin_as_validation_state=None,  # type: Optional[str]
        rpki_validation_state=None,  # type: Optional[str]
        skip_token=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.PeeringReceivedRouteListResult"]
        """Lists the prefixes received over the specified peering under the given subscription and resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param peering_name: The name of the peering.
        :type peering_name: str
        :param prefix: The optional prefix that can be used to filter the routes.
        :type prefix: str
        :param as_path: The optional AS path that can be used to filter the routes.
        :type as_path: str
        :param origin_as_validation_state: The optional origin AS validation state that can be used to
     filter the routes.
        :type origin_as_validation_state: str
        :param rpki_validation_state: The optional RPKI validation state that can be used to filter the
     routes.
        :type rpki_validation_state: str
        :param skip_token: The optional page continuation token that is used in the event of paginated
     result.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of PeeringReceivedRouteListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.peering.models.PeeringReceivedRouteListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PeeringReceivedRouteListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-04-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_peering.metadata['url']  # type: ignore
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'peeringName': self._serialize.url("peering_name", peering_name, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if prefix is not None:
                    query_parameters['prefix'] = self._serialize.query("prefix", prefix, 'str')
                if as_path is not None:
                    query_parameters['asPath'] = self._serialize.query("as_path", as_path, 'str')
                if origin_as_validation_state is not None:
                    query_parameters['originAsValidationState'] = self._serialize.query("origin_as_validation_state", origin_as_validation_state, 'str')
                if rpki_validation_state is not None:
                    query_parameters['rpkiValidationState'] = self._serialize.query("rpki_validation_state", rpki_validation_state, 'str')
                if skip_token is not None:
                    query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('PeeringReceivedRouteListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_peering.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/receivedRoutes'}  # type: ignore
