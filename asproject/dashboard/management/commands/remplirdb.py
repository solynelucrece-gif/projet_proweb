from django.core.management.base import BaseCommand
from dashboard.models import *
import csv

class Command(BaseCommand):
           
    #############################################################################################
    ##### ENREGISTREMENT DES LIGNES DE COMMANDE
    #############################################################################################
    ##### Le code ci-dessous doit être exécuté uniquement après ceux ci-dessus.
    # ### Etant donné que les deux fonctions on le même nom, il faut commenter la fonction ci-dessus
    # ### et son contenu avant exécution
    ################################################################################################# 

    def handle(self, *args, **options):
        print("Début importation...")

        with open("asproject/data/data.csv", "r", encoding="utf-8") as data:
            reader = csv.DictReader(data, delimiter=";")

            for row in reader:

                InstagramUser.objects.get_or_create(
                    user_id=row['user_id'],
                    defaults={
                        'age': row['age'],
                        'gender': row['gender'],
                        'country': row['country'],
                        'income_level': row['income_level'],
                        'employment_status': row['employment_status'],
                        'relationship_status': row['relationship_status'],
                        'has_children': row['has_children'] == "True",
                        'weekly_work_hours': row['weekly_work_hours'],
                        'social_events_per_month': row['social_events_per_month'],
                        'books_read_per_year': row['books_read_per_year'],
                        'posts_created_per_week': row['posts_created_per_week'],
                        'followers_count': row['followers_count'],
                        'account_creation_year': row['account_creation_year'],
                        'content_type_preference': row['content_type_preference'],
                        'preferred_content_theme': row['preferred_content_theme'],
                        'privacy_setting_level': row['privacy_setting_level'],
                        'subscription_status': row['subscription_status'],
                    }
                )

        print("Importation terminée !")
