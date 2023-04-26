from django.core.management.base import BaseCommand
from customers.models import Client, Domain

class Command(BaseCommand):
    help = 'Generate starter public domain that tenants shall inherit from.'

    def handle(self, *args, **kwargs):
        try:
            main = Client.objects.get(schema_name = 'public')
            domain = Domain.objects.get(tenant_id=main.id)
        except Client.DoesNotExist:
            pass
            tenant = Client(schema_name='public', name='buupass')
            tenant.save()
            domain = Domain()
            domain.domain = 'buupass.local'
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()
        self.stdout.write(self.style.SUCCESS(f'Main domain {domain.domain} created successfully'))
