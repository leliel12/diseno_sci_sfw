module efun
contains
    elemental function f(x)
        ! Un procedimiento elemental significa que puede operarse en
        ! vectores automaticamente (como numpy)
        ! para ser elemental es requisito que sea puro
        implicit none
        real(8), intent(in) :: x
        real(8) :: f
        f = 2*x
    end function f
end module efun

program main
    use efun, only: f
    implicit none
    real(8) :: x, x2(3)

    x = 5
    x2 = [1, 2, 3]

    print *, "Variable escalar: ", f(x)
    print *, "Variable vectorial: ", f(x2)
end program main
