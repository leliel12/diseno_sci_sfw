program main
    implicit none
    real(8) :: x, y

    x = 5.0
    y = x
    call sub(x)
    print *, x

contains
    ! Interfaz implicita pero como la rutina esta dentro del 
    ! programa, comparte esas variables con el programa principal
    ! Si se vuelven a definir, son enmascaradas. Como en Python

    elemental subroutine sub(x)
        implicit none
        real(8), intent(in out) :: x
        x = x + 1
    end subroutine

end program main
