#!/usr/bin/env python

'''
Different TILE platforms have different num of cpu cores,
e.g TILEmpower-GX/TILExtreme-GX/TILExtreme-GX-DUO, and thus 
it's hard to provide one fixed header file with fixed array
declaration.

This file will run on each make, to generate the header
file suitable for the num of CPUs. It will detech the num
of CPUs, and then fill in the array according to the num.
Generate the header file dynamically.
'''


import os

# The fixed part of the header file

TOP = '''
# ifndef PITEST_CONFIG_H
# define PITEST_CONFIG_H

// for sysconf
#include <unistd.h>

struct thread_param {
	int index;
	volatile int stop;
	int sleep_ms;
	int priority;
	int policy;
	const char *name;
	int cpu;
	volatile unsigned futex;
	volatile unsigned should_stall;
	volatile unsigned progress;
};

'''

BOTTOM = '''
#endif
'''


def cpu_count():
	'Return the #CPUs in the system'
	try:
		num = os.sysconf('SC_NPROCESSORS_ONLN')
	except (ValueError, OSError, AttributeError):
		num = 0
	return num


def _cpus(fp, num):
	print >> fp, "int cpus = %d;" % num 

def _top(fp):
	'Generate the top part of the header file'
	print >> fp, TOP

def _bottom(fp):
	'Generate the bottom part of the header file'
	print >> fp, BOTTOM


def _fill_common(filename, seq, array_start, fillin, num):
	'''
	Fill in the header with the provided content
	@filename	The header
	@seq		The header seq, e.g it's 6 for testcase 6
	@array_start	The start part of the array defination
	@fillin		The dynamatically generated part on #CPUs
	@num		#CPUs
	'''

	HEADER = '''
#ifndef PITEST_CONFIG_%d_H
#define PITEST_CONFIG_%d_H

#include "pitest_config.h"
'''

	with open(filename, 'a+') as fp:
		fp.truncate(0)
		print "Generating header file: %s" % filename
		print >> fp, HEADER % (seq, seq)
		print >> fp, array_start,
		for i in range(0, num-1):
			print >> fp, '\t',
			print >> fp, fillin[i]
		print >> fp, '};'
		print >> fp, '#endif'


def _fill_pitest_1(prefix, num):
	'Fill in the TF control lines for pi_test-1'
	
	PITEST = '''
static struct thread_param tp[] = {
	{0, 0, 0, 1, SCHED_FIFO, "TL", 0, 0, 0, 0}, 
	{1, 0, 50, 2, SCHED_FIFO, "TP", 0, 0, 0, 0}, 
'''
	
	fillin = []
	for i in range(1, num):
		fillin.append(
			'{%d, 0, 0, 3, SCHED_FIFO, "TF", %d, 0, 0, 0},' % (i+1, i))

	header = prefix + '_1.h'
	_fill_common(header, 1, PITEST, fillin, num)


def _fill_pitest_2(prefix, num):
	'Fill in the TF control lines for pi_test-2'
	
	PITEST = '''
static struct thread_param tp[] = {
	{0, 0, 0, 1, SCHED_FIFO, "TL", 0, 0, 0, 0}, 
	{1, 0, 100, 2, SCHED_FIFO, "TP1", 0, 0, 0, 0}, 
	{2, 0, 100, 5, SCHED_FIFO, "TP2", 0, 0, 0, 0}, 
'''
	
	fillin = []
	for i in range(1, num):
		fillin.append(
			'{%d, 0, 0, 3, SCHED_FIFO, "TF", %d, 0, 0, 0},' % (i+2, i))

	header = prefix + '_2.h'
	_fill_common(header, 2, PITEST, fillin, num)


def _fill_pitest_3(prefix, num):
	'Fill in the TF control lines for pi_test-3'

	PITEST = '''
static struct thread_param tp[] = {
	{0, 0, 0, 1, SCHED_FIFO, "TL", 0, 0, 0, 0}, 
	{1, 0, 100, 2, SCHED_FIFO, "TP1", 0, 0, 0, 0}, 
	{1, 0, 100, 5, SCHED_FIFO, "TP2", 0, 0, 0, 0}, 
'''
	
	fillin = []
	for i in range(1, num):
		fillin.append(
			'{%d, 0, 0, 3, SCHED_FIFO, "TF", %d, 0, 0, 0},' % (i+1, i))

	header = prefix + '_3.h'
	_fill_common(header, 3, PITEST, fillin, num)


def _fill_pitest_4(prefix, num):
	'Fill in the TF control lines for pi_test-4'
	
	PITEST = '''
static struct thread_param tp[] = {
	{0, 0, 0, 1, SCHED_FIFO, "TL", 0, 0, 0, 0}, 
	{1, 0, 100, 4, SCHED_FIFO, "TP", 0, 0, 0, 0},
'''
	
	fillin = []
	for i in range(1, num):
		fillin.append(
			'{%d, 0, 0, 2, SCHED_FIFO, "TF", %d, 0, 0, 0},' % (i+1, i))

	header = prefix + '_4.h'
	_fill_common(header, 4, PITEST, fillin, num)


def _fill_pitest_5(prefix, num):
	'Fill in the TF control lines for pi_test-5'

	PITEST = '''
static struct thread_param tp[] = {
	{0, 0, 0, 1, SCHED_FIFO, "TL", 0, 0, 0, 0}, 
	{1, 0, 200, 2, SCHED_FIFO, "TP", 0, 0, 0, 0}, 
'''
	
	fillin = []
	for i in range(1, num):
		fillin.append(
			'{%d, 0, 0, 3, SCHED_FIFO, "TF", %d, 0, 0, 0},' % (i+1, i))

	header = prefix + '_5.h'
	_fill_common(header, 5, PITEST, fillin, num)


def _fill_pitest_6(prefix, num):
	'Fill in the TF control lines for pi_test-6'

	PITEST = '''
static struct thread_param tp[] = {
	{0, 0, 0, 1, SCHED_FIFO, "TL", 0, 0, 0, 0}, 
	{1, 0, 200, 2, SCHED_FIFO, "TP", 0, 0, 0, 0}, 
'''
	
	fillin = []
	for i in range(1, num):
		fillin.append(
			'{%d, 0, 0, 3, SCHED_FIFO, "TF", %d, 0, 0, 0},' % (i+1, i))

	header = prefix + '_6.h'
	_fill_common(header, 6, PITEST, fillin, num)


def _fill(prefix, num):
	'''
	Fill in the TF control lines for #CPUs.
	Different tests have different declaration of array.
	'''
	_fill_pitest_1(prefix, num)
 	_fill_pitest_2(prefix, num)
	_fill_pitest_3(prefix, num)
	_fill_pitest_4(prefix, num)
	_fill_pitest_5(prefix, num)
	_fill_pitest_6(prefix, num)


def generate_headers(filename):
	'''
	Generate the approriate header file.
	
	It take the following steps:
		1. Truncate the file to 0 size if any.
		   Drop the old content.
		2. Get the #CPUs
		3. Make up the top part
		4. Make up the 'cpus' setup  
		5. Make up the bottom part
		6. Make up the testcases specific headers 
	'''

	header = filename + '.h'
	with open(header, 'a+') as fp:
		print header 
		fp.truncate(0)	# truncate the old content if any
		num = cpu_count()
		_top(fp)
		_cpus(fp, num)
		_bottom(fp)

	# generate separate header files for each testcase
	_fill(filename, num)


if __name__ == '__main__':
	generate_headers("pitest_config")

