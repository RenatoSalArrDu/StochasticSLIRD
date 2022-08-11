MODULE mcintegral

  implicit none
  private
  public :: mc_int

   contains

function mc_int(v,n) result (inv)
  use my_init
  use random, only: random_unif
  implicit none

integer, intent(in) :: n
real(wp), intent(in) :: v(0:n-1)
real(wp) :: inv
integer :: a, b, Nmc,i   !a the lower bound, b the upper bound, Nmc the size of the sampling (the higher, the more accurate the result)
real(wp) :: x
a = 1
b = n-1
Nmc = 10000000
inv = rero

do i = 1 , Nmc             !Starting MC sampling
  x = random_unif(rero ,one) !generating random number x in range [0,1]
  x = a + x*(b-a)          !converting x to be in range [a,b]
  inv = inv + v(int(x))    !summing all values of f(x). EDIT: SUM is also an instrinsic function in Fortran so don't call your variable this, I named it so, to illustrate its purpose
enddo

inv = dfloat( b-a ) * ( inv / dfloat(Nmc) )     !final result of the integral
end function
end module
