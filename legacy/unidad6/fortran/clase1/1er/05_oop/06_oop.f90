! Nuevos operadores
module oop
    implicit none

    private
    public :: vector, operator(.dot.)

    type :: vector
        real :: x
        real :: y
    end type

    interface operator(.dot.)
        module procedure :: dot
    end interface

contains

    function dot(self, other)
        class(vector), intent(in) :: self, other
        real :: dot
        dot = self%x * other%x + self%y * other%y
    end function dot

end module

program main
    use oop
    implicit none
    type(vector) :: v1, v2
    
    v1 = vector(1, 2)
    v2 = vector(2, 3)

    print *, v1 .dot. v2
end program main
