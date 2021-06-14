from assessment.models import OrganisationRegion, OrganisationType

def organisation_in_base_context(request):
    if (request.user.is_authenticated):
        org_region_id = request.user.organisation_set.values()[0]['organisation_region_id']
        org_type_id = request.user.organisation_set.values()[0]['organisation_type_id']
        return {
            'organisation_name': request.user.organisation_set.values()[0]['name'],
            'organisation_type': OrganisationType.objects.get(pk=org_type_id).type,
            'organisation_region': OrganisationRegion.objects.get(pk=org_region_id).name,
        }
