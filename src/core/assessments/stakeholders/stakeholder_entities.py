from tools.adt.types import ADT_WITH_ID, StrField, IntField
from tools.adt.relationships import Relationship1N, RoleSingle, RoleMulti


class Stakeholder(ADT_WITH_ID):
    assessment_id = IntField()
    name = StrField()
    slug = StrField()
    code = StrField()
    description = StrField()

