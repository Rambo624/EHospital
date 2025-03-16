from base import models as base_models

def services_context(request):
    services = base_models.Service.objects.all()
    return {"services": services}