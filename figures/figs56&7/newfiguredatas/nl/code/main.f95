program rsir
use my_init
use random, only: random_Poisson, random_exp, random_unif, &
                  init_random_seed, random_gamma
use mcintegral, only: mc_int
use conf, only: mconf, rtf, rtf_n
use quartiles, only: quart

implicit none
!============= Define variables  ==================!
integer :: ni, ns, nr, nl, nd, sic, nod, t_recov, t_laten, &
           ntot, op, nsap, ro, t_infecc, wop, cop, traj, &
           ini, ins, inr, inl, ind, tsh, ret, erst, opp, opt

real :: rot, kappa, theta

integer, allocatable :: vr(:), vl(:), vd(:), vsic(:) ! memory vectors
real, allocatable :: v_ran(:)     ! random vector
integer, allocatable :: vnl(:), vns(:), vni(:), vnr(:), & !cummulant vectors
                        vnp(:), vnd(:)

integer, allocatable :: avnl(:), avns(:), avni(:), avnr(:), &
                        avnp(:), avnd(:), avl(:), avcumv(:) !av. cummulant vectors



real(wp) :: alpho ,iop , w, hf, cf, &  ! confinement parameters
            leth, un_leth, hp, gamma, io

!dummy variables
integer :: j, i, k, lb, lb2, cumvl, ntott, fl, vrn
real(wp) :: lk, lkk, avarea
real(wp), allocatable :: cumv(:,:), cv(:), area(:), incv(:,:)
real(wp), allocatable:: rt(:), rt_n(:)


! =======================================================!


call init_random_seed() ! generate random seed

!======== read initial conditions and parameters ========!
open(unit=23, file='par.dat', status='old')
read(23,*) ini, ins, inr, inl, ind, t_recov, t_laten, ntot, &
           ro, op, wop, leth, alpho, iop, hp, cop, gamma, io, traj, tsh, ret, &
           opp, opt
close(unit=23)

t_infecc = t_recov - t_laten      !infective time
rot= float(ro)/float(t_infecc)    !infections per unit time
ntott = (ins + ini + inr + inl) * t_infecc !total number of generated random numbers

write(20 ,'(i8,6ES24.13E3)')  0 , dfloat(inl), dfloat(ins) , dfloat(ini) ,&
                             dfloat(inr), dfloat(ind), dfloat(ini)

! =======================================================!


!============= Random number generators ==================!
!we give distribution according to urbanization
!parameters and other stuff. and this is determined trhough
!the different values of op. (see bash file)

allocate(v_ran(ntott)) ! random vector
v_ran = 0

if (opp==0) then
  do i= 1 , ntott
    if (op==1) then
      v_ran(i) =  real( random_unif(rero , two* real(rot,wp)) )
    elseif (op==2) then
      v_ran(i) = real(random_exp(1._sp/rot))
    elseif (op==3) then
      v_ran(i) =  real(random_Poisson(rot , .true.))
    elseif (op==4) then !short tailed gamma distro
      kappa = real(rot,sp)
      theta = real(one,sp)
      v_ran(i) = random_gamma(kappa,theta)
    elseif (op==5) then !longer tailed gamma distro
      kappa = real(four,sp)
      theta = real(rot/four,sp)
      v_ran(i) = random_gamma(kappa,theta)
    elseif(op==6) then !sir model
      v_ran(i) = rot
    end if
  enddo

else if (opp==1) then
  open(unit=23, file='rn.dat', status='old')
  do j=1, ntott
    if (op==1.or.op==2.or.op==4.or.op==5.or.op==7) then
    read(23,*) v_ran(j)
    else if (op==3) then
    read(23,*) vrn
    v_ran(j) = real(vrn,sp)
    endif
  enddo
  close(unit=23)
endif


! =============================================================================!
!============== beginning of different trajectories ============================!
allocate(avnl(ntot + t_laten), avns(ntot), avni(ntot), avnr(ntot + t_recov),&
         avnp(ntot), avnd(ntot + t_laten), avl(ntot + t_laten), &
         cumv(traj,ntot), cv(ntot), area(traj), rt(ntot), rt_n(ntot), &
         incv(traj,ntot))

avnl = 0
avns = 0
avni = 0
avnr = 0
avnd = 0
avl = 0

lk = rero
lkk = rero
rt = rtf(ntot, ret, tsh)/dfloat(ro)
rt_n = rtf_n(ntot, tsh, t_infecc, t_laten) * t_infecc/dfloat(ro)

  allocate( vsic(ntot), vl(ntot + t_laten), vr(ntot + t_recov), &
            vd(ntot + t_laten), vnl(ntot + t_laten),vns(ntot), &
            vni(ntot),vnr(ntot + t_recov), vnd(ntot  +t_laten) , vnp(ntot))


