from .v1.views import HealthView, RootViews

routers = [
    ("/", RootViews()),
    ("/health", HealthView()),
]
