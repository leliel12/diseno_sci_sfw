! https://blog.hpc.qmul.ac.uk/fortran-parameterized-derived-types-1.html
! 
! Tipos de datos parametrizados
! 
module parametrized
    implicit none
    type :: dtype(n)
        integer, len :: n
        real(8) :: a(n)
    end type
end module parametrized

program main
    use parametrized
    implicit none
    type(dtype(3)) :: t

    t%a = [1, 2, 3]
    print *, t%a

    t%a = [1, 2, 3, 4, 5] ! No lee del 4to en adelante
    print *, t%a
end program

