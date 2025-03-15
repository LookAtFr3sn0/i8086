from memory import Memory 

class CPU:
    def __init__(self):
        # General purpose registers
        self.AX = 0
        self.BX = 0
        self.CX = 0
        self.DX = 0

        # Index registers
        self.SI = 0
        self.DI = 0
        self.BP = 0
        self.SP = 0

        # Program counter
        self.IP = 0

        # Segment registers
        self.CS = 0
        self.DS = 0
        self.ES = 0
        self.SS = 0

        # Flags
        self.FLAGS = 0

        # Memory
        self.memory = Memory()

    def __str__(self):
        return (f"AX: {self.AX:08X}, BX: {self.BX:08X}, CX: {self.CX:08X}, DX: {self.DX:08X}\n"
        f"CS: {self.CS:08X}, DS: {self.DS:08X}, SS: {self.SS:08X}, ES: {self.ES:08X}\n"
        f"SP: {self.SP:08X}, BP: {self.BP:08X}, SI: {self.SI:08X}, DI: {self.DI:08X}\n"
        f"IP: {self.IP:08X}, FLAGS: {self.FLAGS:08X}")
    
if __name__ == "__main__":
    cpu = CPU()
    print(cpu)