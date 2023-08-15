!! Modulo para operar vectores
!! Solo a modo de ejemplo! Fortran es vectorial por naturaleza

! Definicion de objeto
module oop
    implicit none

    type :: vector
        real :: x
        real :: y
    end type
end module
