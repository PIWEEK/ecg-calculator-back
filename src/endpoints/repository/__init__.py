from tools.adt_sql.database import SQLADTDatabase
from .organization_repository import OrganizationRepository
from .assessment_repository import (
    AssessmentRepository, StakeholderRepository,
    FormRepository, QuestionRepository,
    SubFormRepository, SubQuestionRepository,
    TopicRepository, AspectRepository
)

import settings

db = SQLADTDatabase(settings.DB_OPTIONS)

organization_repository = OrganizationRepository(db)
assessment_repository = AssessmentRepository(db)
stakeholder_repository = StakeholderRepository(db)
form_repository = FormRepository(db)
question_repository = QuestionRepository(db)
sub_form_repository = SubFormRepository(db)
sub_question_repository = SubQuestionRepository(db)
topic_repository = TopicRepository(db)
aspect_repository = AspectRepository(db)

db.create_all_tables()
