from PrintQueueManager import PrintQueueManager

# Create a queue with capacity 5
pq = PrintQueueManager(capacity=5)

# Add a few jobs
pq.enqueue_job("user1", "job001", 2)
pq.enqueue_job("user2", "job002", 1)

# Show current queue status
pq.show_status()

# Remove a job
pq.dequeue_job()

# Add another job
pq.enqueue_job("user3", "job003", 3)

# Final queue status
pq.show_status()
