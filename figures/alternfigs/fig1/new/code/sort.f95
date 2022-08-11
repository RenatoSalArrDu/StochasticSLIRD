module sorts

  implicit none
  private
  public :: quicksort

  contains

recursive subroutine quicksort(a, first, last)
  use my_init
  implicit none

  real(wp), intent(inout) ::  a(last)
  real(wp) :: x, t
  integer, intent(in) :: first, last
  integer i, j

  x = a( (first+last) / 2 )
  i = first
  j = last
  do
     do while (a(i) < x)
        i = i + 1
     end do
     do while (x < a(j))
        j = j - 1
     end do
     if (i >= j) exit
     t = a(i);  a(i) = a(j);  a(j) = t
     i=i+1
     j=j-1
  end do
  if (first < i-1) call quicksort(a, first, i-1)
  if (j+1 < last)  call quicksort(a, j+1, last)

end subroutine quicksort

end module
