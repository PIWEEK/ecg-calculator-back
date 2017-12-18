import os.path

from anillo.handlers.routing import router as anillo_router, optionized_url as url
from anillo.http import responses

from endpoints.web.api.assessments import assessment_handlers, form_handlers
from endpoints.web.api.organizations import organization_handlers

PREFIX = "/api/v1"

urls = [
    # User
    # url(PREFIX + "/login", user_handlers.Login(), methods=["post"]),
    # url(PREFIX + "/logout", user_handlers.Logout(), methods=["post"]),
    # url(PREFIX + "/users", user_handlers.UsersList(), methods=["get"]),
    # url(PREFIX + "/users/<string:username>", user_handlers.UserDetail(), methods=["get", "patch", "delete"]),

    # Assessments
    url(PREFIX + "/assessments",
        assessment_handlers.AssessmentsList(), methods=["get"]),
    url(PREFIX + "/assessments/<string:assessment_id>",
        assessment_handlers.AssessmentDetail(), methods=["get"]),
    url(PREFIX + "/assessments/<string:assessment_id>/forms",
        form_handlers.AssessmentFormsList(), methods=["get"]),
    url(PREFIX + "/assessments/<string:assessment_id>/forms/<string:form_id>",
        form_handlers.AssessmentFormDetail(), methods=["get"]),

    # Organizations
    url(PREFIX + "/organizations",
        organization_handlers.OrganizationsList(), methods=["get", "post"]),
    url(PREFIX + "/organizations/<string:organization_id>",
        organization_handlers.OrganizationDetail(), methods=["get", "patch", "delete"]),
]

router = anillo_router(urls)
