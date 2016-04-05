
INCLUDE= -I/usr/local/hdf5/include 
LDFLAGS= -L/usr/local/hdf5/lib -lhdf5 -lhdf5_cpp  -lhdf5_hl_cpp 
CFLAGS=

PROGS = hdf5test h5group

TMPFILES=SDS.h5 Group.h5


all:
	g++ hdf5test.cpp $(CFLAGS) $(INCLUDE) $(LDFLAGS) -o hdf5test 
	g++ h5group.cpp $(CFLAGS) $(INCLUDE) $(LDFLAGS) -o h5group

run: $(PROGS)
	./hdf5test
	./h5group

clean:
	rm -fr $(PROGS) $(TMPFILES) 
