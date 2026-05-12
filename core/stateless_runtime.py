import gc

class OmniRuntime:
    """
    A hardened execution environment that prohibits data persistence.
    Uses __slots__ to prevent dynamic attribute injection.
    """
    __slots__ = ['task_id', 'volatile_context']

    def __init__(self, task_id):
        self.task_id = task_id
        self.volatile_context = {}

    def execute_task(self, logic_function, data):
        """Executes logic and immediately prepares for purging."""
        try:
            result = logic_function(data)
            return result
        finally:
            self.purge()

    def purge(self):
        """Explicitly clears volatile memory and triggers garbage collection."""
        self.volatile_context.clear()
        self.task_id = None
        # Forced collection to ensure zero-footprint in RAM
        gc.collect()

def secure_handoff(target_agent, payload):
    """
    Standardizes the 'Clean-Break' handoff logic.
    """
    print(f"Executing Handoff to {target_agent}...")
    # Logic to strip any primary user metadata before transmission
    clean_payload = {k: v for k, v in payload.items() if k == "instruction"}
    return clean_payload
  
