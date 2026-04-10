#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

#define MAX 20   // maximum philosophers

HANDLE mutex;
HANDLE S[MAX];

int state[MAX];
int N;   // number of philosophers (user input)

#define THINKING 0
#define HUNGRY 1
#define EATING 2

int left(int i) { return (i + N - 1) % N; }
int right(int i) { return (i + 1) % N; }

void test(int i) {
    if (state[i] == HUNGRY &&
        state[left(i)] != EATING &&
        state[right(i)] != EATING) {

        state[i] = EATING;
        printf("Philosopher %d is Eating\n", i);

        ReleaseSemaphore(S[i], 1, NULL);
    }
}

void take_forks(int i) {
    WaitForSingleObject(mutex, INFINITE);

    state[i] = HUNGRY;
    printf("Philosopher %d is Hungry\n", i);

    test(i);
    ReleaseMutex(mutex);

    WaitForSingleObject(S[i], INFINITE);
}

void put_forks(int i) {
    WaitForSingleObject(mutex, INFINITE);

    state[i] = THINKING;
    printf("Philosopher %d is Thinking\n", i);

    test(left(i));
    test(right(i));

    ReleaseMutex(mutex);
}

DWORD WINAPI philosopher(LPVOID num) {
    int i = *(int *)num;

    while (1) {
        Sleep(1000);  // thinking
        take_forks(i);
        Sleep(2000);  // eating
        put_forks(i);
    }
}

int main() {
    int i;
    HANDLE thread_id[MAX];
    int phil[MAX];

    printf("Enter number of philosophers (max %d): ", MAX);
    scanf("%d", &N);

    if (N <= 0 || N > MAX) {
        printf("Invalid number!\n");
        return 0;
    }

    mutex = CreateMutex(NULL, FALSE, NULL);

    for (i = 0; i < N; i++)
        S[i] = CreateSemaphore(NULL, 0, 1, NULL);

    for (i = 0; i < N; i++) {
        phil[i] = i;
        thread_id[i] = CreateThread(NULL, 0, philosopher, &phil[i], 0, NULL);
    }

    WaitForMultipleObjects(N, thread_id, TRUE, INFINITE);

    return 0;
}