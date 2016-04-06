
INCLUDE= -I/usr/local/hdf5/include 
LDFLAGS= -L/usr/local/hdf5/lib -lhdf5 -lhdf5_cpp  -lhdf5_hl_cpp 

CFLAGS=

ifdef COV
   CFLAGS+= --coverage
endif

Q=@
ifdef V
Q=
endif


PROGS = hdf5test h5group h5crtgrpar

TMPFILES=SDS.h5 Group.h5


all:
	$(Q)g++ hdf5test.cpp $(CFLAGS) $(INCLUDE) $(LDFLAGS) -o hdf5test 
	$(Q)g++ h5group.cpp $(CFLAGS) $(INCLUDE) $(LDFLAGS) -o h5group
	$(Q)g++ h5crtgrpar.cpp $(CFLAGS) $(INCLUDE) $(LDFLAGS) -o h5crtgrpar

run: $(PROGS)
	$(Q)./hdf5test
	$(Q)./h5group

coverage:
	$(Q)lcov -b . -c -d . > lcov.out
	$(Q)genhtml -o html lcov.out

clean:
	$(Q)rm -fr $(PROGS) $(TMPFILES) *.gcno *.gcda lcov.out *.gcov
