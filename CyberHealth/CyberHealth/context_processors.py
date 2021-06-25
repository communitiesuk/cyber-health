from users.models import OrganisationRegion, OrganisationType


def organisation_in_base_context(request):
    """ Takes in a request and for users who are associated with one organisation adds the organisation information to
        that user's session if the user is authenticated. """
    if request.user.is_authenticated:
        session = request.session

        if request.user.is_superuser:
            return {}

        if request.session.get('organisation') is None:
            if len(request.user.organisation_set.values()) == 1:
                session['organisation'] = {}
                org_region_id = request.user.organisation_set.values()[0]['organisation_region_id']
                org_type_id = request.user.organisation_set.values()[0]['organisation_type_id']
                session['organisation']['org_name'] = request.user.organisation_set.values()[0]['name']
                session['organisation']['org_type'] = OrganisationType.objects.get(pk=org_type_id).type
                session['organisation']['org_region'] = OrganisationRegion.objects.get(pk=org_region_id).name
            else:
                # TODO: Add functionality for when a user is associated with multiple organisations
                pass
        return {
            'organisation_name': session['organisation']['org_name'],
            'organisation_type': session['organisation']['org_type'],
            'organisation_region': session['organisation']['org_region'],
        }
    return {}