do k = 1 , traj
  !
  ! allocate( vsic(ntot), vl(ntot + t_laten), vr(ntot + t_recov), &
  !           vd(ntot + t_laten), vnl(ntot + t_laten),vns(ntot), &
  !           vni(ntot),vnr(ntot + t_recov), vnd(ntot  +t_laten) , vnp(ntot))
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
  lb2 = 0

  vnl(1) = inl
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

  vr = 0
  vl = 0
  vd = 0
  cumvl = ini
  cf = one

  erst=0


!=================== Single trajectories calculation ==========================!
  do j = 1  , ntot

    if(j==1) then
      vr(t_recov) = vni(j)
      hf = one
      cf = one
    else

!=================== Herd immunity =====================!
    if (wop == 1) then
      hf = one !no contingency
    else if (wop == 2) then
      hf  =  (one + exp((dfloat(vni(1))/dfloat(vnp(1)) - iop)/alpho))/&
        (one + exp((dfloat(cumvl)/dfloat(vnp(1)) - iop)/alpho)) &
        * (one - hp) + hp
    endif
! =======================================================!



! ================= Confinement =========================!


    if (cop==1) then !no confinement
      cf = one

    else if (cop==2) then  ! piecewise confinement
      cf = mconf(j)

    else if (cop==3) then ! R(t) Yorch's confinement
      if ( dfloat(cumvl) > dfloat(vnp(1)) * 0.0005 ) then
        if (rt(j) > one) then
          cf = mconf(j)
        elseif ( rt(j) < one ) then
          cf = rt(j)
        end if
      else
        cf = mconf(j)
      end if
    !confinement upon the cumulative of te incidence
    else if (cop == 4.and. dfloat(vni(j)) / dfloat(vnp(1)) >= io) then
      cf = exp(- gamma**2 * (dfloat(vni(j)) / dfloat(vnp(1)))**2)

   else if (cop == 5) then ! R(t) empirical confinement
      !if (ni>=2000.and.erst==0) then
      if (ni>=1000.and.erst==0) then
        erst=1
        if (rt_n(j) > one) then
          cf = mconf(j)
        elseif ( rt_n(j) < one ) then
          cf = rt_n(j)
        end if
      elseif (erst==1) then
        if (rt_n(j) > one) then
          cf = mconf(j)
        elseif ( rt_n(j) < one ) then
          cf = rt_n(j)
        end if
      else
        cf = mconf(j)
      end if

    endif


    w = cf !hf * cf !wise multiplication


    if (k==1) then
      if (j==1) then
        write(16,'(i8,3ES24.13E3)') j , one, cf , hf
      else
        write(16,'(i8,3ES24.13E3)') j , w, cf , hf
      endif
    endif
! =======================================================!


! =============== Incidence generation ==================!
    if (ns<=0) then
      sic = 0
      w = rero

    else ! ----------- > total number susceptible in contagious domains
      sic =  0

      do i = 1, ni
        nsap = random_Poisson( v_ran(lb) * real(w) ,.true.)
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
! =======================================================!



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
! =======================================================!



! =================== Cummulative =======================!
  cumvl = cumvl + vl(j)
  cumv(k,j) = cumvl  ! write cumulant vector
  incv(k,j) = dfloat(vl(j))
! =======================================================!



! ================ SEIR evolution =======================!
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
! =======================================================!


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
! ========================================

! =========== > Ommit non-propagated events
  if (j == ntot.and.ns/=ins) then
    lkk = lkk + one
    fl=1
  else if (j>1.and.ns==ins) then
    fl=0
  endif
! ==========================================

enddo !------------- > End of single trajectory calculation

! =============================================================================!

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

! deallocate( vsic, vl, vr, vd, vnl, vns, vni, vnr, vnd, vnp)
lk = lk + one
print*, int(lk), int(lkk)

end do !------------- > End of trajectories calculation
! =============================================================================!



!===================== Averaging over trajectories ============================!
cumvl = ini

if (traj==1) then

  do i=1 , ntot
  cumvl = cumvl + avl(i)

  write(15, '(i8,7ES24.13E3)') i, dfloat(avl(i)), dfloat(avnl(i)), &
                                 dfloat(avns(i)), dfloat(avni(i)),&
                                 dfloat(avnr(i)), dfloat(avnd(i)), &
                                 dfloat(cumvl)
  enddo

else

  do i=1 , ntot

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

end program
