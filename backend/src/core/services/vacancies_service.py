from src.core.dep.depedencies_api import InterfaceUnitOfWork
from src.core.dto.vacancies_dto import CreateVacancies, AllVacancies
from src.core.errors.auth_errors import AuthErrors
from src.databases.postgres.models import Vacancies
from src.other.enums.api_enums import UserTypesEnum
from src.core.errors.vacancy_errors import VacancyErrors


class VacanciesService:
    @classmethod
    async def create(
        cls,
        token_data: dict,
        uow: InterfaceUnitOfWork,
        new_vacansy: CreateVacancies,  # noqa
    ) -> None:
        """
        Создание вакансии
        :param token_data:
        :param uow:
        :param new_hobby:
        :return:
        """

        async with uow:
            user_data = await uow.user_repository.get_one(
                _id=token_data.get("sub")
            )  # noqa
            if user_data:
                if user_data[0].id_user_type in (
                    UserTypesEnum.WORK.value,
                    UserTypesEnum.ADMIN.value,
                ):  # noqa
                    is_created = await uow.vacancies_repository.create_data(
                        model_data=Vacancies(
                            id_user=new_vacansy.id_user,
                            title_description=new_vacansy.title_description,
                            description=new_vacansy.description,
                        )
                    )
                    if is_created:
                        return None
                    await VacancyErrors.no_create_vacansy()
            await AuthErrors.no_access()

    @classmethod
    async def all_vacansy(cls, uow: InterfaceUnitOfWork) -> AllVacancies:
        """
        Все вакансии
        :param uow:
        :return:
        """

        async with uow:
            all_vac = await uow.vacancies_repository.find_all_vacancies()
            all_vacansy = AllVacancies(vacancies=[])
            for vacancy in all_vac:
                all_vacansy.vacancies.append(
                    CreateVacancies(
                        id_user=vacancy[0].id_user,
                        title_description=vacancy[0].title_description,
                        description=vacancy[0].description,
                    )
                )

            return all_vacansy

    @classmethod
    async def delete_vacansy(
        cls, uow: InterfaceUnitOfWork, token_data: dict, id_vac: int  # noqa
    ) -> None:
        """
        Удаление вакансии
        :param uos:
        :param token_data:
        :param id_hobby:
        :return:
        """

        async with uow:
            user_data = await uow.user_repository.get_one(
                _id=token_data.get("sub")
            )  # noqa
            if user_data:
                if user_data[0].id_user_type in (
                    UserTypesEnum.WORK.value,
                    UserTypesEnum.ADMIN.value,
                ):
                    is_deleted = await uow.vacancies_repository.delete(
                        _id=id_vac
                    )  # noqa
                    if is_deleted:
                        return None
                    await VacancyErrors.no_delete_vacansy()
            await AuthErrors.no_access()
