module oop
    implicit none

    private
    public :: vector

    ! Definicion de metodos
    type :: vector
        real :: x
        real :: y
    contains
        procedure :: dot
    end type
    
contains

    function dot(self, other)
        class(vector) :: self, other
        real :: dot
        dot = self%x * other%x + self%y * other%y
    end function dot

end module

program main
    use oop
    implicit none
    type(vector) :: v1, v2

    v1 = vector(1.0, 2.0)
    v2 = vector(3.0, 2.0)

    print *, v1%dot(v2)
end program main
