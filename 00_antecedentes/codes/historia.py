def matar(bicho: int, arma: int) -> bool:
    """Recibe un bicho y un arma, ambos enteros que representan
    La cantidad de vida del primero, y cuanto daño hace la segunda
    y retorna True si la cantidad de vida se disminuye 0"""
    return (bicho - arma) <= 0

matar(bicho=100, arma=100)
matar(bicho=100, arma="espada")
