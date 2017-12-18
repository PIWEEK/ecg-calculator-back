from sqlalchemy.sql import select

from core.assessments import assessment_entities
from core.assessments.forms import form_entities

from tools.adt_sql.repository import SQLADTRepository


class AssessmentRepository(SQLADTRepository):
    adt = assessment_entities.Assessment
    table_name = "assessments"


class FormRepository(SQLADTRepository):
    adt = form_entities.Form
    table_name = "forms"

    def list_for_assessment(self, context, assessment_id, order_by = None):
        return self.db.retrieve_adts(
            context,
            self.adt,
            select([getattr(self.db, self.table_name)])
                .where(self.db.forms.c.assessment_id == assessment_id)
                .order_by(order_by)
        )

    def retrieve_by_id_full(self, context, form_id):
        return self.db.retrieve_single_joined_adt(
            context,
            form_entities.Form,
            {
                "forms": form_entities.Form,
                "questions": form_entities.Question,
                "sub_forms": form_entities.SubForm,
                "sub_questions": form_entities.SubQuestion,
            },
            select(
                [self.db.forms, self.db.questions, self.db.sub_forms, self.db.sub_questions],
                use_labels=True
            ).select_from(
                self.db.forms.join(
                    self.db.questions,
                    self.db.forms.c.id == self.db.questions.c.form_id
                ).join(
                    self.db.sub_forms,
                    self.db.forms.c.id == self.db.sub_forms.c.form_id
                ).join(
                    self.db.sub_questions,
                    self.db.sub_forms.c.id == self.db.sub_questions.c.sub_form_id
                )
            ).where(
                self.db.forms.c.id == form_id
            ).order_by(self.db.questions.c.order)
        )


class QuestionRepository(SQLADTRepository):
    adt = form_entities.Question
    table_name = "questions"


class SubFormRepository(SQLADTRepository):
    adt = form_entities.SubForm
    table_name = "sub_forms"


class SubQuestionRepository(SQLADTRepository):
    adt = form_entities.SubQuestion
    table_name = "sub_questions"

