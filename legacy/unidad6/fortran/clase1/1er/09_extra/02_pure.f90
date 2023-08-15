pure function f(x)
    ! Un procedimiento puro no permite ningún side-effect
    ! Solamente puede modificarse la variable de salida
    implicit none
    real(8), intent(in) :: x
    real(8) :: f
    ! x = 3
    ! print *, "No puedo printear desde procedimientos puros"
    f = 2*x
end function f
