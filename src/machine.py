import logging

class Machine:
    def __init__(self, name, os_name, cpu, memory, disk):
        self.name = name
        self.os = os_name
        self.cpu = cpu
        self.memory = memory
        self.disk = disk
        logging.info("Machine created: %s (os=%s, cpu=%s, mem=%s, disk=%s)",
                     self.name, self.os, self.cpu, self.memory, self.disk)

    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "memory": self.memory,
            "disk": self.disk
        }
