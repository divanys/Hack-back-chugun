from src.core.dep.depedencies_api import InterfaceUnitOfWork
from src.core.dto.recommends_dto import CreateRecommends, AllUserRecommends
from src.core.errors.auth_errors import AuthErrors
from src.core.errors.recommends_errors import RecommendsErrors
from src.other.enums.api_enums import UserTypesEnum
from src.databases.postgres.models import Recommends  # noqa


class RecommendsService:

    @classmethod
    async def create_recommends(
        cls,
        token_data: dict,
        uow: InterfaceUnitOfWork,
        new_rec: CreateRecommends,  # noqa
    ) -> None:
        """
        Создание рекомендации
        :param token_data:
        :param uow:
        :param new_portfolio:
        :return:
        """

        async with uow:
            user_data = await uow.user_repository.get_one(
                _id=new_rec.id_us_ch
            )  # noqa
            student_data = await uow.user_repository.get_one(_id=token_data.get('sub'))
            if user_data:
                if user_data[0].id_user_type == UserTypesEnum.TEACHER.value and student_data[0].id_user_type == UserTypesEnum.USER.value: # noqa
                    is_created = await uow.recommends_repository.create_data(
                        model_data=Recommends(
                            id_user=new_rec.id_user,
                            id_us_ch=new_rec.id_us_ch,
                            description=new_rec.description
                        )
                    )

                    if is_created:
                        return
                    await RecommendsErrors.no_create_recommends()
            await AuthErrors.no_access()

    @classmethod
    async def get_my_recommends(
        cls, token_data: dict, uow: InterfaceUnitOfWork
    ) -> AllUserRecommends:
        """
        Получение всех рекомендаций пользователя
        :param token_data:
        :param uow:
        :return:
        """

        async with uow:
            my_rec = await uow.recommends_repository.get_all(_id=int(token_data.get('sub')))
            all_recommends = AllUserRecommends(recommends=[])
            if my_rec:
                for rec in my_rec:
                    all_recommends.recommends.append(
                        CreateRecommends(
                            id_user=rec[0].id_user,
                            id_us_ch=rec[0].id_us_ch,
                            description=rec[0].description
                        )
                    )
            return all_recommends

    @classmethod
    async def delete_recommends(
        cls,
        token_data: dict,
        uow: InterfaceUnitOfWork,
        id_rec: int,
    ) -> None:
        """
        Удаление рекомендации
        :param token_data:
        :param uow:
        :return:
        """

        async with uow:
            user_data = await uow.user_repository.get_one(
                _id=token_data.get('sub')
            )  # noqa
            if user_data:
                if user_data[0].id_user_type == UserTypesEnum.TEACHER.value: # noqa
                    is_deleted = await uow.recommends_repository.delete(
                        _id=id_rec
                    )
                    if is_deleted:
                        return None
                    await RecommendsErrors.no_delete_recommends()

            await AuthErrors.no_access()
