function f(x)
    real(8), intent(in) :: x
    real(8) :: f

    f = 2*x
end function f

function f2(x) result(y)
    real :: x
    real :: y

    y = 2*x
end function

real(8) function f3(x)
    real :: x

    f3 = 2*x
end function f3
