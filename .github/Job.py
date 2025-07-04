class Job:
    def __init__(self, job_id, user_id, priority, waiting_time):
        self.job_id = job_id
        self.user_id = user_id
        self.priority = priority
        self.waiting_time = waiting_time

class QueueVisualizer:
    def __init__(self, queue):
        self.queue = queue  # Assume queue is a list or custom object with a list inside

    def display_queue_state(self, event_name=""):
        print("\n=== Queue State ===")
        if event_name:
            print(f"Event: {event_name}")
        if not self.queue:
            print("Queue is empty.")
            return
        print(f"{'JobID':<10}{'UserID':<10}{'Priority':<10}{'WaitingTime':<15}")
        print("-" * 45)
        for job in self.queue:
            print(f"{job.job_id:<10}{job.user_id:<10}{job.priority:<10}{job.waiting_time:<15}")
        print("===================\n")

    def notify_expired_job(self, job):
        print(f"⚠️  Job {job.job_id} (User: {job.user_id}) has expired and was removed from the queue.")

    def notify_enqueue(self, job):
        print(f"✅ New job added: {job.job_id} (User: {job.user_id}, Priority: {job.priority})")

    def notify_dequeue(self, job):
        print(f"⬅️  Job processed: {job.job_id} (User: {job.user_id}) removed from queue.")

