program rsir
use my_init
use random, only: random_Poisson, random_unif, init_random_seed, random_exp
use mcintegral, only: mc_int
use conf, only: mconf, rtf_n
use quartiles, only: quart

implicit none
!============= Define variables  ==================!
integer :: ni, ns, nr, nl, nd, sic, nod, t_recov, t_laten, &
           ntot, nsap, ro, t_infecc, hop, cop, traj, &
           ini, ins, inr, inl, ind, tsh, erst, opt, wop

real :: rot

integer, allocatable :: vr(:), vl(:), vd(:), vsic(:) ! memory vectors
real, allocatable :: v_ran(:)     ! vector
integer, allocatable :: vnl(:), vns(:), vni(:), vnr(:), & !cummulant vectors
                        vnp(:), vnd(:)

integer, allocatable :: avnl(:), avns(:), avni(:), avnr(:), &
                        avnp(:), avnd(:), avl(:), avcumv(:) !av. cummulant vectors

real(wp), allocatable:: rt_n(:) !effective rep.num

! alpho:   parameter of Herd function
! hp:      lower limit to achieve stationarity in herd immunity
! gamma:   parameter to simulate gaussian confinement function
! io:      parameter to describe at what stage gaussian confinement begins

real(wp), parameter:: alpho=0.22_wp, hp=0.01_wp, gamma=50.0_wp, io=0.2_wp
real(wp) :: w, hf, cf, leth, un_leth

!dummy variables
integer :: j, i, k, lb, cumvl, fl
real(wp) :: lk, lkk, avarea
real(wp), allocatable :: cumv(:,:), cv(:), area(:), incv(:,:)
real :: start, finish

real(wp) :: wpar(3,10)

integer :: ivl(4)
integer :: rop

! =======================================================!

call cpu_time(start)
call init_random_seed() ! generate random seed


!======== read initial conditions and parameters ========!
open(unit=23, file='par.dat', status='old')
read(23,*) ini, ins, inr, ivl(1), ivl(2), ivl(3), ivl(4), ind, t_recov, t_laten, ntot, &
           ro, hop, leth, cop, traj, tsh, opt, wop, rop
close(unit=23)

open(unit=24,file='wpar.dat',status='old')
do i = 1 , 10
  read(24,*) wpar(3,i), wpar(2,i),  wpar(1,i)
enddo
close(unit=24)


t_infecc = t_recov - t_laten      !infective time
rot= float(ro)/float(t_infecc)    !infections per unit time

write(20 ,'(i8,6ES24.13E3)')  0 , dfloat(inl), dfloat(ins) , dfloat(ini) ,&
                             dfloat(inr), dfloat(ind), dfloat(ini)

! =======================================================!
! one colud in principal introduce fluctuations around rot to simulate
!super or subpar infectious events
if (rop/=0) then
  allocate( v_ran( (ini + ins + inr + inl + ind)*t_infecc ) )
  do i= 1 , size(v_ran)
    if (rop==1) then
      v_ran(i) =  real( random_unif(rero , two* real(rot,wp)) )
    elseif (rop==2) then
      v_ran(i) = real(random_exp(1._sp/rot))
    elseif (rop==3) then
      v_ran(i) =  real(random_Poisson(rot , .true.))
    end if
  enddo
endif

! =============================================================================!
!============== begining of trajectories calculation ==========================!
allocate(avnl(ntot + t_laten), avns(ntot), avni(ntot), avnr(ntot + t_recov),&
         avnp(ntot), avnd(ntot + t_laten), avl(ntot + t_laten), &
         cumv(traj,ntot), cv(ntot), area(traj), rt_n(ntot), &
         incv(traj,ntot))

avnl = 0
avns = 0
avni = 0
avnr = 0
avnd = 0
avl = 0

lk = rero
lkk = rero
rt_n = rtf_n(ntot, tsh, t_infecc, t_laten) * t_infecc/dfloat(ro)

