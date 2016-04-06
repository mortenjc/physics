
CFLAGS= -I/usr/local/hdf5/include 
LDFLAGS= -L/usr/local/hdf5/lib -lhdf5 -lhdf5_cpp  -lhdf5_hl_cpp 

ifdef COV
   CFLAGS+= --coverage
endif

Q=@
ifdef V
Q=
endif


PROGS= hdf5test h5group h5crtgrpar

TMPFILES=SDS.h5 Group.h5

all: $(PROGS)
	echo done

h5group: src/h5group.cpp
	$(Q)g++ $< $(CFLAGS) $(LDFLAGS) -o $@

hdf5test: src/hdf5test.cpp
	$(Q)g++ $< $(CFLAGS) $(LDFLAGS) -o $@

h5crtgrpar: src/h5crtgrpar.cpp
	$(Q)g++ $< $(CFLAGS) $(LDFLAGS) -o $@


run: $(PROGS)
	$(Q)./hdf5test
	$(Q)./h5group

coverage:
	$(Q)lcov -b . -c -d . > lcov.out
	$(Q)genhtml -o html lcov.out

clean:
	$(Q)rm -fr $(PROGS) $(TMPFILES) *.gcno *.gcda lcov.out *.gcov
