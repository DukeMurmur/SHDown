print('Requires a root acsess!')
import sys

def shutdown():
    current_os = platform.system()

    if current_os == 'Windows':
        shutdown_sys(1)

    if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
        shutdown_sys(0)

def shutdown_sys(ind):
	import subprocess
	if ind == 0:
		subprocess.call('halt')
	if ind == 1:
		subprocess.call('cmd /c shutdown.exe /s -t 0')
import time
def shutdown_time():
	global cut_off
	cut_off = input('Enter time in a valid format, e.g. 20:30 (in 24hours format!)\nThe programm will shutdown the computer when given time will appear: ')
	if ':' not in cut_off:
		print('Invalid time')
		return 0
	cut_off = cut_off.split(':')
	for item in cut_off:
		try:
			item = int(item)
		except:
			print('Invalid time')
			return 0
	if 23 >= int(cut_off[0]) >= 0:
		if 60 >= int(cut_off[1]) >= 0:
			None
		else:
			return 0
	else:
		return 0
	return 1
while shutdown_time() != 1:
	None
print('Timer has been set. If you want to stop it - simply close timer window')
print('')
current_time = time.localtime()
while current_time.tm_hour != int(cut_off[0]) or current_time.tm_min != int(cut_off[1]):
	current_time = time.localtime()
	time.sleep(1)
	hour_dif = int(cut_off[0]) - current_time.tm_hour
	min_dif = int(cut_off[1]) - current_time.tm_min
	if hour_dif < 0:
		hour_dif = 24 + hour_dif
	if min_dif < 0:
		min_dif = 60 + min_dif
		if hour_dif != 0:
			hour_dif = hour_dif - 1
	if hour_dif == 0:
		if current_time.tm_min > int(cut_off[1]):
			if current_time.tm_hour == int(cut_off[1]):
				hour_dif = 23
	if min_dif == 0:
		hour_dif = hour_dif - 1
		min_dif = 59
	else:
		min_dif = min_dif - 1
	sec_dif = 60 - current_time.tm_sec - 1
	output = 'Time left before shutdown: ' + str(hour_dif) + ' hours ' + str(min_dif) + ' minutes ' + str(sec_dif) + ' seconds     '
	if hour_dif <= 0 or min_dif <= 0 or sec_dif <= 0:
		sys.stdout.write(output)
		sys.stdout.write('\r')
		sys.stdout.flush()
	else:
		output = 'Time left before shutdown: 0 hours 0 minutes 0 seconds      '
		sys.stdout.write(output)
		sys.stdout.write('\r')
		sys.stdout.flush()
		print('')
		print('Shutting down now...')
shutdown()
time.sleep(5)
sys.stdout.write('\r')
sys.stdout.flush()
print('\n')
print('Failed to shutdown')
print('Check the root access')
time.sleep(3)
