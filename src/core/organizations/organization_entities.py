from tools.adt.types import ADT, ADT_WITH_ID, Field, StrField, IntField


class Organization(ADT_WITH_ID):
    name = StrField()
    address = StrField()
    state = StrField()
    country = StrField()
    sector = StrField()
    web = StrField()
    description = StrField()

    def edit(self, organization_for_update):
        self.address = organization_for_update.address
        self.state = organization_for_update.address
        self.country = organization_for_update.country
        self.sector = organization_for_update.address
        self.web = organization_for_update.address
        self.description = organization_for_update.address


class OrganizationForCreate(ADT):
    name = StrField()


class OrganizationForUpdate(ADT):
    address = StrField()
    state = StrField()
    country = StrField()
    sector = StrField()
    web = StrField()
    description = StrField()

