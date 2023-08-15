module oop
    implicit none

    type :: vector
        real :: x
        real :: y
    end type

end module

! Utilizacion de objeto
program main
    use oop
    implicit none
    type(vector) :: v

    v = vector(1.0, 2.0)

    print *, v%x, v%y

end program main

