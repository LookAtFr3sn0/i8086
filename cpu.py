from memory import Memory 

class CPU:
    def __init__(self):
        # General purpose registers
        self.AX = 0 # Primary Accumulator
        self.BX = 0 # Base register
        self.CX = 0 # Counter register
        self.DX = 0 # Extended Accumulator

        # Index registers
        self.SI = 0 # Source Index
        self.DI = 0 # Destination Index
        self.BP = 0 # Base Pointer
        self.SP = 0 # Stack Pointer

        # Program counter
        self.IP = 0 # Instruction Pointer

        # Segment registers
        self.CS = 0 # Code Segment
        self.DS = 0 # Data Segment
        self.ES = 0 # Extra Segment
        self.SS = 0 # Stack Segment

        # Flags
        self.FLAGS = 0

        # Memory
        self.memory = Memory()

    def reset(self):
        self.AX = 0
        self.BX = 0
        self.CX = 0
        self.DX = 0
        self.SI = 0
        self.DI = 0
        self.BP = 0
        self.SP = 0
        self.IP = 0
        self.CS = 0
        self.DS = 0
        self.ES = 0
        self.SS = 0
        self.FLAGS = 0
        self.memory.reset()

    def fetch(self):
        address = self.IP
        instruction = self.memory.read_byte(address)
        self.IP += 1
        return instruction
    
    def decode(self, instruction):
        pass

    def execute(self, instruction):
        pass

    def __str__(self):
        return (f"AX: {self.AX:08X}, BX: {self.BX:08X}, CX: {self.CX:08X}, DX: {self.DX:08X}\n"
        f"CS: {self.CS:08X}, DS: {self.DS:08X}, SS: {self.SS:08X}, ES: {self.ES:08X}\n"
        f"SP: {self.SP:08X}, BP: {self.BP:08X}, SI: {self.SI:08X}, DI: {self.DI:08X}\n"
        f"IP: {self.IP:08X}, FLAGS: {self.FLAGS:08X}")
    
if __name__ == "__main__":
    cpu = CPU()
    print(cpu)