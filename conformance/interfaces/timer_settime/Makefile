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
subdir=			conformance/interfaces/timer_settime
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
LDLIBS+=		-lpthread -lrt

INSTALL_TARGETS+=	timer_settime_11-1.sh timer_settime_6-1.run-test timer_settime_5-2.run-test timer_settime_8-1.run-test timer_settime_3-2.run-test timer_settime_2-1.run-test timer_settime_1-1.run-test timer_settime_5-3.run-test timer_settime_8-2.run-test timer_settime_9-2.run-test timer_settime_1-2.run-test timer_settime_10-1.sh timer_settime_9-1.run-test timer_settime_13-1.run-test timer_settime_8-3.run-test timer_settime_5-1.run-test timer_settime_4-1.sh timer_settime_8-4.run-test
MAKE_TARGETS+=		timer_settime_11-1.sh timer_settime_6-1.run-test timer_settime_5-2.run-test timer_settime_8-1.run-test timer_settime_3-2.run-test timer_settime_2-1.run-test timer_settime_1-1.run-test timer_settime_5-3.run-test timer_settime_8-2.run-test timer_settime_9-2.run-test timer_settime_1-2.run-test timer_settime_10-1.sh timer_settime_9-1.run-test timer_settime_13-1.run-test timer_settime_8-3.run-test timer_settime_5-1.run-test timer_settime_4-1.sh timer_settime_8-4.run-test

INSTALL_TARGETS+=	timer_settime_3-3.run-test timer_settime_3-1.run-test
MAKE_TARGETS+=		timer_settime_3-3.run-test timer_settime_3-1.run-test

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

timer_settime_6-1.run-test: $(srcdir)/6-1.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/6-1.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/6-1 compile PASSED"; \
		 echo "$(subdir)/6-1 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/6-1 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/6-1 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_5-2.run-test: $(srcdir)/5-2.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/5-2.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/5-2 compile PASSED"; \
		 echo "$(subdir)/5-2 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/5-2 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/5-2 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_8-1.run-test: $(srcdir)/8-1.c
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

timer_settime_3-2.run-test: $(srcdir)/3-2.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/3-2.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/3-2 compile PASSED"; \
		 echo "$(subdir)/3-2 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/3-2 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/3-2 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_2-1.run-test: $(srcdir)/2-1.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/2-1.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/2-1 compile PASSED"; \
		 echo "$(subdir)/2-1 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/2-1 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/2-1 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_1-1.run-test: $(srcdir)/1-1.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/1-1.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/1-1 compile PASSED"; \
		 echo "$(subdir)/1-1 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/1-1 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/1-1 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_5-3.run-test: $(srcdir)/5-3.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/5-3.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/5-3 compile PASSED"; \
		 echo "$(subdir)/5-3 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/5-3 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/5-3 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_8-2.run-test: $(srcdir)/8-2.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/8-2.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/8-2 compile PASSED"; \
		 echo "$(subdir)/8-2 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/8-2 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/8-2 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_9-2.run-test: $(srcdir)/9-2.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/9-2.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/9-2 compile PASSED"; \
		 echo "$(subdir)/9-2 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/9-2 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/9-2 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_1-2.run-test: $(srcdir)/1-2.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/1-2.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/1-2 compile PASSED"; \
		 echo "$(subdir)/1-2 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/1-2 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/1-2 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_9-1.run-test: $(srcdir)/9-1.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/9-1.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/9-1 compile PASSED"; \
		 echo "$(subdir)/9-1 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/9-1 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/9-1 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_13-1.run-test: $(srcdir)/13-1.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/13-1.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/13-1 compile PASSED"; \
		 echo "$(subdir)/13-1 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/13-1 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/13-1 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_8-3.run-test: $(srcdir)/8-3.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/8-3.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/8-3 compile PASSED"; \
		 echo "$(subdir)/8-3 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/8-3 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/8-3 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_5-1.run-test: $(srcdir)/5-1.c
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

timer_settime_8-4.run-test: $(srcdir)/8-4.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/8-4.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/8-4 compile PASSED"; \
		 echo "$(subdir)/8-4 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/8-4 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/8-4 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_11-1.sh: $(srcdir)/11-1.sh
	@cp $(srcdir)/11-1.sh $@

timer_settime_10-1.sh: $(srcdir)/10-1.sh
	@cp $(srcdir)/10-1.sh $@

timer_settime_4-1.sh: $(srcdir)/4-1.sh
	@cp $(srcdir)/4-1.sh $@

timer_settime_3-3.run-test: $(srcdir)/3-3.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/3-3.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/3-3 compile PASSED"; \
		 echo "$(subdir)/3-3 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/3-3 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/3-3 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

timer_settime_3-1.run-test: $(srcdir)/3-1.c
	@if $(CC)  $(CFLAGS) $(LDFLAGS) -o $@ $(srcdir)/3-1.c $(LDLIBS) > logfile.$$$$ 2>&1; then \
		 cat logfile.$$$$; \
		 echo "$(subdir)/3-1 compile PASSED"; \
		 echo "$(subdir)/3-1 compile PASSED" >> $(LOGFILE); \
	else \
		 cat logfile.$$$$; \
		 echo "$(subdir)/3-1 compile FAILED; SKIPPING"; \
		(echo "$(subdir)/3-1 compile FAILED; SKIPPING"; cat logfile.$$$$) >> $(LOGFILE); \
	fi; \
	rm -f logfile.$$$$

