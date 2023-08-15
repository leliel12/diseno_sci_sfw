module mod_1
    contains
        subroutine sub(x, y)
            real, intent(in) :: x
            real, intent(out) :: y

            y = 2 * x
        end subroutine
end module
