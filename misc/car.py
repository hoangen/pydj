from pydj.di.decorator import bean


@bean
class Engine:
    pass


@bean
class Wheels:
    def __init__(self, wheels_count: int = 4):
        self.wheels_count = wheels_count

    def __str__(self) -> str:
        return f'{self.wheels_count}'


@bean
class Person:
    def __init__(self, name: str = 'Unknown'):
        self.name = name

    def __str__(self) -> str:
        return f'{self.name}'


@bean
class Car:
    def __init__(self, engine: Engine, wheels: Wheels, driver: Person):
        self.engine = engine
        self.wheels = wheels
        self.driver = driver

    def __str__(self) -> str:
        return f'{self.driver} on {self.wheels}.'
