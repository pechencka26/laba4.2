if __name__ == "__main__":
    class SocialNetwork:
        """
        Базовый класс "Социальные сети".

        Attributes:
            name (str): Название социальной сети.
            users (int): Количество пользователей.

        Methods:
            __init__(self, name: str, users: int): Конструктор класса.
            __str__(self) -> str: Возвращает информацию о социальной сети в виде строки.
            __repr__(self) -> str: Возвращает строку, представляющую объект для отладки.
        """

        def __init__(self, name: str, users: int):
            self.name = name
            self.users = users

        def __str__(self) -> str:
            return f"{self.name} - {self.users} пользователей"

        def __repr__(self) -> str:
            return f"SocialNetwork({self.name}, {self.users})"


    class VK(SocialNetwork):
        """
        Дочерний класс "ВКонтакте" от базового класса "Социальные сети".

        Additional Attributes:
            online_users (int): Количество пользователей онлайн.

        Methods:
            __init__(self, name: str, users: int, online_users: int): Конструктор класса.
            __str__(self) -> str: Перегрузка метода для вывода информации о ВКонтакте.
            __repr__(self) -> str: Унаследованный метод для отладки.
            update_online_users(self, new_online_users: int) -> None: Обновляет количество пользователей онлайн.

        Note:
            Метод update_online_users добавлен для обновления количества пользователей онлайн.
            Это позволит удобно изменять этот параметр без прямого доступа к атрибуту online_users извне.
        """

        def __init__(self, name: str, users: int, online_users: int):
            super().__init__(name, users)
            self.online_users = online_users

        def __str__(self) -> str:
            return f"{self.name} - {self.users} пользователей, {self.online_users} онлайн"

        def update_online_users(self, new_online_users: int) -> None:
            self.online_users = new_online_users


    class Facebook(SocialNetwork):
        """
        Дочерний класс "Facebook" от базового класса "Социальные сети".

        Additional Attributes:
            ads_revenue (float): Доход от рекламы.

        Methods:
            __init__(self, name: str, users: int, ads_revenue: float): Конструктор класса.
            __str__(self) -> str: Перегрузка метода для вывода информации о Facebook.
            __repr__(self) -> str: Унаследованный метод для отладки.
            calculate_profit(self) -> float: Рассчитывает прибыль на основе дохода от рекламы.

        Note:
            Метод calculate_profit добавлен для расчета прибыли на основе дохода от рекламы.
            Это позволит вычислять прибыль без необходимости напрямую обращаться к атрибуту ads_revenue извне.
        """

        def __init__(self, name: str, users: int, ads_revenue: float):
            super().__init__(name, users)
            self.ads_revenue = ads_revenue

        def __str__(self) -> str:
            return f"{self.name} - {self.users} пользователей, доход от рекламы: {self.ads_revenue}"

        def calculate_profit(self) -> float:
            return self.ads_revenue
    # Write your solution here
    pass
