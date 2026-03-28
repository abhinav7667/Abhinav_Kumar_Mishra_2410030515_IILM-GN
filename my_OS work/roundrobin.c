#include <stdio.h>
int main() {
    int n, tq;
    
    printf("Enter number of processes: ");
    scanf("%d", &n);

    int bt[n], rem_bt[n], wt[n], tat[n];
    
    printf("Enter burst times:\n");
    for(int i = 0; i < n; i++) {
        printf("P%d: ", i + 1);
        scanf("%d", &bt[i]);
        rem_bt[i] = bt[i]; 
    }

    printf("Enter time quantum: ");
    scanf("%d", &tq);

    int time = 0;

    while(1) {
        int done = 1;

        for(int i = 0; i < n; i++) {
            if(rem_bt[i] > 0) {
                done = 0;

                if(rem_bt[i] > tq) {
                    time += tq;
                    rem_bt[i] -= tq;
                } else {
                    time += rem_bt[i];
                    wt[i] = time - bt[i]; 
                    rem_bt[i] = 0;
                }
            }
        }

        if(done == 1)
            break;
    }

    for(int i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];
    }

    float total_wt = 0, total_tat = 0;

    printf("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time\n");

    for(int i = 0; i < n; i++) {
        printf("P%d\t%d\t\t%d\t\t%d\n", i + 1, bt[i], wt[i], tat[i]);
        total_wt += wt[i];
        total_tat += tat[i];
    }

    printf("\nAverage Waiting Time: %.2f", total_wt / n);
    printf("\nAverage Turnaround Time: %.2f\n", total_tat / n);

    return 0;
}