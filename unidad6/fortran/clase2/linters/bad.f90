program main
    !comment
    implicit   none
    real*8 x
    real*4 y(3)
    integer i

    x = 2.3
    y  =[2,  3, 1]

    x = x + x + x + 2  + 3 + 2 + 1 + 2 + 4 + 2341 + x + x + 123 + 4 + 5 + 2 + x + 1 + 3 + 1 + 2 + 5 + 2 + 10

    do  i = 1 , 3
        y( i) = 2 * i ** 2
        end do
    
end program main
