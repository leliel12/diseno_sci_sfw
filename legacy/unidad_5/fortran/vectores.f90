module vectores
    implicit none
    contains

    ! Producto escalar entre dos vectores u, v de longitud n
    function producto_escalar(n, u, v) result(p)
        integer, intent(in) :: n
        double precision, intent(in) :: u(n), v(n)
        double precision :: p
        p = dot_product(u, v)
    end function

    ! Producto vectorial entre dos vectores u, v de longitud 3
    function producto_vectorial(u, v) result(w)
        double precision, intent(in) :: u(3), v(3)
        double precision :: w(3)
        w(1) = u(2) * v(3) - u(3) * v(2)
        w(2) = u(3) * v(1) - u(1) * v(3)
        w(3) = u(1) * v(2) - u(2) * v(1)
    end function
end module