do k = 1 , traj

  allocate( vsic(ntot), vl(ntot + t_laten), vr(ntot + t_recov), &
            vd(ntot + t_laten), vnl(ntot + t_laten),vns(ntot), &
            vni(ntot),vnr(ntot + t_recov), vnd(ntot  +t_laten) , vnp(ntot) )
  vsic = 0
  vl = 0
  vr = 0
  vd = 0
  vnl = 0
  vns = 0
  vni = 0
  vnr = 0
  vnd = 0
  vnp = 0

  lb = 1

  vnl(1) = ivl(4)
  vns(1) = ins
  vni(1) = ini
  vnr(1) = inr
  vnp(1) = vnl(1) + vns(1) + vni(1) + vnr(1)
  vnd(1) = ind

  nl = 0
  ns = 0
  ni = 0
  nr = 0
  nd = 0

  cumvl = ini
  cf = one

  erst=0

  vl(1) = ivl(1)
  vl(2) = ivl(2)
  vl(3) = ivl(3)
  vl(4) = ivl(4)


!=================== Single trajectories calculation ==========================!
  do j = 1  , ntot

    if(j==1) then
      vr(t_recov) = vni(j)
      hf = one
      cf = one
    else

!=================== Herd immunity =====================!
      if (hop == 1) then
        hf = one !no contingency
      else if (hop == 2) then
        hf  =  (one + exp((dfloat(vni(1))/dfloat(vnp(1)))/alpho))/&
        (one + exp((dfloat(cumvl)/dfloat(vnp(1)))/alpho)) &
        * (one - hp) + hp
      endif

! ================= Confinement =========================!
      if (cop==1 .and. wop==0) then !no confinement
        cf = one
      else if (cop==2.and.wop==0) then  ! piecewise confinement
        cf = mconf(j,wpar)
      else if (cop == 3.and.wop==0 .and.  & !confinement upon the cumulative of the incidence
               dfloat(vni(j)) / dfloat(vnp(1)) >= io) then
        cf = exp(- gamma**2 * (dfloat(vni(j)) / dfloat(vnp(1)))**2)
      else if (cop == 4.and.wop==1) then  !confinement upon empirical R(t)
        cf = rt_n(j)
      endif

      if (wop==1) then
        w = cf
      else if (wop==0) then
        w = hf * cf !wise multiplication
      endif

! store weight function
      if (k==1) then
        if (j==1) then
          write(16,'(i8,3ES24.13E3)') j , one , cf , hf
        else
          write(16,'(i8,3ES24.13E3)') j , w , cf , hf
        endif
      else if (traj/=1.and.k==traj/2) then
        if (j==1) then
          write(17,'(i8,3ES24.13E3)') j , one , cf , hf
        else
          write(17,'(i8,3ES24.13E3)') j , w , cf , hf
        endif
      else if (traj>=3.and.k==traj) then
        if (j==1) then
          write(18,'(i8,3ES24.13E3)') j , one , cf , hf
        else
          write(18,'(i8,3ES24.13E3)') j , w , cf , hf
        endif
      endif

! =============== Incidence generation ==================!
      if (ns<=0) then
        sic = 0
        w = rero
      else ! ----------- > total number susceptible in contagious domains
        sic =  0
        do i = 1, ni
          if (rop/=0) then
            nsap = random_Poisson( v_ran(lb) * real(w) ,.true.)
          else
            nsap = random_Poisson( rot * real(w) ,.true.)
          endif
          lb = lb + 1
          sic = sic + nsap
        ! we give here certain conditions to avoid having negative numbers
          if (ns - sic <= 0) then ! --- >  last number of sic is remaining ns
            ns = sic
            exit
          endif
        enddo
      endif

      vsic(j) = sic
      vl(j + t_laten) = vsic(j)
      vr(j + t_recov) = vsic(j)

    endif

! ===================== Deads ===========================!

    if (j==1) then
      nod = 0
      do i = 1 , vni(1)
        un_leth = random_unif(rero , one)
        if (un_leth > one - leth) then
          nod = nod + 1
        end if
      enddo
    else if (j>= t_laten + 1.and.vl(j) /= 0) then
      nod = 0
      do i = 1 , vl(j)
        un_leth = random_unif(rero , one)
        if (un_leth > one - leth) then
          nod = nod + 1
        end if
      enddo
    else
      un_leth = rero
      nod = 0
    endif

    vd(j+ t_laten ) = nod


! =================== Cummulative =======================!
    cumvl = cumvl + vl(j)
    cumv(k,j) = cumvl  ! write cumulant vector
    incv(k,j) = dfloat(vl(j))

