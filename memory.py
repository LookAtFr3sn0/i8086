class Memory:
    def __init__(self):
        self.memory = bytearray(1024 * 1024)

    def read_byte(self, address):
        return self.memory[address]
    
    def write_byte(self, address, value):
        self.memory[address] = value & 0xFF
    
    def read_word(self, address):
        low = self.memory[address]
        high = self.memory[address + 1]
        return (high << 8) | low
    
    def write_word(self, address, value):
        low = value & 0xFF
        high = (value >> 8) & 0xFF
        self.memory[address] = low
        self.memory[address + 1] = high

    def reset(self):
        self.memory = bytearray(1024 * 1024)
    
    def __str__(self):
        lines = []
        for i in range(0, len(self.memory), 16):
            hex_bytes = " ".join(f"{b:02X}" for b in self.memory[i:i+16])
            lines.append(hex_bytes)
        return "\n".join(lines)

if __name__ == "__main__":
    memory = Memory()
    print(memory)