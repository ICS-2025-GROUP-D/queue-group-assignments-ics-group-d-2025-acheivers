class PrintQueueManager:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue_job(self, user_id, job_id, priority):
        if self.size == self.capacity:
            print("[!] Queue is full. Cannot enqueue new job.")
            return False

        job = {
            "user_id": user_id,
            "job_id": job_id,
            "priority": priority,
            "waiting_time": 0
        }

        self.queue[self.rear] = job
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        print(f"[+] Enqueued job {job_id} by user {user_id}.")
        return True

    def dequeue_job(self):
        if self.size == 0:
            print("[!] Queue is empty. Nothing to dequeue.")
            return None

        job = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"[-] Dequeued job {job['job_id']}.")
        return job

    def show_status(self):
        print("\n📄 Current Queue Status:")
        if self.size == 0:
            print("Queue is empty.")
            return

        index = self.front
        for i in range(self.size):
            job = self.queue[index]
            print(f"  • Job ID: {job['job_id']}, User: {job['user_id']}, Priority: {job['priority']}, Waiting Time: {job['waiting_time']}s")
            index = (index + 1) % self.capacity
        print()
