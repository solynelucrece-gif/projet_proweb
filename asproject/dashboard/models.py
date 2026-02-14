from django.db import models

# Create your models here.

# Create your models here.
RELATIONSHIP_STATUS = [
    ('Single','SINGLE'), ('Divorced','DIVORCED'), ('Married','MARRIED'), ('Widowed','WIDOWED'), ('In a relationship','IN A RELATIONSHIP')
]
EMPLOYMENT_STATUS = [
    ('Freelancer','FREELANCER'), ('Full-time employed','FULL-TIME EMPLOYED'), ('student','STUDENT'), ('Unemployed','UNEMPLOYED'), ('Part-time','PART-TIME'), ('Retired','RETIRED')
]

GENDER = {
    'Female':'FEMALE', 'Male':'MALE', 'Non-binary':'NON-BINARY', 'Prefer not to say':'PREFER NOT TO SAY'
}

CONTENT_TYPE_PREFERENCE = {
    'Photos':'PHOTOS', 'Videos':'VIDEOS', 'Live':'LIVE', 'Mixed':'MIXED', 'Reels':'REELS'
}

SUBSCRIPTION_STATUS = {
    'Free':'FREE', 'Premium':'PREMIUM', 'Business':'BUSINESS'
}

PRIVACY_SETTING_LEVEL = {
    'Public':'PUBLIC', 'Friends Only':'FRIENDS ONLY', 'Private':'PRIVATE'
}
INCOME_LEVEL = {
    'Low':'LOW', 'Middle':'MIDDLE', 'Upper-middle':'UPPER-MIDDLE', 'High':'HIGH'
}
HAS_CHILDREN = {
    'no':'NO', 'yes':'YES'
}


class InstagramUser(models.Model):
    user_id = models.IntegerField(unique=True, primary_key=True)
    age = models.IntegerField(verbose_name='Age')
    gender = models.CharField(max_length=20, verbose_name='Genre', choices=GENDER)
    country = models.CharField(max_length=100, verbose_name='Pays')
    income_level = models.CharField(max_length=50, verbose_name='Niveau de revenu', choices=INCOME_LEVEL)
    employment_status = models.CharField(max_length=50, verbose_name='Statut d\'emploi', choices=EMPLOYMENT_STATUS)
    relationship_status = models.CharField(max_length=50, verbose_name='Statut relationnel', choices=RELATIONSHIP_STATUS)
    has_children = models.CharField(max_length=10, verbose_name='A des enfants', choices=HAS_CHILDREN)
    weekly_work_hours = models.DecimalField(verbose_name='Heures de travail par semaine', max_digits=5, decimal_places=2)
    social_events_per_month = models.IntegerField(verbose_name='Événements sociaux par mois')
    books_read_per_year = models.IntegerField(verbose_name='Livres lus par an')
    posts_created_per_week = models.IntegerField(verbose_name='Publications créées par semaine')
    followers_count = models.IntegerField(verbose_name='Nombre de followers')
    account_creation_year = models.IntegerField(verbose_name='Année de création du compte')
    content_type_preference = models.CharField(max_length=100, verbose_name='Préférence de type de contenu', choices=CONTENT_TYPE_PREFERENCE)
    preferred_content_theme = models.CharField(max_length=100, verbose_name='Thème préféré du contenu')
    privacy_setting_level = models.CharField(max_length=50, verbose_name='Niveau des paramètres de confidentialité', choices=PRIVACY_SETTING_LEVEL)
    subscription_status = models.CharField(max_length=50, verbose_name='Statut d\'abonnement', choices=SUBSCRIPTION_STATUS)

    def __str__(self):
        return self.user_id
