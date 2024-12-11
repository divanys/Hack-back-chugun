from src.core.dep.depedencies_api import InterfaceUnitOfWork
from src.core.dto.university_dto import CreateUniversity, AllUniversity
from src.core.errors.auth_errors import AuthErrors
from src.databases.postgres.models import University
from src.other.enums.api_enums import UserTypesEnum
from src.core.errors.university_errors import UniversityErrors


class UniversityService:
    @classmethod
    async def create(
        cls,
        token_data: dict,
        uow: InterfaceUnitOfWork,
        new_university: CreateUniversity,  # noqa
    ) -> None:
        """
        Создание учебного заведения
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
                if user_data[0].id_user_type in (UserTypesEnum.ADMIN.value):  # noqa
                    is_created = await uow.university_repository.create_data(
                        model_data=University(
                            name_university=new_university.name_university
                        )
                    )

                    if is_created:
                        return None
                    await UniversityErrors.no_create_university()
            await AuthErrors.no_access()

    @classmethod
    async def all_universities(cls, uow: InterfaceUnitOfWork) -> AllUniversity:
        """
        Все учебные заведения
        :param uow:
        :return:
        """

        async with uow:
            all_university = await uow.university_repository.get_all()
            all_univ_res = AllUniversity(universities=[])
            for univ in all_university:
                all_univ_res.universities.append(
                    {
                        "id_univ": univ[0].id,
                        "name_university": univ[0].name_university
                    }
                )

            return all_univ_res

    @classmethod
    async def delete_university(
        cls, uow: InterfaceUnitOfWork, token_data: dict, id_univ: int  # noqa
    ) -> None:
        """
        Удаление учебного заведения
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
                if user_data[0].id_user_type in (UserTypesEnum.ADMIN.value,):
                    is_deleted = await uow.university_repository.delete(
                        _id=id_univ
                    )  # noqa
                    if is_deleted:
                        return None
                    await UniversityErrors.no_delete_university()
            await AuthErrors.no_access()
