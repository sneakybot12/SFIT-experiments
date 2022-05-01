#include <stdio.h>
int main()
{
    int fragments[10], blocks[10], process[10];
    int m, n, number_of_blocks, number_of_processes, temp, top = 0;
    static int block_arr[10], process_arr[10];
    printf("\nEnter the Total Number of Blocks:\t");
    scanf("%d", &number_of_blocks);

    printf("Enter the Total Number of processes:\t");
    scanf("%d", &number_of_processes);
    printf("\nEnter the Size of the Blocks:\n");
    for (m = 0; m < number_of_blocks; m++)
    {
        printf("Block No.[%d]:\t", m + 1);
        scanf("%d", &blocks[m]);
    }
    printf("Enter the Size of the processes:\n");
    for (m = 0; m < number_of_processes; m++)
    {
        printf("Process No.[%d]:\t", m + 1);
        scanf("%d", &process[m]);
    }
    for (m = 0; m < number_of_processes; m++)
    {
        for (n = 0; n < number_of_blocks; n++)
        {
            if (block_arr[n] != 1)
            {
                temp = blocks[n] - process[m];
                if (temp >= 0)
                {
                    if (top < temp)
                    {
                        process_arr[m] = n;
                        top = temp;
                    }
                }
            }
            fragments[m] = top;

            block_arr[process_arr[m]] = 1;
            top = 0;
        }
    }
printf("\nProcess Number\tAllocated Block Number\tAllocated Block Size\tFragment");
for(m = 0; m < number_of_processes; m++)
{
        printf("\n%d\t\t\t%d\t\t\t%d\t\t%d", m, process_arr[m], blocks[process_arr[m]],
               fragments[m]);
}
printf("\n");
return 0;
}