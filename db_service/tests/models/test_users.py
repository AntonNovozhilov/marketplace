from datetime import date, datetime

from db_service.src.models import User, UserRole

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
    role=UserRole.ADMIN,
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
    assert user.is_active == user.is_active
    assert isinstance(user.is_active, bool)
    assert user.created_at == datetime(2022, 1, 1)
    assert isinstance(user.created_at, datetime)
    assert user.updated_at == datetime(2022, 1, 1)
    assert isinstance(user.updated_at, datetime)
    assert user.deleted_at == datetime(2022, 1, 1)
    assert isinstance(user.deleted_at, datetime)
    assert user.role == UserRole.ADMIN


def test_user_role():
    u1 = UserRole.ADMIN
    u2 = UserRole.USER
    u3 = UserRole.SELLER
    assert isinstance(u1, UserRole)
    assert isinstance(u2, UserRole)
    assert isinstance(u3, UserRole)
    assert u1.value == "admin"
    assert u2.value == "user"
    assert u3.value == "seller"
