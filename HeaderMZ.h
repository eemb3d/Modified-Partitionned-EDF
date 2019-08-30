#ifndef FREE_RTOS_CONFIG_MZ
#define FREE_RTOS_CONFIG_MZ

#define SIZE 10
#define ROW SIZE
#define COL SIZE

unsigned int count_matrix_task_tick_start = 0;
unsigned int count_matrix_task_tick_end = 0;
unsigned int count_tasks_ticks = 0;
unsigned short communication_priority = 0;

static void communication_task(void);
static void matrix_task(void);
static void prioritysettask(void);
static void reciveData(void);
static void printMatrix(double);

xTaskHandle matrix_handle;
xTaskHandle communication_handle;
xTaskHandle prioritysettask_handle;
xTaskHandle recivetask_handle;

#define set_NUM_TASKS_C SIZE

QueueHandle_t xQueue = NULL;

typedef struct MZMessage
{
	int msg_pos_i;
	int msg_pos_j;
	double **msg;
} MZMessage_T;

#endif

