class World:
    def world(self) -> str:
        return f'{self._w()}{self._o()}{self._r()}{self._l()}{self._d()}' 

    def _w(self) -> str:
        return 'w'

    def _o(self) -> str:
        return 'o'
    
    def _r(self) -> str:
        return 'r'
    
    def _l(self) -> str:
        return 'l'
    
    def _d(self) -> str:
        return 'd'
    
    
    
