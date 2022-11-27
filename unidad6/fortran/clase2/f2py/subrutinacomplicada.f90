subroutine sub(n, x, y)
    integer :: n
    real, intent(in) :: x(n)
    real, intent(out) :: y

    y = sum(x)
end subroutine sub
