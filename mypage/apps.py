from django.apps import AppConfig


class MypageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mypage'

    def ready(self) -> None:
        # 下記に初期化処理を記載する
        return super().ready()