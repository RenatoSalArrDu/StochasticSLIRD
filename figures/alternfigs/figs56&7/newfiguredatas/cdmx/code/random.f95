!                                             29/04/2021
!-------------------------------------------------------!
module random
real, private             :: zero = 0.0, half = 0.5, one = 1.0, two = 2.0
private                   :: integral
public                    :: init_random_seed, random_unif, random_Poisson, &
                             random_gamma, random_exp

contains

subroutine init_random_seed()

     integer :: i, n, clock
     integer, dimension(:), allocatable :: seed

     call random_seed(size = n)
     allocate(seed(n))

     call system_clock(COUNT=clock)

     seed = clock + 37 * (/ (i - 1, i = 1, n) /)
     call random_seed(put = seed)

     deallocate(seed)

end subroutine

function random_unif(a,b) result(ans)

use my_init, only: wp => dp !for double precission constants

real(wp) :: a,b,y

 !call init_random_seed()
call random_number(y)

ans = a + y * (b - a)
end function


function random_Poisson(mu, first) result(ival)
!**********************************************************************
!     Translated to Fortran 90 by Alan Miller from:
!                           RANLIB
!
!     Library of Fortran Routines for Random Number Generation
!
!                    Compiled and Written by:
!
!                         Barry W. Brown
!                          James Lovato
!
!             Department of Biomathematics, Box 237
!             The University of Texas, M.D. Anderson Cancer Center
!             1515 Holcombe Boulevard
!             Houston, TX      77030
!
! This work was supported by grant CA-16672 from the National Cancer Institute.

!                    GENerate POIsson random deviate

!                            function

! Generates a single random deviate from a Poisson distribution with mean mu.

!                            Arguments

!     mu --> The mean of the Poisson distribution from which
!            a random deviate is to be generated.
!                              real mu

!                              Method

!     For details see:

!               Ahrens, J.H. and Dieter, U.
!               Computer Generation of Poisson Deviates
!               From Modified Normal Distributions.
!               ACM Trans. Math. Software, 8, 2
!               (June 1982),163-179

!     TABLES: COEFFICIENTS A0-A7 FOR STEP F. FACTORIALS FACT
!     COEFFICIENTS A(K) - FOR PX = FK*V*V*SUM(A(K)*V**K)-DEL

!     SEPARATION OF CASES A AND B

!     .. Scalar Arguments ..
real, intent(in)    :: mu
logical, intent(in) :: first
integer             :: ival
!     ..
!     .. Local Scalars ..
real          :: b1, b2, c, c0, c1, c2, c3, del, difmuk, e, fk, fx, fy, g,  &
                 omega, px, py, t, u, v, x, xx
real, save    :: s, d, p, q, p0
integer       :: j, k, kflag
logical, save :: full_init
integer, save :: l, m
!     ..
!     .. Local Arrays ..
real, save    :: pp(35)
!     ..
!     .. Data statements ..
real, parameter :: a0 = -.5, a1 = .3333333, a2 = -.2500068, a3 = .2000118,  &
                   a4 = -.1661269, a5 = .1421878, a6 = -.1384794,   &
                   a7 = .1250060

real, parameter :: fact(10) = (/ 1., 1., 2., 6., 24., 120., 720., 5040.,  &
                                 40320., 362880. /)

!     ..
!     .. Executable Statements ..
if (mu > 10.0) then
!     C A S E  A. (RECALCULATION OF S, D, L if MU HAS CHANGED)

  if (first) then
    s = SQRT(mu)
    d = 6.0*mu*mu

!             THE POISSON PROBABILITIES PK EXCEED THE DISCRETE NORMAL
!             PROBABILITIES FK WHENEVER K >= M(MU). L=IFIX(MU-1.1484)
!             IS AN UPPER BOUND TO M(MU) FOR ALL MU >= 10 .

    l = mu - 1.1484
    full_init = .false.
  end if


!     STEP N. NORMAL SAMPLE - random_normal() FOR STANDARD NORMAL DEVIATE

  g = mu + s*random_normal()
  if (g > 0.0) then
    ival = g

!     STEP I. IMMEDIATE ACCEPTANCE if ival IS LARGE ENOUGH

    if (ival>=l) return

