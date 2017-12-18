from tools.adt.types import ADT_WITH_ID, StrField, IntField, DictField
from tools.adt.relationships import Relationship1N, RoleSingle, RoleMulti


class Form(ADT_WITH_ID):
    assessment_id = IntField()
    code = StrField()
    name = StrField()
    description = StrField()


class Question(ADT_WITH_ID):
    form_id = IntField()
    order = IntField()
    title = StrField()
    quick_description = StrField()
    full_description = StrField()
    examples = StrField()
    data_type = StrField()
    options = DictField(null = True)


class FormHasQuestions(Relationship1N):
    role_1 = RoleSingle(role_class=Form, role_name="form")
    role_n = RoleMulti(role_class=Question, role_name="questions", role_fk="form_id", required=True)


class SubForm(ADT_WITH_ID):
    form_id = IntField()
    order = IntField()
    caption = StrField()
    description = StrField()


class SubQuestion(ADT_WITH_ID):
    sub_form_id = IntField()
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

