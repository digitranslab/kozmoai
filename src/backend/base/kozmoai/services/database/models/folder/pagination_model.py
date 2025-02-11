from fastapi_pagination import Page

from kozmoai.helpers.base_model import BaseModel
from kozmoai.services.database.models.flow.model import Flow
from kozmoai.services.database.models.folder.model import FolderRead


class FolderWithPaginatedFlows(BaseModel):
    folder: FolderRead
    flows: Page[Flow]
