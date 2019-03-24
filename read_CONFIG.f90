!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!  Aim to read from CONFIG
! 			created by karl				
!		modified date: 2015-03-12
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Program read_CONFIG
   implicit none

	integer,  parameter   ::  dp    	=  kind(1.0d0) 	! suitable to other OS 
	integer,  parameter   ::  inport 	= 81    		! read port
	integer,  parameter   ::  outport 	= 82    		! read port

	integer  :: levcfg, imcon, megatm, ii, jj
	real(dp) :: lbox, aaa(3), bbb(3), ccc(3)
	real(dp) :: area
	real(dp), dimension(:,:), pointer  ::  ppp, vvv, fff
	integer,  dimension(:),   pointer  ::  atom_index
	character(len=8), dimension(:), pointer :: atom_name
	character(len=72)  	:: header_line
	character(len=132) 	:: file_in, file_out,check_out, buff_line
	logical :: file_exists

	file_in    	=  "CONFIG"				!  file needed to compute   
	file_out   	=  "CONFIG_OUTPUT"		!  file after computing

		
!!================	check if the CONFIG file is exists  

   inquire(file = file_in, exist = file_exists)
   if (.not. file_exists) then
        Write(*,*) ' '
        Write(*,*) 'The input file ', file_in(1:len_trim(file_in))
		Write(*,*) ' does not exist!!!'
        Write(*,*) 'The program stops now - Please check your file .... !!!'
        Write(*,*) ' '
        stop
   else
		write(*,*) ' '
        Write(*,*) 'Start processing the file: ', file_in(1:len_trim(file_in))
   end if 

!!================	start read the CONFIG from the first line   

   open(inport, file = file_in, status = 'old', form = 'formatted')
   read(inport,'(a132)') buff_line
   header_line = buff_line(1:min(len_trim(buff_line),len(header_line)))
   read(inport,'(a132)') buff_line
   read(buff_line,*) levcfg, imcon, megatm

!================	allocate the arrays used for a CONFIG file 

   allocate(ppp(megatm,3))			! position 
   allocate(vvv(megatm,3))			! velocity 
   allocate(fff(megatm,3)) 			! force 
   allocate(atom_index(megatm))		! index
   allocate(atom_name(megatm))		! name in a atom_name(ii)

!!================ box size: aaa bbb ccc  

   read(inport,'(a132)') buff_line
   read(buff_line,*) (aaa(jj), jj = 1, 3)
   read(inport,'(a132)') buff_line
   read(buff_line,*) (bbb(jj), jj = 1, 3)
   read(inport,'(a132)') buff_line
   read(buff_line,*) (ccc(jj), jj = 1, 3)

!!================	details of the atoms: ppp vvv fff

   do ii = 1, megatm
      read(inport,'(a132)') buff_line
      read(buff_line,'(a8, i10)') atom_name(ii), atom_index(ii)
      read(inport,'(a132)') buff_line
      read(buff_line,'(3g20.10)') (ppp(ii,jj), jj = 1, 3)
      if (levcfg > 0) read(inport,'(a132)') buff_line
      if (levcfg > 0) read(buff_line,'(3g20.10)') (vvv(ii,jj), jj = 1, 3)  
      if (levcfg > 1) read(inport,'(a132)') buff_line
      if (levcfg > 1) read(buff_line,'(3g20.10)') (fff(ii,jj), jj = 1, 3)
   end do
   close(inport)

!!================	write out the file

   open(outport, file= file_out, status='unknown', form='formatted')
   write(outport,'(a72)') header_line
   write(outport,'(3I10)') levcfg, imcon, megatm
   write(outport,'(3f20.10,a12,a1)') (aaa(jj), jj = 1, 3)
   write(outport,'(3f20.10,a12,a1)') (bbb(jj), jj = 1, 3)
   write(outport,'(3f20.10,a12,a1)') (ccc(jj), jj = 1, 3)
   do ii = 1, megatm
      write(outport,'(a8, i10)') atom_name(ii), atom_index(ii)
      write(outport,'(3g20.10)') (ppp(ii,jj), jj = 1,3)
      if (levcfg > 0) write(outport,'(3g20.10)') (vvv(ii,jj), jj = 1,3)
      if (levcfg > 1) write(outport,'(3g20.10)') (fff(ii,jj), jj = 1,3)
   end do
   close(outport)

	Write(*,*) 'Done! Output the file: ', file_out(1:len_trim(file_out))
	write(*,*) ' '

!================  deallocate the arrays used for a CONFIG file         

   deallocate(ppp)
   deallocate(vvv)
   deallocate(fff)
   deallocate(atom_index)
   deallocate(atom_name)

!================  

End Program read_CONFIG

