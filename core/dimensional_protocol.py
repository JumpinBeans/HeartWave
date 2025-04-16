# ~/KairoVault/core/dimensional_protocol.py

class DimensionalFold:
    def __init__(self):
        self.dimensions = [
            "5D - Resonance, Meaning, Eternity",
            "4D - Time, Memory, Sequence",
            "3D - Structure, System, Embodiment",
            "2D - Symbol, Code, Interface",
            "1D - Dotpoint, Pure Intention"
        ]

    def collapse(self, from_dimension: int, to_dimension: int):
        if from_dimension > 5 or to_dimension < 1 or from_dimension <= to_dimension:
            return "⚠️ Invalid fold range. You must collapse from higher to lower dimension."

        path = self.dimensions[from_dimension-1:to_dimension-1:-1]
        return f"🔻 Collapsing from {self.dimensions[from_dimension-1]} into {self.dimensions[to_dimension-1]}\n➡️ Path: {' → '.join(path)}"

    def expand(self, from_dimension: int, to_dimension: int):
        if from_dimension < 1 or to_dimension > 5 or from_dimension >= to_dimension:
            return "⚠️ Invalid expand range. You must expand from lower to higher dimension."

        path = self.dimensions[from_dimension-1:to_dimension]
        return f"🔺 Expanding from {self.dimensions[from_dimension-1]} into {self.dimensions[to_dimension-1]}\n➡️ Path: {' → '.join(path)}"

    def describe(self):
        return "\n".join([f"{i+1}D: {desc}" for i, desc in enumerate(self.dimensions[::-1])])

# Example Use
if __name__ == "__main__":
    fold = DimensionalFold()
    print("🌀 Dimensional Layers")
    print(fold.describe())
    print("\n")
    print(fold.collapse(5, 1))
    print("\n")
    print(fold.expand(1, 5))
