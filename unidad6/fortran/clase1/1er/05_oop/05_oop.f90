module oop
    implicit none

    private
    public :: vector, operator(+)

    type :: vector
        real :: x
        real :: y
    end type

    interface operator(+)
        module procedure :: add
    end interface

contains
    
    function add(self, other)
        class(vector), intent(in) :: self, other
        type(vector) :: add
        add%x = self%x + other%x
        add%y = self%y + other%y
    end function

end module

program main
    use oop
    implicit none
    type(vector) :: v1, v2, v3

    v1 = vector(1, 2)
    v2 = vector(5, 3)
    v3 = v1 + v2

    print *, v1%x, v2%x, v3%x
end program main
