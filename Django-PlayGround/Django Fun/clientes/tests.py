import random

from faker import Faker
from validate_docbr import CPF

from django.test import TestCase
from rest_framework import status

from django.urls import reverse

from clientes.models import Cliente

fake = Faker("pt_BR")
Faker.seed(10)
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


class CursosTestCase(TestCase):
    def setUp(self):
        self.list_url = reverse("cliente-list")
        self.cliente_1 = Cliente.objects.create(
            nome=nome, email=email, cpf=cpf, rg=rg, celular=celular
        )

    def getRequest(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def postRequest(self):
        data = {"nome": nome, "email": email, "cpf": cpf, "rg": rg, "celular": celular}
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
