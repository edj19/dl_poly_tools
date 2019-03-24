program Config_analysis
	implicit none
	integer, parameter :: mxatms=100000
	integer,parameter:: in=8
	integer i,n,levcfg,imcon,natms
	character*8 aname
	character*80  text
	real*8 cell,xxx,yyy,zzz
	character*40 FNAME

	character*8 name(mxatms)
	dimension cell(9)
	dimension xxx(mxatms),yyy(mxatms),zzz(mxatms)

	write(*,*)'Enter name of FIELD file'
    read(*,*)FNAME

	open(in,file=FNAME)
	open(12,file="results.txt")
	read(in,'(a80)')text
	write(*,*)text
	read(in,'(2i10)')levcfg,imcon
	if(imcon.gt.0)then
	 read(in,'(3f20.12)')cell(1),cell(2),cell(3)
	 read(in,'(3f20.12)')cell(4),cell(5),cell(6)
	 read(in,'(3f20.12)')cell(7),cell(8),cell(9)
	endif
	do i=1,mxatms
	 read(in,'(a8,i10)',end=300)aname,n
	 if(n.eq.0)n=i
	 name(n)=aname
	 read(in,'(3f20.12)')xxx(n),yyy(n),zzz(n)
	 write(12,'(3f20.12)')xxx(n),yyy(n),zzz(n)
	 if(levcfg.gt.0)read(in,*)
	 if(levcfg.gt.1)read(in,*)
	enddo
	300  continue
	natms=i-1
	write(*,*)'atoms in CONFIG file = ',natms
	close(in)


end program Config_analysis
