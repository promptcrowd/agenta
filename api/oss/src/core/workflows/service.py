from typing import Optional, List
from uuid import UUID

from oss.src.utils.logging import get_module_logger

from oss.src.core.git.interfaces import GitDAOInterface
from oss.src.core.shared.dtos import Reference, Windowing
from oss.src.core.git.dtos import (
    ArtifactCreate,
    ArtifactEdit,
    ArtifactQuery,
    ArtifactFork,
    ArtifactLog,
    #
    VariantCreate,
    VariantEdit,
    VariantQuery,
    #
    RevisionCreate,
    RevisionEdit,
    RevisionQuery,
    RevisionCommit,
)
from oss.src.core.workflows.dtos import (
    Workflow,
    WorkflowCreate,
    WorkflowEdit,
    WorkflowQuery,
    WorkflowFork,
    WorkflowLog,
    #
    WorkflowVariant,
    WorkflowVariantCreate,
    WorkflowVariantEdit,
    WorkflowVariantQuery,
    #
    WorkflowRevision,
    WorkflowRevisionCreate,
    WorkflowRevisionEdit,
    WorkflowRevisionQuery,
    WorkflowRevisionCommit,
)


log = get_module_logger(__name__)


class WorkflowsService:
    def __init__(
        self,
        *,
        workflows_dao: GitDAOInterface,
    ):
        self.workflows_dao = workflows_dao

    ## -- artifacts ------------------------------------------------------------

    async def create_workflow(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_create: WorkflowCreate,
    ) -> Optional[Workflow]:
        _artifact_create = ArtifactCreate(
            **workflow_create.model_dump(mode="json"),
        )

        artifact = await self.workflows_dao.create_artifact(
            project_id=project_id,
            user_id=user_id,
            #
            artifact_create=_artifact_create,
        )

        if not artifact:
            return None

        _workflow = Workflow(**artifact.model_dump(mode="json"))

        return _workflow

    async def fetch_workflow(
        self,
        *,
        project_id: UUID,
        #
        workflow_ref: Reference,
    ) -> Optional[Workflow]:
        artifact = await self.workflows_dao.fetch_artifact(
            project_id=project_id,
            #
            artifact_ref=workflow_ref,
        )

        if not artifact:
            return None

        _workflow = Workflow(**artifact.model_dump(mode="json"))

        return _workflow

    async def edit_workflow(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_edit: WorkflowEdit,
    ) -> Optional[Workflow]:
        _artifact_edit = ArtifactEdit(
            **workflow_edit.model_dump(mode="json"),
        )

        artifact = await self.workflows_dao.edit_artifact(
            project_id=project_id,
            user_id=user_id,
            #
            artifact_edit=_artifact_edit,
        )

        if not artifact:
            return None

        _workflow = Workflow(**artifact.model_dump(mode="json"))

        return _workflow

    async def archive_workflow(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_id: UUID,
    ) -> Optional[Workflow]:
        artifact = await self.workflows_dao.archive_artifact(
            project_id=project_id,
            user_id=user_id,
            #
            artifact_id=workflow_id,
        )

        if not artifact:
            return None

        _workflow = Workflow(**artifact.model_dump(mode="json"))

        return _workflow

    async def unarchive_workflow(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_id: UUID,
    ) -> Optional[Workflow]:
        artifact = await self.workflows_dao.unarchive_artifact(
            project_id=project_id,
            user_id=user_id,
            #
            artifact_id=workflow_id,
        )

        if not artifact:
            return None

        _workflow = Workflow(**artifact.model_dump(mode="json"))

        return _workflow

    async def query_workflows(
        self,
        *,
        project_id: UUID,
        #
        workflow_query: Optional[WorkflowQuery] = None,
        #
        workflow_refs: Optional[List[Reference]] = None,
        #
        include_archived: Optional[bool] = None,
        #
        windowing: Optional[Windowing] = None,
    ) -> List[Workflow]:
        _artifact_query = (
            ArtifactQuery(
                **workflow_query.model_dump(mode="json", exclude_none=True),
            )
            if workflow_query
            else ArtifactQuery()
        )

        artifacts = await self.workflows_dao.query_artifacts(
            project_id=project_id,
            #
            artifact_query=_artifact_query,
            #
            artifact_refs=workflow_refs,
            #
            include_archived=include_archived,
            #
            windowing=windowing,
        )

        _workflows = [
            Workflow(
                **artifact.model_dump(mode="json"),
            )
            for artifact in artifacts
        ]

        return _workflows

    ## -------------------------------------------------------------------------

    ## -- variants -------------------------------------------------------------

    async def create_workflow_variant(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_variant_create: WorkflowVariantCreate,
    ) -> Optional[WorkflowVariant]:
        _variant_create = VariantCreate(
            **workflow_variant_create.model_dump(mode="json"),
        )

        variant = await self.workflows_dao.create_variant(
            project_id=project_id,
            user_id=user_id,
            #
            variant_create=_variant_create,
        )

        if not variant:
            return None

        _workflow_variant = WorkflowVariant(
            **variant.model_dump(mode="json"),
        )

        return _workflow_variant

    async def fetch_workflow_variant(
        self,
        *,
        project_id: UUID,
        #
        workflow_ref: Optional[Reference] = None,
        workflow_variant_ref: Optional[Reference] = None,
    ) -> Optional[WorkflowVariant]:
        variant = await self.workflows_dao.fetch_variant(
            project_id=project_id,
            #
            artifact_ref=workflow_ref,
            variant_ref=workflow_variant_ref,
        )

        if not variant:
            return None

        _workflow_variant = WorkflowVariant(
            **variant.model_dump(mode="json"),
        )

        return _workflow_variant

    async def edit_workflow_variant(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_variant_edit: WorkflowVariantEdit,
    ) -> Optional[WorkflowVariant]:
        _variant_edit = VariantEdit(
            **workflow_variant_edit.model_dump(mode="json"),
        )

        variant = await self.workflows_dao.edit_variant(
            project_id=project_id,
            user_id=user_id,
            #
            variant_edit=_variant_edit,
        )

        if not variant:
            return None

        _workflow_variant = WorkflowVariant(
            **variant.model_dump(mode="json"),
        )

        return _workflow_variant

    async def archive_workflow_variant(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_variant_id: UUID,
    ) -> Optional[WorkflowVariant]:
        variant = await self.workflows_dao.archive_variant(
            project_id=project_id,
            user_id=user_id,
            #
            variant_id=workflow_variant_id,
        )

        if not variant:
            return None

        _workflow_variant = WorkflowVariant(
            **variant.model_dump(mode="json"),
        )

        return _workflow_variant

    async def unarchive_workflow_variant(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_variant_id: UUID,
    ) -> Optional[WorkflowVariant]:
        variant = await self.workflows_dao.unarchive_variant(
            project_id=project_id,
            user_id=user_id,
            #
            variant_id=workflow_variant_id,
        )

        if not variant:
            return None

        _workdlow_variant = WorkflowVariant(
            **variant.model_dump(mode="json"),
        )

        return _workdlow_variant

    async def query_workflow_variants(
        self,
        *,
        project_id: UUID,
        #
        workflow_variant_query: Optional[WorkflowVariantQuery] = None,
        #
        workflow_refs: Optional[List[Reference]] = None,
        workflow_variant_refs: Optional[List[Reference]] = None,
        #
        include_archived: Optional[bool] = None,
        #
        windowing: Optional[Windowing] = None,
    ) -> List[WorkflowVariant]:
        _variant_query = (
            VariantQuery(
                **workflow_variant_query.model_dump(mode="json", exclude_none=True),
            )
            if workflow_variant_query
            else VariantQuery()
        )

        variants = await self.workflows_dao.query_variants(
            project_id=project_id,
            #
            variant_query=_variant_query,
            #
            artifact_refs=workflow_refs,
            variant_refs=workflow_variant_refs,
            #
            include_archived=include_archived,
            #
            windowing=windowing,
        )

        _workflow_variants = [
            WorkflowVariant(
                **variant.model_dump(mode="json"),
            )
            for variant in variants
        ]

        return _workflow_variants

    ## .........................................................................

    async def fork_workflow_variant(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_fork: WorkflowFork,
    ) -> Optional[WorkflowVariant]:
        _artifact_fork = ArtifactFork(
            **workflow_fork.model_dump(mode="json"),
        )

        variant = await self.workflows_dao.fork_variant(
            project_id=project_id,
            user_id=user_id,
            #
            artifact_fork=_artifact_fork,
        )

        if not variant:
            return None

        _workflow_variant = WorkflowVariant(
            **variant.model_dump(mode="json"),
        )

        return _workflow_variant

    ## -------------------------------------------------------------------------

    ## -- revisions ------------------------------------------------------------

    async def create_workflow_revision(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_revision_create: WorkflowRevisionCreate,
    ) -> Optional[WorkflowRevision]:
        _revision_create = RevisionCreate(
            **workflow_revision_create.model_dump(mode="json"),
        )

        revision = await self.workflows_dao.create_revision(
            project_id=project_id,
            user_id=user_id,
            #
            revision_create=_revision_create,
        )

        if not revision:
            return None

        _workflow_revision = WorkflowRevision(
            **revision.model_dump(mode="json"),
        )

        return _workflow_revision

    async def fetch_workflow_revision(
        self,
        *,
        project_id: UUID,
        #
        workflow_variant_ref: Optional[Reference] = None,
        workflow_revision_ref: Optional[Reference] = None,
    ) -> Optional[WorkflowRevision]:
        revision = await self.workflows_dao.fetch_revision(
            project_id=project_id,
            #
            variant_ref=workflow_variant_ref,
            revision_ref=workflow_revision_ref,
        )

        if not revision:
            return None

        _workflow_revision = WorkflowRevision(
            **revision.model_dump(mode="json"),
        )

        return _workflow_revision

    async def edit_workflow_revision(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_revision_edit: WorkflowRevisionEdit,
    ) -> Optional[WorkflowRevision]:
        _workflow_revision_edit = RevisionEdit(
            **workflow_revision_edit.model_dump(mode="json"),
        )

        revision = await self.workflows_dao.edit_revision(
            project_id=project_id,
            user_id=user_id,
            #
            revision_edit=_workflow_revision_edit,
        )

        if not revision:
            return None

        _workflow_revision = WorkflowRevision(
            **revision.model_dump(mode="json"),
        )

        return _workflow_revision

    async def archive_workflow_revision(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_revision_id: UUID,
    ) -> Optional[WorkflowRevision]:
        revision = await self.workflows_dao.archive_revision(
            project_id=project_id,
            user_id=user_id,
            #
            revision_id=workflow_revision_id,
        )

        if not revision:
            return None

        _workflow_revision = WorkflowRevision(
            **revision.model_dump(mode="json"),
        )

        return _workflow_revision

    async def unarchive_workflow_revision(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_revision_id: UUID,
    ) -> Optional[WorkflowRevision]:
        revision = await self.workflows_dao.unarchive_revision(
            project_id=project_id,
            user_id=user_id,
            #
            revision_id=workflow_revision_id,
        )

        if not revision:
            return None

        _workflow_revision = WorkflowRevision(
            **revision.model_dump(mode="json"),
        )

        return _workflow_revision

    async def query_workflow_revisions(
        self,
        *,
        project_id: UUID,
        #
        workflow_revision_query: Optional[WorkflowRevisionQuery] = None,
        #
        workflow_refs: Optional[List[Reference]] = None,
        workflow_variant_refs: Optional[List[Reference]] = None,
        workflow_revision_refs: Optional[List[Reference]] = None,
        #
        include_archived: Optional[bool] = None,
        #
        windowing: Optional[Windowing] = None,
    ) -> List[WorkflowRevision]:
        _revision_query = (
            RevisionQuery(
                **workflow_revision_query.model_dump(mode="json", exclude_none=True),
            )
            if workflow_revision_query
            else RevisionQuery()
        )

        revisions = await self.workflows_dao.query_revisions(
            project_id=project_id,
            #
            revision_query=_revision_query,
            #
            artifact_refs=workflow_refs,
            variant_refs=workflow_variant_refs,
            revision_refs=workflow_revision_refs,
            #
            include_archived=include_archived,
            #
            windowing=windowing,
        )

        _workflow_revisions = [
            WorkflowRevision(
                **revision.model_dump(mode="json"),
            )
            for revision in revisions
        ]

        return _workflow_revisions

    ## .........................................................................

    async def commit_workflow_revision(
        self,
        *,
        project_id: UUID,
        user_id: UUID,
        #
        workflow_revision_commit: WorkflowRevisionCommit,
    ) -> Optional[WorkflowRevision]:
        _revision_commit = RevisionCommit(
            **workflow_revision_commit.model_dump(mode="json"),
        )

        if not _revision_commit.artifact_id:
            if not _revision_commit.variant_id:
                return None

            variant = await self.workflows_dao.fetch_variant(
                project_id=project_id,
                #
                variant_ref=Reference(id=_revision_commit.variant_id),
            )

            if not variant:
                return None

            _revision_commit.artifact_id = variant.artifact_id

        revision = await self.workflows_dao.commit_revision(
            project_id=project_id,
            user_id=user_id,
            #
            revision_commit=_revision_commit,
        )

        if not revision:
            return None

        _workflow_revision = WorkflowRevision(
            **revision.model_dump(mode="json"),
        )

        return _workflow_revision

    async def log_workflow_revisions(
        self,
        *,
        project_id: UUID,
        #
        workflow_log: WorkflowLog,
    ) -> List[WorkflowRevision]:
        _artifact_log = ArtifactLog(
            **workflow_log.model_dump(mode="json"),
        )

        revisions = await self.workflows_dao.log_revisions(
            project_id=project_id,
            #
            artifact_log=_artifact_log,
        )

        _workflow_revisions = [
            WorkflowRevision(
                **revision.model_dump(mode="json"),
            )
            for revision in revisions
        ]

        return _workflow_revisions

    ## -------------------------------------------------------------------------
