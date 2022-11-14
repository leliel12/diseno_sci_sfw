module mod2
    implicit none

    real, parameter :: const=50
    real :: x

contains

    subroutine sub(input, output)
        real, intent(in) :: input
        real, intent(out) :: output

        output = const * input
    end subroutine sub
end module mod2

program main
    use mod2, only: sub
    implicit none
    real :: x, y

    x = 50

    call sub(x, y)

    print *, x, y
end program main
