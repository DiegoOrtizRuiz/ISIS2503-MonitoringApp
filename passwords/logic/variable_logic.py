from ..models import Password

def get_passwords():
    queryset = Password.objects.all()
    return (queryset)

def create_password(form):
    measurement = form.save()
    measurement.save()
    return ()