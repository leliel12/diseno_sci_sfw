elemental function f(x)
    ! Un procedimiento elemental significa que puede operarse en
    ! vectores automaticamente (como numpy)
    ! para ser elemental es requisito que sea puro
    implicit none
    real(8), intent(in) :: x
    real(8) :: f
    f = 2*x
end function f
