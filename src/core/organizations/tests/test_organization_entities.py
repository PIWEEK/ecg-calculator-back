from core.organizations import organization_entities


def test_organization():
    o = organization_entities.Organization(name = "test 1", address = "address 1")
    assert o.address == "address 1"


def test_organization_for_create():
    c = organization_entities.OrganizationForCreate(name = "test 1")
    assert c.name == "test 1"


def test_organization_for_update():
    u = organization_entities.OrganizationForUpdate(address = "address 1")
    assert u.address == "address 1"


def test_organization_edit():
    o = organization_entities.Organization(name = "test 1", address = "address 1")
    u = organization_entities.OrganizationForUpdate(address = "address 2")
    o.edit(u)
    assert o.address == "address 2"

