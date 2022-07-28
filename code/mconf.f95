module conf

implicit none
private !:: !nextpar
public :: mconf, rtf_n

 contains

  function rtf_n(nt,tsh,ti,tl) result(rt)
   use my_init
   implicit none

   integer, intent(in) :: nt, ti, tl, tsh
   integer :: d, j, i
   integer :: in(nt)
   real(wp) :: rt(nt-tsh + 1), inf(nt)

   rt = rero
   inf = rero

   open(unit=5, file='state.dat', status='old')
   do j = 1 , nt
     read(5,*) d, in(j)   !maybe we should start counting only after incidence
     if (j >= ti+tl) then
       do i =1, ti
         inf(j) = inf(j) +  dfloat(in(j-tl- i))
       enddo
     endif
     if (j >=tsh) then
       rt(j - tsh + 1) = dfloat( in(j) ) / inf(j)
     endif
   enddo
   close(unit=5)

  end function



 function mconf(j,wpar) result (cf)
   use my_init
   implicit none

   integer, intent(in) :: j
   real(wp) :: cf
   real(wp), intent(in) :: wpar(3,10)
   integer :: i


   if ( j <= int(wpar(3,1)) ) then
     cf  =  one
   elseif ( j > int(wpar(3,1)) .and. j <= int(wpar(3,1)) + int(wpar(2,1))) then
     cf = - (one - wpar(1,1))/wpar(2,1) * (dfloat(j) - wpar(3,1)) + one
   elseif ( j > int(wpar(3,1)) + int(wpar(2,1)) .and. j <= int(wpar(3,2)) ) then
     cf = wpar(1,1)
   elseif ( j > int(wpar(3,2)) .and. j <= int( wpar(3,2) + wpar(2,2)) ) then
     cf = - (wpar(1,1) - wpar(1,2))/wpar(2,2) * (dfloat(j) - wpar(3,2)) + wpar(1,1)
   elseif ( j > int(wpar(3,2)) + int(wpar(2,2)) .and. j <= int(wpar(3,3)) ) then
     cf = wpar(1,2)
   elseif ( j > int(wpar(3,3)) .and. j <= int(wpar(3,3) + wpar(2,3)) ) then
     cf = - (wpar(1,2) - wpar(1,3))/wpar(2,3) * (dfloat(j) - wpar(3,3)) + wpar(1,2)
   elseif ( j > int(wpar(3,3) + wpar(2,3)) .and. j <= int(wpar(3,4)) ) then
     cf = wpar(1,3)
   elseif (j > int(wpar(3,4)) .and. j <= int(wpar(3,4) + wpar(2,4)) ) then
     cf = - (wpar(1,3) - wpar(1,4))/wpar(2,4) * (dfloat(j) - wpar(3,4)) + wpar(1,3)
   elseif (j > int(wpar(3,4) + wpar(2,4)) .and.j <= int(wpar(3,5)) ) then
     cf = wpar(1,4)
   elseif (j > int(wpar(3,5)) .and. j <= int(wpar(3,5) + wpar(2,5)) ) then
     cf = - (wpar(1,4) - wpar(1,5))/wpar(2,5) * (dfloat(j) - wpar(3,5)) + wpar(1,4)
   elseif ( j > int(wpar(3,5) + wpar(2,5)).and.j<= int(wpar(3,6)) ) then
     cf = wpar(1,5)
   elseif ( j > int(wpar(3,6)) .and. j <= int(wpar(3,6) + wpar(2,6)) ) then
     cf = - (wpar(1,5) - wpar(1,6))/wpar(2,6) * (dfloat(j) - wpar(3,6)) + wpar(1,5)
   elseif ( j > int(wpar(3,6) + wpar(2,6)).and. j<= int(wpar(3,7)) ) then
     cf = wpar(1,6)
   elseif ( j > int(wpar(3,7)) .and. j <= int(wpar(3,7) + wpar(2,7)) ) then
     cf = - (wpar(1,6) - wpar(1,7))/wpar(2,7) * (dfloat(j) - wpar(3,7)) + wpar(1,6)
   elseif ( j > int(wpar(3,7) + wpar(2,7)) .and. j<= int(wpar(3,8)) ) then
     cf = wpar(1,7)
   elseif ( j > int(wpar(3,8)) .and. j <= int(wpar(3,8) + wpar(2,8)) ) then
     cf = - (wpar(1,7) - wpar(1,8))/wpar(2,8) * (dfloat(j) - wpar(3,8)) + wpar(1,7)
   elseif ( j > int(wpar(3,8) + wpar(2,8)) .and. j<= int(wpar(3,9)) ) then
     cf = wpar(1,8)
   elseif ( j > int(wpar(3,9)) .and. j <= int(wpar(3,9) + wpar(2,9)) ) then
     cf = - (wpar(1,8) - wpar(1,9))/wpar(2,9) * (dfloat(j) - wpar(3,9)) + wpar(1,8)
   elseif ( j > int(wpar(3,9) + wpar(2,9)).and. j<= int(wpar(3,10))) then
     cf = wpar(1,9)
   elseif ( j > int(wpar(3,10)) .and. j <= int(wpar(3,10) + wpar(2,10))) then
     cf = - (wpar(1,9) - wpar(1,10))/wpar(2,10) * (dfloat(j) - wpar(3,10)) + wpar(1,9)
   elseif ( j > int(wpar(3,10) + wpar(2,10)) ) then
     cf = wpar(1,10)
   endif
 end function

 ! subroutine nextpar
 ! character(len=1) :: chr
 !   do
 !     read (5,'(a1)') chr
 !     if (chr(1:1) /= 'c') exit
 !   end do
 ! end subroutine nextpar

end module
