program main
    use mod_1, only: sub

    real :: x
    real :: y

    x = 2
    y = 3

    call sub(x, y)

    print *, x, y
end program main
