from django.db import models

AGE_CHOICES = [(i, str(i)) for i in range(1, 101)]  
INCOME_CHOICES = [
    ('Private', 'Private'),
    ('Self-emp-not-inc', 'Self-emp-not-inc'),
    ('Self-emp-inc', 'Self-emp-inc'),
    ('Federal-gov', 'Federal-gov'),
    ('Local-gov', 'Local-gov'),
    ('State-gov', 'State-gov'),
    ('Without-pay', 'Without-pay'),
    ('Never-worked', 'Never-worked'),
]
EDUCATION_CHOICES = [
    ('Bachelors', 'Bachelors'),
    ('Some-college', 'Some-college'),
    ('11th', '11th'),
    ('HS-grad', 'HS-grad'),
    ('Prof-school', 'Prof-school'),
    ('Assoc-acdm', 'Assoc-acdm'),
    ('Assoc-voc', 'Assoc-voc'),
    ('9th', '9th'),
    ('7th-8th', '7th-8th'),
    ('12th', '12th'),
    ('Masters', 'Masters'), 
    ('1st-4th', '1st-4th'),
    ('10th', '10th'),
    ('Doctorate', 'Doctorate'),
    ('5th-6th', '5th-6th'),
    ('Preschool', 'Preschool'),
]
MARITAL_STATUS_CHOICES = [
    ('Married-civ-spouse', 'Married-civ-spouse'),
    ('Divorced', 'Divorced'),
    ('Never-married', 'Never-married'),
    ('Separated', 'Separated'),
    ('Widowed', 'Widowed'),
    ('Married-spouse-absent', 'Married-spouse-absent'),
    ('Married-AF-spouse', 'Married-AF-spouse'),
]
OCCUPATION_CHOICES = [
    ('Tech-support', 'Tech-support'),
    ('Craft-repair', 'Craft-repair'),
    ('Other-service', 'Other-service'),
    ('Sales', 'Sales'),
    ('Exec-managerial', 'Exec-managerial'),
    ('Prof-specialty', 'Prof-specialty'),
    ('Handlers-cleaners', 'Handlers-cleaners'),
    ('Machine-op-inspct', 'Machine-op-inspct'),
    ('Adm-clerical', 'Adm-clerical'),
    ('Farming-fishing', 'Farming-fishing'),
    ('Transport-moving', 'Transport-moving'),
    ('Priv-house-serv', 'Priv-house-serv'),
    ('Protective-serv', 'Protective-serv'),
    ('Armed-Forces', 'Armed-Forces'),
]
RELATIONSHIP_CHOICES = [
    ('Wife', 'Wife'),
    ('Own-child', 'Own-child'),
    ('Husband', 'Husband'),
    ('Not-in-family', 'Not-in-family'),
    ('Other-relative', 'Other-relative'),
    ('Unmarried', 'Unmarried'),
]
RACE_CHOICES = [
    ('White', 'White'),
    ('Asian-Pac-Islander', 'Asian-Pac-Islander'),
    ('Amer-Indian-Eskimo', 'Amer-Indian-Eskimo'),
    ('Other', 'Other'),
    ('Black', 'Black'),
]
SEX_CHOICES = [
    ('Female', 'Female'),
    ('Male', 'Male'),
]
COUNTRY_CHOICES = [
    ('United-States', 'United-States'),
    ('Cambodia', 'Cambodia'),
    ('England', 'England'),
    ('Puerto-Rico', 'Puerto-Rico'),
    ('Canada', 'Canada'),
    ('Germany', 'Germany'),
    ('Outlying-US(Guam-USVI-etc)', 'Outlying-US(Guam-USVI-etc)'),
    ('India', 'India'),
    ('Japan', 'Japan'),
    ('Greece', 'Greece'),
    ('South', 'South'),
    ('China', 'China'),
    ('Cuba', 'Cuba'),
    ('Iran', 'Iran'),
    ('Honduras', 'Honduras'),
    ('Philippines', 'Philippines'),
    ('Italy', 'Italy'),
    ('Poland', 'Poland'),
    ('Jamaica', 'Jamaica'),
    ('Vietnam', 'Vietnam'),
    ('Mexico', 'Mexico'),
    ('Portugal', 'Portugal'),
    ('Ireland', 'Ireland'),
    ('France', 'France'),
    ('Dominican-Republic', 'Dominican-Republic'),
    ('Laos', 'Laos'),
    ('Ecuador', 'Ecuador'),
    ('Taiwan', 'Taiwan'),
    ('Haiti', 'Haiti'),
    ('Columbia', 'Columbia'),
    ('Hungary', 'Hungary'),
    ('Guatemala', 'Guatemala'),
    ('Nicaragua', 'Nicaragua'),
    ('Scotland', 'Scotland'),
    ('Thailand', 'Thailand'),
    ('Yugoslavia', 'Yugoslavia'),
    ('El-Salvador', 'El-Salvador'),
    ('Trinadad&Tobago', 'Trinadad&Tobago'),
    ('Peru', 'Peru'),
    ('Hong', 'Hong'),
    ('Holand-Netherlands', 'Holand-Netherlands'),
]
INCOME_TARGET_CHOICES = [
    ('>50K', '>50K'),
    ('<=50K', '<=50K'),
]


class EmploymentDetails(models.Model):
    id = models.AutoField(primary_key=True)
    education = models.CharField(max_length=50, choices=EDUCATION_CHOICES)
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES, null=True, blank=True)
    workclass = models.CharField(max_length=50, choices=INCOME_CHOICES, null=True, blank=True)
    income = models.CharField(max_length=10, choices=INCOME_TARGET_CHOICES)

    class Meta:
        indexes = [
            models.Index(fields=['education']),
            models.Index(fields=['occupation']),
        ]


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField(choices=AGE_CHOICES)
    employment_details = models.ForeignKey(EmploymentDetails, on_delete=models.SET_NULL, null=True, blank=True)
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICES, default='Never-married')
    relationship = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES, default='Not-in-family')
    race = models.CharField(max_length=50, choices=RACE_CHOICES, default='White')
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default='Male')
    capital_gain = models.IntegerField()
    capital_loss = models.IntegerField()
    hours_per_week = models.IntegerField()
    native_country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default='United-States', null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['age']),
        ]