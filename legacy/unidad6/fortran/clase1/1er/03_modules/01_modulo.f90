module mod1
    implicit none ! Declara implicit none para TODO lo que esté en dentro.

    real :: x
end module mod1

program main
    use mod1 ! análogo a from mod1 import *
    ! use mod1, only: x  << Asi es una mejor manera
    implicit none

    x = 50
    print *, x
end program main
