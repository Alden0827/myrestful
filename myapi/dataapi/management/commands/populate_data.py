# run: python manage.py populate_data

from django.core.management.base import BaseCommand
from faker import Faker
from dataapi.models import DataEntry
import random

class Command(BaseCommand):
    help = "Populate the database with fake data within Region XII (SOCCSKSARGEN)"

    def handle(self, *args, **kwargs):
        fake = Faker('fil_PH')

        region_xii = "SOCCSKSARGEN"  # Fixed Region

        provinces = [
            "Cotabato (North Cotabato)",
            "Sarangani",
            "South Cotabato",
            "Sultan Kudarat",
            "General Santos City"
        ]

        municipalities = {
            "Cotabato (North Cotabato)": ["Kidapawan", "Midsayap", "Kabacan", "Matalam", "Makilala"],
            "Sarangani": ["Alabel", "Glan", "Kiamba", "Malungon"],
            "South Cotabato": ["Koronadal", "Polomolok", "Tupi", "Tampakan"],
            "Sultan Kudarat": ["Isulan", "Tacurong", "Lambayong", "Esperanza"],
            "General Santos City": ["General Santos City"]  # No municipalities, just the city itself
        }

        barangays = [
            "Poblacion", "San Isidro", "San Roque", "Fatima",
            "Lagao", "Apopong", "Katangawan", "Baluan"
        ]

        for _ in range(1000):
            province = random.choice(provinces)
            municipality = random.choice(municipalities[province])

            DataEntry.objects.create(
                REGION=region_xii,
                PROVINCE=province,
                MUNICIPALITY=municipality,
                BARANGAY=random.choice(barangays),
                HH_ID=fake.uuid4(),
                ENTRY_ID=fake.uuid4(),
                FIRST_NAME=fake.first_name(),
                MIDDLE_NAME=fake.first_name() if random.choice([True, False]) else None,
                LAST_NAME=fake.last_name(),
                EXT_NAME=random.choice(["Jr.", "Sr.", None]),
                BIRTHDAY=fake.date_of_birth(minimum_age=18, maximum_age=90),
                AGE=random.randint(18, 90),
                AGE_ON_EDUC=random.randint(5, 25),
                SEX=random.choice(["Male", "Female"]),
                MEMBER_STATUS=random.choice(["Active", "Inactive"]),
                RELATION_TO_HH_HEAD=random.choice(["Head", "Spouse", "Child"]),
                CIVIL_STATUS=random.choice(["Single", "Married", "Widowed"]),
                GRANTEE=random.choice([True, False]),
                HH_SET=fake.word(),
                SOLOPARENT=random.choice([True, False]),
                IPAFFILIATION=fake.word() if random.choice([True, False]) else None,
            )

        self.stdout.write(self.style.SUCCESS("Database populated with localized data for Region XII!"))
