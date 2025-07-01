class PrintQueueManager:
    def __init__(self, max_jobs=10):
        self.max_jobs = max_jobs
        self.jobs = [None] * max_jobs
        self.start = self.end = self.count = 0

    def enqueue_job(self, user, job, priority):
        if self.count >= self.max_jobs:
            print("[!] Queue full: Cannot add job.")
            return False

        new_job = {
            "user_id": user,
            "job_id": job,
            "priority": priority,
            "waiting_time": 0
        }
        self.jobs[self.end] = new_job
        print(f"[✔] Job {job} added by user {user}.")
        self.end = (self.end + 1) % self.max_jobs
        self.count += 1
        return True

    def dequeue_job(self):
        if self.count == 0:
            print("[!] Queue empty: No job to remove.")
            return None

        job_to_remove = self.jobs[self.start]
        self.jobs[self.start] = None
        self.start = (self.start + 1) % self.max_jobs
        self.count -= 1
        print(f"[✖] Removed job {job_to_remove['job_id']}.")
        return job_to_remove

    def show_status(self):
        print("\n📋 Print Queue Overview:")
        if self.count == 0:
            print("-> Queue is currently empty.")
            return

        position = self.start
        for _ in range(self.count):
            job = self.jobs[position]
            print(f" • Job ID: {job['job_id']} | User: {job['user_id']} | Priority: {job['priority']} | Wait: {job['waiting_time']}s")
            position = (position + 1) % self.max_jobs
        print()
