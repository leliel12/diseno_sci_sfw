! Herencia
module oop
    implicit none

    private
    public :: vector, vector_3d

    type :: vector
        real :: x
        real :: y
    contains
        procedure :: dot
    end type

    type, extends(vector) :: vector_3d
        real :: z
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
    type(vector_3d) :: v1, v2
    
    v1 = vector_3d(1.0, 2.0, 3.0)
    v2 = vector_3d(2.0, 3.0, 5.0)

    print *, v1%dot(v2)

end program main
