program main
    implicit none

    integer, parameter :: n=5
    integer :: i
    real :: x(n)

    do i=1,n
        x(i) = i**2
    end do

    print *, x
end program main
