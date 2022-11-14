subroutine sub(x)
    implicit none
    real(8), intent(in out) :: x
    x = x + 1
end subroutine

program main
    implicit none ! (external)
    real(8) :: x

    x = 5.0
    call sub(x)
    print *, x
end program main
