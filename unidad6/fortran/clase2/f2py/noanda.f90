subroutine sub_alloc(x, y)
    real, allocatable, intent(in) :: x(:)
    real, intent(out) :: y

    y = sum(x)
end subroutine
