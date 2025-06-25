class PrintQueueManager:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = self.size = 0

    def enqueue_job(self, user_id, job_id, priority):
        if self.size >= self.capacity:
            print("[!] Queue full: Cannot add job.")
            return False

        self.queue[self.rear] = {
            "user_id": user_id,
            "job_id": job_id,
            "priority": priority,
            "waiting_time": 0
        }

        print(f"[✔] Job {job_id} added by user {user_id}.")
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def dequeue_job(self):
        if self.size == 0:
            print("[!] Queue empty: No job to remove.")
            return None

        removed_job = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"[✖] Removed job {removed_job['job_id']}.")
        return removed_job

    def show_status(self):
        print("\n📋 Print Queue Overview:")
        if self.size == 0:
            print("-> Queue is currently empty.")
            return

        idx = self.front
        for count in range(self.size):
            job = self.queue[idx]
            print(f" • Job ID: {job['job_id']} | User: {job['user_id']} | Priority: {job['priority']} | Wait: {job['waiting_time']}s")
            idx = (idx + 1) % self.capacity
        print()
