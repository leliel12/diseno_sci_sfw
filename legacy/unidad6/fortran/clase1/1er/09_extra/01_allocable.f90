! Fortran permite alocacion dinamica de memoria
program main
    implicit none
    real, allocatable :: a(:) ! Un array de dimension variable

    ! Asignarle una dimension de 3
    allocate(a(3))
    a = [1, 2, 3]
    print *, a

    ! La asignacion tambien puede ser implicita, en este caso
    ! se reasigna de 3 a 4
    a = [a, 4.0]
    print *, a

    ! Liberar memoria
    deallocate(a)

    print *, a
end program main
