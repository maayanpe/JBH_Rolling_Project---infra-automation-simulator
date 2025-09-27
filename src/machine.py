# src/machine.py
import logging

class Machine:
    def __init__(self, name, address, os_name, cpu, memory, disk):
        self.name = name
        self.address = address
        self.os = os_name
        self.cpu = cpu
        self.memory = memory
        self.disk = disk
        logging.info("Machine created: %s (addr=%s, os=%s, cpu=%s, mem=%s, disk=%s)",
                     self.name, self.address, self.os, self.cpu, self.memory, self.disk)

    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "os": self.os,
            "cpu": self.cpu,
            "memory": self.memory,
            "disk": self.disk
        }

