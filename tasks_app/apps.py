from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = "tasks_app"

class TasksAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks_app'
