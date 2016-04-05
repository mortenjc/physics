
INCLUDE= -I/usr/local/hdf5/include 
LDFLAGS= -L/usr/local/hdf5/lib -lhdf5 -lhdf5_cpp  -lhdf5_hl_cpp 
CFLAGS=


PROG=hdf5test

all:
	g++ $(PROG).cpp $(CFLAGS) $(INCLUDE) $(LDFLAGS) -o $(PROG) 

run: $(PROG)
	./$(PROG)

clean:
	rm -fr $(PROG) SDS.h5
