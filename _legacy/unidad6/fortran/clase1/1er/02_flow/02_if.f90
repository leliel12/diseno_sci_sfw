program main
    implicit none

    integer, parameter :: n=5
    integer :: i
    real :: x(n)

    do i=1,n
        x(i) = i**2

        if (i == 3) then
            print *, i
            exit  ! sale del loop
        end if

    end do

    print *, x
end program main

! Operadores
! ==========
!  ==   .eq.
!  /=   .ne.
!  >    .gt.
!  <    .lt.
!  >=   .ge.
!  <=   .le.
