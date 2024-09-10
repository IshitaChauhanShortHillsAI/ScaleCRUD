from django.db import transaction
import csv
from const import DATASET_PATH
from crudx10m.models import DemographicDataTest

def handle(self, *args, **kwargs):
    file_path = DATASET_PATH
    batch_size = 10000

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        batch = []

        for row in reader:
            batch.append(DemographicDataTest(
                age=int(row[0]),
                workclass=row[1] if row[1] != '?' else None,
                fnlwgt=int(row[2]),
                education=row[3],
                education_num=int(row[4]),
                marital_status=row[5],
                occupation=row[6] if row[6] != '?' else None,
                relationship=row[7],
                race=row[8],
                sex=row[9],
                capital_gain=int(row[10]),
                capital_loss=int(row[11]),
                hours_per_week=int(row[12]),
                native_country=row[13] if row[13] != '?' else None,
                income=row[14],
            ))

            if len(batch) >= batch_size:
                with transaction.atomic():
                    DemographicDataTest.objects.bulk_create(batch)
                batch = []

        if batch:
            with transaction.atomic():
                DemographicDataTest.objects.bulk_create(batch)
    
    self.stdout.write(self.style.SUCCESS('Data successfully loaded into the database!'))
