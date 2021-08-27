from .v1.views import HealthView, RootViews, APIViews

routers = [
    ("/", RootViews()),
    ("/health", HealthView()),
    ("/api/car/create", APIViews()),
]
