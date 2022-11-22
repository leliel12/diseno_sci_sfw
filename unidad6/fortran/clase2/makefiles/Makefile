# compiler
FC = gfortran

# compiler flags
# standard
CFLAGS = -std=f2008ts
# warning flags
CFLAGS += -Wall
# debugging options
CFLAGS += -fPIC -fcheck=all -fbacktrace -fmax-errors=3
# GDB flag
CFLAGS += -g

# lib flags
# LFLAGS = -pthread -I/usr/lib/x86_64-linux-gnu/openmpi/lib -L/usr/lib/x86_64-linux-gnu/openmpi/lib -lmpi_usempif08 -lmpi_usempi_ignore_tkr -lmpi_mpifh -lmpi

# source files
SRCS = mod_1 main
OBJS = $(SRCS:=.o)

# executable
MAIN = main

# compile project
all : $(MAIN)
	@echo Ya compiló todo

$(MAIN)	: $(OBJS)
	@echo Compilando ejecutable
	$(FC) $(CFLAGS) -o $(MAIN) $(OBJS) $(LFLAGS)

.SUFFIXES : .o .f90

.f90.o :
	@echo Compilando $< 
	$(FC) $(CFLAGS) $(LFLAGS) -c $<

clean :
	$(RM) *.o *.so *.mod $(MAIN)
