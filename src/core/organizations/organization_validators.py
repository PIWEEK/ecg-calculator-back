# -*- coding: utf-8 -*-

from skame.schemas import types as t, strings as s, numeric as n, base as b
from skame.exceptions import SchemaError
from tools import validator as v


class OrganizationForCreateValidator(v.Validator):
    schema = b.schema({
        "name": b.And(
            t.String(),
            s.NotEmpty(),
        )
    })


class OrganizationForUpdateValidator(v.Validator):
    schema = b.schema({
        b.Optional("address"): b.And(
            t.String(),
            s.NotEmpty(),
        ),
        b.Optional("state"): b.And(
            t.String(),
            s.NotEmpty(),
        ),
        b.Optional("country"): b.And(
            t.String(),
            s.NotEmpty(),
        ),
        b.Optional("sector"): b.And(
            t.String(),
            s.NotEmpty(),
        ),
        b.Optional("web"): b.And(
            t.String(),
            s.NotEmpty(),
            s.URL(),
        ),
        b.Optional("description"): b.And(
            t.String(),
            s.NotEmpty(),
        ),
    })

