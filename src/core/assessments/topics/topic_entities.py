from tools.adt.types import ADT_WITH_ID, StrField, IntField, BoolField
from tools.adt.relationships import Relationship1N, RoleSingle, RoleMulti

from ..stakeholders import stakeholder_entities


class Topic(ADT_WITH_ID):
    assessment_id = IntField()
    stakeholder_id = IntField()
    slug = StrField()
    code = StrField()
    name = StrField()
    description = StrField()


class Aspect(ADT_WITH_ID):
    topic_id = IntField()
    order = IntField()
    slug = StrField()
    code = StrField()
    title = StrField()
    quick_description = StrField()
    valorative_questions = StrField()
    mandatory_indicators = StrField()
    evaluation_levels = StrField()
    explanatory_notes = StrField()
    is_negative = BoolField()


class TopicHasStakeholder(Relationship1N):
    role_1 = RoleSingle(role_class=stakeholder_entities.Stakeholder, role_name="stakeholder")
    role_n = RoleMulti(role_class=Topic, role_name="topics", role_fk="stakeholder_id", required=True)


class TopicHasAspects(Relationship1N):
    role_1 = RoleSingle(role_class=Topic, role_name="topic")
    role_n = RoleMulti(role_class=Aspect, role_name="aspects", role_fk="topic_id", required=True)

