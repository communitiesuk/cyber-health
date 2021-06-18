from users.models import OrganisationRegion, OrganisationType

def organisation_in_base_context(request):
    if (request.user.is_authenticated):
        # user is logged in, get organisation details
        # re-use from session if possible
        session = request.session
                
        if session.get('organisation') is None:
            if len(request.user.organisation_set.values()) == 1:
                session['organisation'] = {}
                # for users who are associated with one organisation
                # ids
                org_region_id = request.user.organisation_set.values()[0]['organisation_region_id']
                org_type_id = request.user.organisation_set.values()[0]['organisation_type_id']

                # strings
                session['organisation']['org_name'] = request.user.organisation_set.values()[0]['name']
                session['organisation']['org_type'] = OrganisationType.objects.get(pk=org_type_id).type
                session['organisation']['org_region'] = OrganisationRegion.objects.get(pk=org_region_id).name
            else:
                # once a user can be associated with multiple organisations, 
                # work out which org user is logged in with
                pass

        return {
            'organisation_name': session['organisation']['org_name'],
            'organisation_type': session['organisation']['org_type'],
            'organisation_region': session['organisation']['org_region'],
        }


    # no org details: return empty dict
    return {}
