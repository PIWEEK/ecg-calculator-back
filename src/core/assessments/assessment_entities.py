from tools.adt.types import ADT_WITH_ID, StrField
from tools.adt.relationships import Relationship1N, RoleSingle, RoleMulti

from .stakeholders import stakeholder_entities
from .forms import form_entities
from .topics import topic_entities


class Assessment(ADT_WITH_ID):
    name = StrField()
    slug = StrField()
    version = StrField()
    year = StrField()
    description = StrField()


class AssessmentHasStakeholders(Relationship1N):
    role_1 = RoleSingle(role_class=Assessment, role_name="assessment")
    role_n = RoleMulti(role_class=stakeholder_entities.Stakeholder, role_name="stakeholders", role_fk="assessment_id", required=True)


class AssessmentHasForms(Relationship1N):
    role_1 = RoleSingle(role_class=Assessment, role_name="assessment")
    role_n = RoleMulti(role_class=form_entities.Form, role_name="forms", role_fk="assessment_id", required=True)


class AssessmentHasTopics(Relationship1N):
    role_1 = RoleSingle(role_class=Assessment, role_name="assessment")
    role_n = RoleMulti(role_class=topic_entities.Topic, role_name="topics", role_fk="assessment_id", required=True)

