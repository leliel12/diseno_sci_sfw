module noanda
    type :: obj
        real, allocatable :: att(:)
    end type obj

contains

    subroutine noanda_sub(x, y)
        type(obj), intent(in) :: x
        real, intent(out) :: y

        y = sum(x%att)
    end subroutine noanda_sub

    subroutine sianda_sub(n, x, y)
        integer :: n
        real, intent(in) :: x(n)
        real, intent(out) :: y

        type(obj) :: in_obj

        in_obj%att = x

        call noanda_sub(in_obj, y)
    end subroutine sianda_sub

end module noanda
