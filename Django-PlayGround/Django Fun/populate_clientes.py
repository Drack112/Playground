from io import StringIO
import os
import django
import random
import tempfile

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from faker import Faker
from validate_docbr import CPF


from clientes.models import Cliente


def get_mock_img(name="test.png", ext="png", size=(50, 50), color=(256, 0, 0)):
    file_obj = StringIO()
    image = Image.new("RGB", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)


def create_people(n):
    fake = Faker("pt_BR")
    Faker.seed(10)
    for _ in range(n):
        cpf = CPF()
        nome = fake.name()
        email = "{}@{}".format(nome.lower(), fake.free_email_domain())
        email = email.replace(" ", "")
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(
            random.randint(10, 21),
            random.randint(100, 999),
            random.randint(100, 999),
            random.randint(0, 9),
        )
        celular = "{}9 {}-{}".format(
            random.randint(10, 21),
            random.randint(4000, 9999),
            random.randint(4000, 9999),
        )
        avatar = tempfile.NamedTemporaryFile(suffix=".jpg").name
        p = Cliente(
            nome=nome, email=email, cpf=cpf, rg=rg, celular=celular, avatar=avatar
        )
        p.save()


create_people(50)
print("Success!")
