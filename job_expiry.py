class PrintQueueManager:
    def __init__(self):
        self.queue = []
        self.EXPIRY_TIME = 10  # Job expires after 10 ticks
        self.tick_count = 0

    def enqueue_job(self, user_id, job_id, priority):
        job = {
            "user_id": user_id,
            "job_id": job_id,
            "priority": priority,
            "waiting_time": 0
        }
        self.queue.append(job)
        print(f"[ENQUEUED] Job {job_id} by user {user_id} with priority {priority}")

    def tick(self):
        self.tick_count += 1
        print(f"\n=== Tick {self.tick_count} ===")

        # Increase waiting time for all jobs
        for job in self.queue:
            job["waiting_time"] += 1

        # Call your module: remove expired jobs
        self.remove_expired_jobs()

    def remove_expired_jobs(self):
        expired_jobs = []
        new_queue = []

        for job in self.queue:
            if job["waiting_time"] >= self.EXPIRY_TIME:
                expired_jobs.append(job)
                print(f"[EXPIRED] Job {job['job_id']} by user {job['user_id']} expired after {job['waiting_time']} ticks.")
            else:
                new_queue.append(job)

        self.queue = new_queue

    def show_status(self):
        print("\n- Current Queue Status -")
        if not self.queue:
            print("Queue is empty.")
        else:
            for job in self.queue:
                print(f"JobID: {job['job_id']}, User: {job['user_id']}, Priority: {job['priority']}, Waiting: {job['waiting_time']} ticks")


# TESTING

if __name__ == "__main__":
    pq_manager = PrintQueueManager()

    # Enqueue 2 jobs
    pq_manager.enqueue_job("U101", "job001", 3)
    pq_manager.enqueue_job("U102", "job002", 2)

    # Simulate 12 ticks
    for _ in range(12):
        pq_manager.tick()
        pq_manager.show_status()
