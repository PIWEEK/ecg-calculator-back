from tools.adt.types import ADT_WITH_ID, StrField
from tools.adt.relationships import Relationship1N, RoleSingle, RoleMulti

from .forms import form_entities


class Assessment(ADT_WITH_ID):
    name = StrField()
    version = StrField()
    year = StrField()
    description = StrField()


class AssessmentHasForms(Relationship1N):
    role_1 = RoleSingle(role_class=Assessment, role_name="assessment")
    role_n = RoleMulti(role_class=form_entities.Form, role_name="forms", role_fk="assessment_id", required=True)

