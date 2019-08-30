"""
Partitionned EDF using PartitionedScheduler.
"""
from simso.core.Scheduler import SchedulerInfo
from simso.utils import PartitionedScheduler
from simso.schedulers import scheduler

@scheduler("simso.schedulers.P_RM_MZ")
class P_RM_MZ(PartitionedScheduler):
    def init(self):
        PartitionedScheduler.init(
            self, SchedulerInfo("simso.schedulers.RM_mono"))

    # x(2pow(1/x) - 1) 
    def urm(self, x):
        return x * (2**(1.0/x) - 1)

    def packer(self):
        # First Fit
        cpus = [[cpu, 0] for cpu in self.processors]
        for task in self.task_list:
            j = 0
            x = 0
            # Find the processor with the lowest UTILIZATION.
            for i, c in enumerate(cpus):
                m = c[1] + float(task.wcet) / task.period
                if m < self.urm(x+1):
                    j = i
                    x += 1

            # Affect it to the task.
            self.affect_task_to_processor(task, cpus[j][0])

            # Update utilization.
            cpus[j][1] += float(task.wcet) / task.period
        return True
