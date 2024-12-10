from typing import List
from src.databases.postgres.models.users import Users  # noqa
from src.databases.postgres.models.user_hobby import UserHobbies  # noqa
from src.databases.postgres.models.users_type import UsersType  # noqa
from src.databases.postgres.models.tasks import Tasks  # noqa
from src.databases.postgres.models.portfolio import Portfolio  # noqa
from src.databases.postgres.models.courses import Courses  # noqa
from src.databases.postgres.models.vacancies import Vacancies  # noqa
from src.databases.postgres.models.hobbies import Hobbies  # noqa
from src.databases.postgres.models.recommends import Recommends  # noqa
from src.databases.postgres.models.university import University  # noqa
from src.databases.postgres.models.hobby_courses import HobbyCourses  # noqa


__all__: List[str] = [
    "Users",
    "HobbyCourses",
    "Recommends",
    "UsersType",
    "Portfolio",
    "Courses",
    "Tasks",
    "University",
    "UserHobbies",
    "Vacancies",
    "Hobbies",
]
