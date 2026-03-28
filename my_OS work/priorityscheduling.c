#include <stdio.h>

struct Process {
    int pid;
    int at;   
    int bt;   
    int pr;   
    int wt;   
    int tat;  
    int ct;   
    int done; 
};

int main() {
    int n;
    printf("Enter number of processes: ");
    scanf("%d", &n);

    struct Process p[n];

    for(int i = 0; i < n; i++) {
        p[i].pid = i + 1;
        printf("Enter AT, BT and Priority for P%d: ", p[i].pid);
        scanf("%d %d %d", &p[i].at, &p[i].bt, &p[i].pr);
        p[i].done = 0;
    }

    int completed = 0, time = 0;

    while(completed < n) {
        int idx = -1;
        int highest_priority = 9999;

        for(int i = 0; i < n; i++) {
            if(p[i].at <= time && p[i].done == 0) {
                if(p[i].pr < highest_priority) {
                    highest_priority = p[i].pr;
                    idx = i;
                }
              
                else if(p[i].pr == highest_priority) {
                    if(p[i].at < p[idx].at) {
                        idx = i;
                    }
                }
            }
        }

        if(idx != -1) {
          
            time += p[idx].bt;
            p[idx].ct = time;
            p[idx].tat = p[idx].ct - p[idx].at;
            p[idx].wt = p[idx].tat - p[idx].bt;
            p[idx].done = 1;
            completed++;
        } else {
            time++; // CPU idle
        }
    }

  
    float total_wt = 0, total_tat = 0;

    printf("\nPID\tAT\tBT\tPR\tCT\tTAT\tWT\n");

    for(int i = 0; i < n; i++) {
        printf("P%d\t%d\t%d\t%d\t%d\t%d\t%d\n",
               p[i].pid, p[i].at, p[i].bt, p[i].pr,
               p[i].ct, p[i].tat, p[i].wt);

        total_wt += p[i].wt;
        total_tat += p[i].tat;
    }

    printf("\nAverage Waiting Time: %.2f", total_wt / n);
    printf("Average Turnaround Time: %.2f\n", total_tat / n);

    return 0;
}

