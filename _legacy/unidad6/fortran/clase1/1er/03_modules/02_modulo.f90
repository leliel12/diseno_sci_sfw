module mod1
    implicit none ! Declara implicit none para TODO lo que esté en dentro.

    real :: x
end module mod1

subroutine sub(var)
    use mod1, only: x
    real, intent(in) :: var

    x = x + var
end subroutine

program main
    use mod1 ! análogo a from mod1 import *
    implicit none

    x = 50
    print *, x
    ! Puede ser un peligro!
    call sub(25.0)
    print *, x
end program main
