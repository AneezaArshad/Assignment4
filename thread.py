burst_time = []
wait = []
turn_around = []
average_wait_time = 0
average_turn_around = 0

print "Enter number of Processes:"

number = input()

print "Enter Processes Burst Time: \n"

for x in range(number):
	print "for P [" , (x+1) , "] = "
	burst_time.append(input())


wait.append(0)

for x in range(1 ,number):
	wait.append(0)
	for y in range(0,x):
		wait[x] = wait[x] + burst_time[y]


print "\nProcess \tBurst Time\tWaiting Time\tturn_around Time"

for x in range(number):
	turn_around.append(burst_time[x] + wait[x])
	average_wait_time = average_wait_time + wait[x]
	average_turn_around = average_turn_around + turn_around[x]
	print "\nP[",(x+1),"]\t\t",burst_time[x],"\t\t",wait[x],"\t\t",turn_around[x]



average_wait_time = average_wait_time / number
average_turn_around = average_turn_around / number

print "\n Average Waiting Time : " , average_wait_time
print "\n Average Turn Around Time : " , average_turn_around



