from assessment.models import OrganisationRegion, OrganisationType

def organisation_in_base_context(request):
    if (request.user.is_authenticated):
        if len(request.user.organisation_set.values()) == 1:
            # for users who are associated with one organisation
            # ids
            org_region_id = request.user.organisation_set.values()[0]['organisation_region_id']
            org_type_id = request.user.organisation_set.values()[0]['organisation_type_id']

            # strings
            org_name = request.user.organisation_set.values()[0]['name']
            org_type = OrganisationType.objects.get(pk=org_type_id).type
            org_region = OrganisationRegion.objects.get(pk=org_region_id).name

            return {
                'organisation_name': org_name,
                'organisation_type': org_type,
                'organisation_region': org_region,
            }
        else:
            # once a user can be associated with multiple organisations, 
            # work out which org user is logged in with
            pass


    # no org details: return empty dict
    return {}
