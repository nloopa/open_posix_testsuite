#
# Automatically generated by generate-makefiles.sh -- DO NOT EDIT.
#
# Restrictions for generate-makefiles.sh apply to this file. See COPYING for
# more details.
#
# Garrett Cooper, June 2010
#

# Path variables.
top_srcdir?=		../../..
subdir=			conformance/interfaces/mlock
srcdir=			$(top_srcdir)/$(subdir)

prefix?=		/opt/openposix_testsuite
exec_prefix?=		$(prefix)
INSTALL_DIR=		$(DESTDIR)/$(exec_prefix)/$(subdir)
LOGFILE?=		logfile

# Build variables
CFLAGS+=		-I$(top_srcdir)/include

# XXX: for testfrmw.c -- needs to be moved into a library.
CFLAGS+=		-I$(srcdir)

# Top-level make definitions
CFLAGS+=		-std=c99 -D_POSIX_C_SOURCE=200112L -D_XOPEN_SOURCE=600 -W -Wall
LDFLAGS+=		
LDLIBS+=		
# Submake make definitions.
CFLAGS+=		
LDFLAGS+=		
LDLIBS+=		

INSTALL_TARGETS+=	mlock_8-1.run-test mlock_10-1.run-test mlock_5-1.run-test mlock_4-1.sh mlock_7-1.sh mlock_12-1.run-test
MAKE_TARGETS+=		mlock_8-1.run-test mlock_10-1.run-test mlock_5-1.run-test mlock_4-1.sh mlock_7-1.sh mlock_12-1.run-test

INSTALL_TARGETS+=	mlock_2-1.sh
MAKE_TARGETS+=		mlock_2-1.sh

all: $(MAKE_TARGETS)
	@if [ -d speculative ]; then $(MAKE) -C speculative all; fi

clean:
	rm -f $(MAKE_TARGETS) logfile* run.sh *.core
	@if [ -d speculative ]; then $(MAKE) -C speculative clean; fi

install: $(INSTALL_DIR) run.sh
	set -e; for file in $(INSTALL_TARGETS) run.sh; do	\
		if [ -f "$$file" ] ; then			\
			install -m 00755 $$file		\
				$(INSTALL_DIR)/$$file;	\
		fi;						\
	done
	@if [ -d speculative ]; then $(MAKE) -C speculative install; fi

test: run.sh
	@./run.sh

$(INSTALL_DIR):
	mkdir -p $@

run.sh:
	@echo '#/bin/sh' > $@
	@echo "$(top_srcdir)/bin/run-tests.sh $(subdir) $(INSTALL_TARGETS)" >> $@
	@chmod +x run.sh

mlock_8-1.run-test: $(srcdir)/8-1.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/8-1.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/8-1 compile PASSED"; \
		 echo "$(subdir)/8-1 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/8-1 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/8-1 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

mlock_10-1.run-test: $(srcdir)/10-1.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/10-1.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/10-1 compile PASSED"; \
		 echo "$(subdir)/10-1 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/10-1 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/10-1 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

mlock_5-1.run-test: $(srcdir)/5-1.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/5-1.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/5-1 compile PASSED"; \
		 echo "$(subdir)/5-1 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/5-1 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/5-1 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

mlock_12-1.run-test: $(srcdir)/12-1.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/12-1.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/12-1 compile PASSED"; \
		 echo "$(subdir)/12-1 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/12-1 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/12-1 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

mlock_4-1.sh: $(srcdir)/4-1.sh
	@cp $(srcdir)/4-1.sh $@

mlock_7-1.sh: $(srcdir)/7-1.sh
	@cp $(srcdir)/7-1.sh $@

mlock_2-1.sh: $(srcdir)/2-1.sh
	@cp $(srcdir)/2-1.sh $@

