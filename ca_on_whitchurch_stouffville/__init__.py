from __future__ import unicode_literals
from utils import CanadianJurisdiction
from pupa.scrape import Organization


class WhitchurchStouffville(CanadianJurisdiction):
    classification = 'legislature'
    division_id = 'ocd-division/country:ca/csd:3519044'
    division_name = 'Whitchurch-Stouffville'
    name = 'Town of Whitchurch-Stouffville'
    url = 'http://www.townofws.ca'

    def get_organizations(self):
        organization = Organization(self.name, classification=self.classification)

        organization.add_post(role='Mayor', label=self.division_name, division_id=self.division_id)
        for ward_number in range(1, 7):
            # Until a boundary set is received and loaded into Represent, we treat Uxbridge as having no divisions.
            # organization.add_post(role='Councillor', label='Ward {}'.format(ward_number), division_id=self.division_id)
            organization.add_post(role='Councillor', label='Whitchurch-Stouffville (seat {})'.format(ward_number), division_id=self.division_id)

        yield organization