module quartiles

  implicit none
  private
  public :: quart

   contains

subroutine quart(x, ntr, nt)
  use my_init
  use sorts, only: quicksort

  implicit none
integer, intent(in):: ntr , nt
integer ::  i, k
real(wp), intent(in) :: x(ntr,nt)
real(wp), parameter :: q1 = 0.25_wp, q3 = 0.75_wp
real(wp) :: qh , ql

!dumies
real(wp) :: c, tol, diff1, diff2
integer :: n, ib1,ib2
real(wp) :: y(ntr)

tol = 1.E-8
ib1 = int( ntr * q1 - mod (ntr * q1 , one) )
diff1 = mod(ntr * q1 , one) - rero

ib2 = int( ntr * q3 - mod (ntr * q3 , one) )
diff2 = mod(ntr * q3 , one) - rero

do i = 1 , nt

  do k = 1 , ntr
    y(k) = x(k,i)
  enddo

call quicksort(y, 1, ntr)

  if(diff1 <= tol) then
    ql = ( y(ib1 + 1) + y(ib1) ) / two
  else
    ql = y( ib1 + 1 )
  end if

  if(diff2 <= tol) then
    qh = ( y(ib2 + 1) + y(ib2) ) / two
  else
    qh = y( ib2 + 1 )
  end if

  write(105,'(i8,2ES24.13E3)') i , ql, qh
enddo

end subroutine

end module
