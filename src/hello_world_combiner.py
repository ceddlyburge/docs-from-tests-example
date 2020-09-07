import src.hello as hello
from src.world import World

class HelloWorldCombiner:
    def combine(self) -> str:
        world = World()

        return f'{hello.hello()} {world.world()}' 