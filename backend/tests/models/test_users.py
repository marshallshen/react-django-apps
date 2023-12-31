import pytest
from backend.models import User


@pytest.mark.django_db
def test_user(*_):
    user = User.objects.create(
        first_name="Barack",
        last_name="Obama",
        email="barack.obama@gmail.com",
        status=1,
    )

    assert user.first_name == "Barack"
