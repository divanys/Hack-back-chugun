from typing import List
from src.databases.postgres.repositories.general_repositories import (
    GeneralRepository,
)  # noqa
from src.databases.postgres.repositories.user_repository import UserRepository  # noqa
from src.databases.postgres.repositories.user_type_repository import (
    UserTypesRepository,
)  # noqa
from src.databases.postgres.repositories.courses_repository import (  # noqa
    CoursesRepository,
)  # nqqa
from src.databases.postgres.repositories.hobby_courses_repository import (
    HobbyCoursesRepository,
)  # noqa
from src.databases.postgres.repositories.hobbies_repository import (
    HobbiesRepository,
)  # noqa
from src.databases.postgres.repositories.vacancies_repository import (
    VacanciesRepository,
)  # noqa
from src.databases.postgres.repositories.university_repository import (
    UniversityRepository,
)  # noqa


__all__: List[str] = [
    "GeneralRepository",
    "UserRepository",
    "UserTypesRepository",
    "CoursesRepository",
    "HobbyCoursesRepository",
    "HobbiesRepository",
    "VacanciesRepository",
]  # noqa
