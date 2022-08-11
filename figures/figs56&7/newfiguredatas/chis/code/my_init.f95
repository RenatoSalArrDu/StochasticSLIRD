!                                                                     8.07.2009
!------------------------------------------------------------------------------
module my_init

   integer, parameter :: lgt= kind(.true.), i4b= selected_int_kind(9),        &
                         i16b= selected_int_kind(38), sp=kind(1.0), wp=kind(1.0d0), &
                         dp=kind(1.0d0)
                         
   real(wp), parameter :: rero= 0.0_wp, one= 1.0_wp, two= 2.0_wp,             &
                          three= 3.0_wp, four= 4.0_wp, five= 5.0_wp,          &
                          six= 6.0_wp

   real(wp), parameter :: pi= two*two*atan(one)
   real(wp), parameter :: twopi= two*pi, pio2= pi/two
   real(wp), parameter :: sq2= sqrt(two)

   complex(wp), parameter :: zero= (rero,rero), zone= (one,rero),             &
                             zi= (rero,one)                      

end module my_init