!     STEP S. SQUEEZE ACCEPTANCE - SAMPLE U

    fk = ival
    difmuk = mu - fk
    call random_number(u)
    if (d*u >= difmuk*difmuk*difmuk) return
  end if

!     STEP P. PREPARATIONS FOR STEPS Q AND H.
!             (RECALCULATIONS OF PARAMETERS if NECESSARY)
!             .3989423=(2*PI)**(-.5)  .416667E-1=1./24.  .1428571=1./7.
!             THE QUANTITIES B1, B2, C3, C2, C1, C0 ARE FOR THE HERMITE
!             APPROXIMATIONS TO THE DISCRETE NORMAL PROBABILITIES FK.
!             C=.1069/MU GUARANTEES MAJORIZATION BY THE 'HAT'-function.

  if (.NOT. full_init) then
    omega = .3989423/s
    b1 = .4166667E-1/mu
    b2 = .3*b1*b1
    c3 = .1428571*b1*b2
    c2 = b2 - 15.*c3
    c1 = b1 - 6.*b2 + 45.*c3
    c0 = 1. - b1 + 3.*b2 - 15.*c3
    c = .1069/mu
    full_init = .true.
  end if

  if (g < 0.0) goto 50

!             'SUBROUTINE' F IS CALLED (KFLAG=0 FOR CORRECT return)

  kflag = 0
  goto 70

!     STEP Q. QUOTIENT ACCEPTANCE (RARE CASE)

  40 if (fy-u*fy <= py*EXP(px-fx)) return

!     STEP E. EXPONENTIAL SAMPLE - random_exponential() FOR STANDARD EXPONENTIAL
!             DEVIATE E AND SAMPLE T FROM THE LAPLACE 'HAT'
!             (if T <= -.6744 then PK < FK FOR ALL MU >= 10.)

  50 e = random_exp(1.0)
  call random_number(u)
  u = u + u - one
  t = 1.8 + SIGN(e, u)
  if (t <= (-.6744)) goto 50
  ival = mu + s*t
  fk = ival
  difmuk = mu - fk

!             'SUBROUTINE' F IS CALLED (KFLAG=1 FOR CORRECT return)

  kflag = 1
  goto 70

!     STEP H. HAT ACCEPTANCE (E IS REPEATED ON REJECTION)

  60 if (c*ABS(u) > py*EXP(px+e) - fy*EXP(fx+e)) goto 50
  return

!     STEP F. 'SUBROUTINE' F. CALCULATION OF PX, PY, FX, FY.
!             CASE ival < 10 USES FACTORIALS FROM TABLE FACT

  70 if (ival>=10) goto 80
  px = -mu
  py = mu**ival/fact(ival+1)
  goto 110

!             CASE ival >= 10 USES POLYNOMIAL APPROXIMATION
!             A0-A7 FOR ACCURACY WHEN ADVISABLE
!             .8333333E-1=1./12.  .3989423=(2*PI)**(-.5)

  80 del = .8333333E-1/fk
  del = del - 4.8*del*del*del
  v = difmuk/fk
  if (ABS(v)>0.25) then
    px = fk*LOG(one + v) - difmuk - del
  else
    px = fk*v*v* (((((((a7*v+a6)*v+a5)*v+a4)*v+a3)*v+a2)*v+a1)*v+a0) - del
  end if
  py = .3989423/SQRT(fk)
  110 x = (half - difmuk)/s
  xx = x*x
  fx = -half*xx
  fy = omega* (((c3*xx + c2)*xx + c1)*xx + c0)
  if (kflag <= 0) goto 40
  goto 60

!---------------------------------------------------------------------------
!     C A S E  B.    mu < 10
!     START NEW TABLE AND CALCULATE P0 if NECESSARY

else
  if (first) then
    m = MAX(1, INT(mu))
    l = 0
    p = EXP(-mu)
    q = p
    p0 = p
  end if

!     STEP U. UNIFORM SAMPLE FOR INVERSION METHOD

  do
    call random_number(u)
    ival = 0
    if (u <= p0) return

