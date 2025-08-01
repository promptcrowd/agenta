# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.invite_request import InviteRequest
from ..types.organization import Organization
from ..types.organization_details import OrganizationDetails

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawOrganizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_organization_details(
        self, org_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OrganizationDetails]:
        """
        Return the details of the organization.

        Parameters
        ----------
        org_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OrganizationDetails]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{jsonable_encoder(org_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OrganizationDetails,
                    parse_obj_as(
                        type_=OrganizationDetails,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(
                status_code=_response.status_code,
                headers=dict(_response.headers),
                body=_response.text,
            )
        raise ApiError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response_json,
        )

    def list_organizations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Organization]]:
        """
        Returns a list of organizations associated with the user's session.

        Returns:
            list[Organization]: A list of organizations associated with the user's session.

        Raises:
            HTTPException: If there is an error retrieving the organizations from the database.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Organization]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "organizations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Organization],
                    parse_obj_as(
                        type_=typing.List[Organization],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(
                status_code=_response.status_code,
                headers=dict(_response.headers),
                body=_response.text,
            )
        raise ApiError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response_json,
        )

    def invite_user_to_workspace(
        self,
        org_id: str,
        workspace_id: str,
        *,
        request: typing.Sequence[InviteRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Assigns a role to a user in an organization.

        Args:
            org_id (str): The ID of the organization.
            payload (InviteRequest): The payload containing the organization id, user email, and role to assign.
            workspace_id (str): The ID of the workspace.

        Returns:
            bool: True if the role was successfully assigned, False otherwise.

        Raises:
            HTTPException: If the user does not have permission to perform this action.
            HTTPException: If there is an error assigning the role to the user.

        Parameters
        ----------
        org_id : str

        workspace_id : str

        request : typing.Sequence[InviteRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{jsonable_encoder(org_id)}/workspaces/{jsonable_encoder(workspace_id)}/invite",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[InviteRequest],
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(
                status_code=_response.status_code,
                headers=dict(_response.headers),
                body=_response.text,
            )
        raise ApiError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response_json,
        )

    def resend_invitation(
        self,
        org_id: str,
        workspace_id: str,
        *,
        email: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Resend an invitation to a user to an Organization.

        Raises:
            HTTPException: _description_; status_code: 500
            HTTPException: Invitation not found or has expired; status_code: 400
            HTTPException: You already belong to this organization; status_code: 400

        Returns:
            JSONResponse: Resent invitation to user; status_code: 200

        Parameters
        ----------
        org_id : str

        workspace_id : str

        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{jsonable_encoder(org_id)}/workspaces/{jsonable_encoder(workspace_id)}/invite/resend",
            method="POST",
            json={
                "email": email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(
                status_code=_response.status_code,
                headers=dict(_response.headers),
                body=_response.text,
            )
        raise ApiError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response_json,
        )

    def accept_invitation(
        self,
        org_id: str,
        workspace_id: str,
        *,
        project_id: str,
        token: str,
        email: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Accept an invitation to an organization.

        Raises:
            HTTPException: _description_; status_code: 500
            HTTPException: Invitation not found or has expired; status_code: 400
            HTTPException: You already belong to this organization; status_code: 400

        Returns:
            JSONResponse: Accepted invitation to workspace; status_code: 200

        Parameters
        ----------
        org_id : str

        workspace_id : str

        project_id : str

        token : str

        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{jsonable_encoder(org_id)}/workspaces/{jsonable_encoder(workspace_id)}/invite/accept",
            method="POST",
            params={
                "project_id": project_id,
            },
            json={
                "token": token,
                "email": email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(
                status_code=_response.status_code,
                headers=dict(_response.headers),
                body=_response.text,
            )
        raise ApiError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response_json,
        )


class AsyncRawOrganizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fetch_organization_details(
        self, org_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OrganizationDetails]:
        """
        Return the details of the organization.

        Parameters
        ----------
        org_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OrganizationDetails]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{jsonable_encoder(org_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OrganizationDetails,
                    parse_obj_as(
                        type_=OrganizationDetails,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(
                status_code=_response.status_code,
                headers=dict(_response.headers),
                body=_response.text,
            )
        raise ApiError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response_json,
        )

    async def list_organizations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Organization]]:
        """
        Returns a list of organizations associated with the user's session.

        Returns:
            list[Organization]: A list of organizations associated with the user's session.

        Raises:
            HTTPException: If there is an error retrieving the organizations from the database.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Organization]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "organizations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Organization],
                    parse_obj_as(
                        type_=typing.List[Organization],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(
                status_code=_response.status_code,
                headers=dict(_response.headers),
                body=_response.text,
            )
        raise ApiError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response_json,
        )

    async def invite_user_to_workspace(
        self,
        org_id: str,
        workspace_id: str,
        *,
        request: typing.Sequence[InviteRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Assigns a role to a user in an organization.

        Args:
            org_id (str): The ID of the organization.
            payload (InviteRequest): The payload containing the organization id, user email, and role to assign.
            workspace_id (str): The ID of the workspace.

        Returns:
            bool: True if the role was successfully assigned, False otherwise.

        Raises:
            HTTPException: If the user does not have permission to perform this action.
            HTTPException: If there is an error assigning the role to the user.

        Parameters
        ----------
        org_id : str

        workspace_id : str

        request : typing.Sequence[InviteRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{jsonable_encoder(org_id)}/workspaces/{jsonable_encoder(workspace_id)}/invite",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[InviteRequest],
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(
                status_code=_response.status_code,
                headers=dict(_response.headers),
                body=_response.text,
            )
        raise ApiError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response_json,
        )

    async def resend_invitation(
        self,
        org_id: str,
        workspace_id: str,
        *,
        email: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Resend an invitation to a user to an Organization.

        Raises:
            HTTPException: _description_; status_code: 500
            HTTPException: Invitation not found or has expired; status_code: 400
            HTTPException: You already belong to this organization; status_code: 400

        Returns:
            JSONResponse: Resent invitation to user; status_code: 200

        Parameters
        ----------
        org_id : str

        workspace_id : str

        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{jsonable_encoder(org_id)}/workspaces/{jsonable_encoder(workspace_id)}/invite/resend",
            method="POST",
            json={
                "email": email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(
                status_code=_response.status_code,
                headers=dict(_response.headers),
                body=_response.text,
            )
        raise ApiError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response_json,
        )

    async def accept_invitation(
        self,
        org_id: str,
        workspace_id: str,
        *,
        project_id: str,
        token: str,
        email: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Accept an invitation to an organization.

        Raises:
            HTTPException: _description_; status_code: 500
            HTTPException: Invitation not found or has expired; status_code: 400
            HTTPException: You already belong to this organization; status_code: 400

        Returns:
            JSONResponse: Accepted invitation to workspace; status_code: 200

        Parameters
        ----------
        org_id : str

        workspace_id : str

        project_id : str

        token : str

        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{jsonable_encoder(org_id)}/workspaces/{jsonable_encoder(workspace_id)}/invite/accept",
            method="POST",
            params={
                "project_id": project_id,
            },
            json={
                "token": token,
                "email": email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(
                status_code=_response.status_code,
                headers=dict(_response.headers),
                body=_response.text,
            )
        raise ApiError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response_json,
        )
