import hashlib
from django.core.management.base import BaseCommand
from django.apps import apps

# ANSI escape sequences for colors (optional)
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RED = "\033[31m"

class Command(BaseCommand):
    help = 'Print row count and full MD5 data hash for each model in the default database, formatted as a table'

    def handle(self, *args, **options):
        db = 'default'
        models_by_app = {}

        # Group models by app label
        for model in apps.get_models():
            app_label = model._meta.app_label
            model_name = model.__name__
            models_by_app.setdefault(app_label, []).append((model_name, model))

        for app_label, models in models_by_app.items():
            self.stdout.write(f"\n{BOLD}{CYAN}📦 Aplikace: {app_label}{RESET}")
            # Table header
            self.stdout.write(f"{BOLD}{'Model':<30} | {'Počet řádků':>12} | {'MD5 hash':<32}{RESET}")
            self.stdout.write("-" * (30 + 3 + 12 + 3 + 32))

            for model_name, model in models:
                try:
                    rows = list(model.objects.using(db).all().values())
                    row_count = len(rows)

                    hasher = hashlib.md5()
                    for row in rows:
                        serialized = str(sorted(row.items()))
                        hasher.update(serialized.encode("utf-8"))
                    data_hash = hasher.hexdigest()

                    self.stdout.write(
                        f"{model_name:<30} | {str(row_count):>12} | {GREEN}{data_hash}{RESET}"
                    )

                except Exception as e:
                    self.stdout.write(
                        f"{model_name:<30} | {'CHYBA':>12} | {RED}{str(e)}{RESET}"
                    )
