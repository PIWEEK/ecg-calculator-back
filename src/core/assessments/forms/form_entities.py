from tools.adt.types import ADT_WITH_ID, StrField, IntField, DictField
from tools.adt.relationships import Relationship1N, RoleSingle, RoleMulti

from ..stakeholders import stakeholder_entities


class Form(ADT_WITH_ID):
    assessment_id = IntField()
    stakeholder_id = IntField(null = True)
    slug = StrField()
    name = StrField()
    description = StrField()


class Question(ADT_WITH_ID):
    form_id = IntField()
    order = IntField()
    slug = StrField()
    title = StrField()
    quick_description = StrField()
    full_description = StrField()
    examples = StrField()
    data_type = StrField()
    options = DictField(null = True)


class FormHasStakeholder(Relationship1N):
    role_1 = RoleSingle(role_class=stakeholder_entities.Stakeholder, role_name="stakeholder")
    role_n = RoleMulti(role_class=Form, role_name="forms", role_fk="stakeholder_id", required=False)


class FormHasQuestions(Relationship1N):
    role_1 = RoleSingle(role_class=Form, role_name="form")
    role_n = RoleMulti(role_class=Question, role_name="questions", role_fk="form_id", required=True)


class SubForm(ADT_WITH_ID):
    form_id = IntField()
    order = IntField()
    slug = StrField()
    caption = StrField()
    description = StrField()


class SubQuestion(ADT_WITH_ID):
    sub_form_id = IntField()
    order = IntField()
    columns = IntField()
    slug = StrField()
    title = StrField()
    description = StrField()
    data_type = StrField()
    options = DictField(null = True)


class FormHasSubForms(Relationship1N):
    role_1 = RoleSingle(role_class=Form, role_name="form")
    role_n = RoleMulti(role_class=SubForm, role_name="sub_forms", role_fk="form_id", required=True)


class SubFormHasQuestions(Relationship1N):
    role_1 = RoleSingle(role_class=SubForm, role_name="sub_form")
    role_n = RoleMulti(role_class=SubQuestion, role_name="sub_questions", role_fk="sub_form_id", required=True)