! ================ SLIRD evolution =======================!
    vnl(j+1) = vnl(j) + vsic(j) - vl(j)
    vns(j+1) = vns(j) - vsic(j)
    vni(j+1) = vni(j) + vl(j) - vr(j)
    vnr(j+1) = vnr(j) + vr(j) - vd(j)
    vnd(j+1) = vnd(j) + vd(j)
    vnp(j+1) = vnl(j+1) + vns(j+1) + vni(j+1) + vnr(j+1)

    nl = vnl(j+1)
    ns = vns(j+1)
    ni = vni(j+1)
    nr = vnr(j+1)
    nd = vnd(j+1)

    if (ns<=0) then
      ns = 0
    endif


! ============ > write single trajectories
    if (k==1) then
      write(20 ,'(i8,7ES24.13E3)')  j , dfloat(nl), dfloat(ns) , dfloat(ni) ,&
      dfloat(nr), dfloat(nd), dfloat(cumvl)
      write(25,'(7i10)') j , vsic(j), vl(j), vr(j), vni(j), vd(j), nod
    endif

    if (traj>1.and.k==traj/2) then
      write(21 ,'(i8,7ES24.13E3)')  j , dfloat(nl), dfloat(ns) , dfloat(ni) ,&
      dfloat(nr), dfloat(nd), dfloat(cumvl)
      write(26,'(7i10)') j , vsic(j), vl(j), vr(j), vni(j), vd(j), nod
    endif

! =========== > Ommit non-propagated events
    if (j == ntot.and.ns/=ins) then
      lkk = lkk + one
      fl=1
    else if (j>1.and.ns==ins) then
      fl=0
    endif

  enddo !------------- > End of single trajectory calculation

!=============================================================================!

  if (fl==1) then
    avnl = avnl + vnl
    avns = avns + vns
    avni = avni + vni
    avnr = avnr + vnr
    avnd = avnd + vnd
    avnp = avnp + vnp
    avl = avl + vl
  endif

!get minimum and maximum areas under the cummulative curves
!we compare the area of single trajectories and store only the
!smallets and the greatest

  cv = cumv(k,:)
  if (fl == 1) then
   area (k) = mc_int(cv,ntot)
  endif

  deallocate( vsic, vl, vr, vd, vnl, vns, vni, vnr, vnd, vnp )
  lk = lk + one

print*, int(lk), int(lkk)

end do !------------- > End of trajectories calculation
! =============================================================================!


!===================== Averaging over trajectories ============================!
cumvl = ini

if (traj==1) then

  do i = 1 , ntot
    cumvl = cumvl + avl(i)

    write(15, '(i8,7ES24.13E3)') i, dfloat(avl(i)), dfloat(avnl(i)), &
                                 dfloat(avns(i)), dfloat(avni(i)),&
                                 dfloat(avnr(i)), dfloat(avnd(i)), &
                                 dfloat(cumvl)
  enddo

else

  do i = 1 , ntot

    cumvl = cumvl + avl(i)

    if (i == 1) then
      write(15, '(i8,12ES24.13E3)') i, dfloat(avl(i))/lkk, dfloat(inl), &
                         dfloat(ins), dfloat(ini), dfloat(inr), dfloat(ind), &
                         dfloat(ini), cumv(minloc(area),1),cumv(maxloc(area),1), &
                         incv(minloc(area),1), incv(maxloc(area),1)
    else
      write(15, '(i8,12ES24.13E3)') i, dfloat(avl(i))/lkk, dfloat(avnl(i))/lkk, &
                    dfloat(avns(i))/lkk, dfloat(avni(i))/lkk,&
                    dfloat(avnr(i))/lkk, dfloat(avnd(i))/lkk, &
                    dfloat(cumvl)/lkk, cumv(minloc(area),i),cumv(maxloc(area),i),&
                    incv(minloc(area),i), incv(maxloc(area),i)
    endif

  enddo
endif

! compute quartiles
call quart(cumv, traj, ntot)

! =============================================================================!
!write all trajectories
if ( opt == 0 ) then
  do k=1 , traj
    do i = 1 , ntot
      write(100,'(i8,2ES24.13E3)') i, incv(k,i), cumv(k,i)
    enddo
    write(100,*)
  enddo
endif

call cpu_time(finish)
print*, start/60., finish/60., (finish-start)/60.

end program
