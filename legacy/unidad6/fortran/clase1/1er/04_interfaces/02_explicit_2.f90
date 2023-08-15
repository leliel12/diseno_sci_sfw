elemental subroutine sub(x)
    implicit none
    real(8), intent(in out) :: x
    x = x + 1
end subroutine

program main
    implicit none
    real(8) :: x

    ! Interfaz explícita
    interface
        elemental subroutine sub(x)
            real(8), intent(in out) :: x
        end subroutine
    end interface

    x = 5.0
    call sub(x)
    print *, x
end program main
