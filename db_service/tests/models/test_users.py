from db_service.src.models import User
from datetime import date, datetime

user = User(
    id=1,
    name="Алина",
    surname="Ким",
    email="kimalina@example.com",
    phone="+79876543210",
    password="password",
    date_of_birth=date(2000, 1, 1),
    is_active=True,
    created_at=datetime(2022, 1, 1),
    updated_at=datetime(2022, 1, 1),
    deleted_at=datetime(2022, 1, 1),
)

def test_user(user=user):
    assert user.id == 1
    assert isinstance(user.id, int)
    assert user.name == "Алина"
    assert isinstance(user.name, str)
    assert user.surname == "Ким"
    assert isinstance(user.surname, str)
    assert user.email == "kimalina@example.com"
    assert isinstance(user.email, str)
    assert user.phone == "+79876543210"
    assert isinstance(user.phone, str)
    assert user.password == "password"
    assert isinstance(user.password, str)
    assert user.date_of_birth == date(2000, 1, 1)
    assert isinstance(user.date_of_birth, date)
    assert user.is_active == True
    assert isinstance(user.is_active, bool)
    assert user.created_at == datetime(2022, 1, 1)
    assert isinstance(user.created_at, datetime)
    assert user.updated_at == datetime(2022, 1, 1)
    assert isinstance(user.updated_at, datetime)
    assert user.deleted_at == datetime(2022, 1, 1)
    assert isinstance(user.deleted_at, datetime)
    
    