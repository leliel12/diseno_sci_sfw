module mod2
    implicit none

    private  ! Todo privado

    public :: sub

    real :: x = 250

contains

    subroutine sub(input, output)
        real, intent(in) :: input
        real, intent(out) :: output

        output = x * input
    end subroutine sub
end module mod2

program main
    use mod2
    implicit none
    real :: x, y

    x = 50

    call sub(x, y)

    print *, x, y
end program main