!     STEP T. TABLE COMPARISON UNTIL THE end PP(L) OF THE
!             PP-TABLE OF CUMULATIVE POISSON PROBABILITIES
!             (0.458=PP(9) FOR MU=10)

    if (l == 0) goto 150
    j = 1
    if (u > 0.458) j = MIN(l, m)
    do k = j, l
      if (u <= pp(k)) goto 180
    end do
    if (l == 35) CYCLE

!     STEP C. CREATION OF NEW POISSON PROBABILITIES P
!             AND THEIR CUMULATIVES Q=PP(K)

    150 l = l + 1
    do k = l, 35
      p = p*mu / k
      q = q + p
      pp(k) = q
      if (u <= q) goto 170
    end do
    l = 35
  end do

  170 l = k
  180 ival = k
  return
end if

return
end function random_Poisson

real function random_exp(s)

! Adapted from Fortran 77 code from the book:
!     Dagpunar, J. 'Principles of random variate generation'
!     Clarendon Press, Oxford, 1988.   ISBN 0-19-852202-9

! function GENERATES A RANDOM VARIATE IN [0,INFINITY) FROM
! A NEGATIVE EXPONENTIAL DlSTRIBUTION WlTH DENSITY PROPORTIONAL
! TO EXP(-random_exponential), USING INVERSION.

implicit none
real, intent(in)    :: s
!     Local variable
real  :: r

do
  call random_number(r)
  if (r > zero) exit
end do

random_exp = -log(r )/s
return

end function random_exp


function random_gamma(alpha,beta) result(x)
   implicit none
   real,intent(in) :: alpha,beta
   real :: x
   call random_stdgamma(alpha,x)
   x = x*beta
end function random_gamma

! ------------------  Needed subroutines and functions -------------------!
real function random_normal()

! Adapted from the following Fortran 77 code
!      ALGORITHM 712, COLLECTED ALGORITHMS FROM ACM.
!      THIS WORK PUBLISHED IN TRANSACTIONS ON MATHEMATICAL SOFTWARE,
!      VOL. 18, NO. 4, DECEMBER, 1992, PP. 434-435.

!  The function random_normal() returns a normally distributed pseudo-random
!  number with zero mean and unit variance.

!  The algorithm uses the ratio of uniforms method of A.J. Kinderman
!  and J.F. Monahan augmented with quadratic bounding curves.

implicit none

!     Local variables
real     :: s = 0.449871, t = -0.386595, a = 0.19600, b = 0.25472,           &
            r1 = 0.27597, r2 = 0.27846, u, v, x, y, q

!     Generate P = (u,v) uniform in rectangle enclosing acceptance region

do
  call random_number(u)
  call random_number(v)
  v = 1.7156 * (v - half)

!     Evaluate the quadratic form
  x = u - s
  y = ABS(v) - t
  q = x**2 + y*(a*y - b*x)

!     Accept P if inside inner ellipse
  if (q < r1) exit
!     Reject P if outside outer ellipse
  if (q > r2) cycle
!     Reject P if outside acceptance region
  if (v**2 < -4.0*LOG(u)*u**2) exit
end do

!     Return ratio of P's coordinates as the normal deviate
random_normal = v/u
return

end function random_normal

subroutine random_stdgamma_alpha_ge_1(alpha,x)
  use my_init
   implicit none
   real,intent(in) :: alpha
   real,intent(out) :: x
   real :: y,t,u1,u2
   do
      u1 = random_unif(one,rero)
      !call random_stduniform(u1)
      y = -log(u1)
      t = (y/exp(y-1))**(alpha-1)
      u2 = random_unif(one,rero)
      if(u2 <= t) then
         x = alpha*y
         exit
      end if
   end do
end subroutine random_stdgamma_alpha_ge_1

subroutine random_stdgamma(alpha,x)
  use my_init
   implicit none
   real,intent(in) :: alpha
   real,intent(out) :: x
   real :: g,u
   if(alpha<=0) then
      stop "alpha<=0"
   else if(alpha<1) then
      call random_stdgamma_alpha_ge_1(alpha+1.0,g)
      !call random_stduniform(u)
      u = random_unif(one,rero)
      x = g*u**(1.0/alpha)
   else
      call random_stdgamma_alpha_ge_1(alpha,x)
   end if
end subroutine random_stdgamma


end module
