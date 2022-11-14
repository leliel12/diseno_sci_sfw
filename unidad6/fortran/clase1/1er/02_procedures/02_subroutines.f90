subroutine sub(x, y)
    real(8), intent(in) :: x
    real(8), intent(out) :: y

    y = x**2
end subroutine sub

program main
    implicit none
    real(8) :: x, y

    x = 2
    call sub(x, y)

    print *, x, y
end program main
