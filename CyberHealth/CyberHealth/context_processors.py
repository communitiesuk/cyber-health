from assessment.models import OrganisationRegion, OrganisationType

def organisation_in_base_context(request):
    if (request.user.is_authenticated):
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
        # user is not logged in: return empty dict
        return {}
