from django.core.management import BaseCommand
from users.models import Users

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = Users.objects.create(email='jeiromadmin1@mail.ru')
        user.set_password('12345qwertyAc')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()