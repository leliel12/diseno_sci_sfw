program main
    implicit none

    integer, parameter :: n=5
    integer :: i
    real :: x(n)

    i = 0
    do while (i /= 3)
        i = i + 1
        x(i) = i**2
    end do

    print *, i
    print *, x
end program main
