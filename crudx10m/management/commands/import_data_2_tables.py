from django.core.management.base import BaseCommand
from django.db import transaction
import csv
from crudx10m.models import EmploymentDetails, Person
from crudx10m.const import DATASET_PATH

class Command(BaseCommand):
    help = 'Bulk create EmploymentDetails and Person entries from CSV files'

    def handle(self, *args, **kwargs):
        self.import_data()

    def import_data(self):
        file_path = DATASET_PATH
        batch_size = 10000

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            employment_batch = []
            person_batch = []

            for row in reader:
                # Create EmploymentDetails entry
                employment_details = EmploymentDetails(
                    education=row[0],
                    occupation=row[6] if row[6] != '?' else None,
                    workclass=row[1] if row[1] != '?' else None,
                    income=row[14],
                )
                employment_batch.append(employment_details)

                if len(employment_batch) >= batch_size:
                    with transaction.atomic():
                        EmploymentDetails.objects.bulk_create(employment_batch)
                        for employment in employment_batch:
                            person_batch.append(
                                Person(
                                    age=int(row[0]),
                                    employment_details=employment,
                                    marital_status=row[5],
                                    relationship=row[7],
                                    race=row[8],
                                    sex=row[9],
                                    capital_gain=int(row[10]),
                                    capital_loss=int(row[11]),
                                    hours_per_week=int(row[12]),
                                    native_country=row[13] if row[13] != '?' else None,
                                )
                            )
                        Person.objects.bulk_create(person_batch)
                    employment_batch = []
                    person_batch = []

            if employment_batch:
                with transaction.atomic():
                    EmploymentDetails.objects.bulk_create(employment_batch)
                    for employment in employment_batch:
                        person_batch.append(
                            Person(
                                age=int(row[0]),
                                employment_details=employment,
                                marital_status=row[5],
                                relationship=row[7],
                                race=row[8],
                                sex=row[9],
                                capital_gain=int(row[10]),
                                capital_loss=int(row[11]),
                                hours_per_week=int(row[12]),
                                native_country=row[13] if row[13] != '?' else None,
                            )
                        )
                    Person.objects.bulk_create(person_batch)

        self.stdout.write(self.style.SUCCESS('EmploymentDetails and Person data successfully loaded into the database!'))
