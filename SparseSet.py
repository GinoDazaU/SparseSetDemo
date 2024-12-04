import matplotlib.pyplot as plt

class SparseSet:
    def __init__(self, n):
        self.n = n
        self.sparse = [-1] * n
        self.dense = [0] * n
        self.size = 0

    def insert(self, x):
        if self.contains(x):
            return
        self.sparse[x] = self.size
        self.dense[self.size] = x
        self.size += 1

    def remove(self, x):
        if not self.contains(x):
            return
        idx = self.sparse[x]
        last = self.dense[self.size - 1]
        self.dense[idx] = last
        self.sparse[last] = idx
        self.sparse[x] = -1
        self.size -= 1

    def contains(self, x):
        return 0 <= x < self.n and self.sparse[x] < self.size and self.dense[self.sparse[x]] == x

    def visualize(self, operation=None, subtitle=None):
        fig, ax = plt.subplots(2, 1, figsize=(10, 6))

        # Dense Array Visualization
        ax[0].set_title("Dense Array")
        for i in range(self.n):
            color = "lightblue" if i < self.size else "white"
            ax[0].add_patch(plt.Rectangle((i, 0), 1, 1, edgecolor="black", facecolor=color))
            val = self.dense[i] if i < self.size else "-"
            ax[0].text(i + 0.5, 0.5, str(val), ha='center', va='center', fontsize=12)
        ax[0].set_xlim(0, self.n)
        ax[0].set_ylim(0, 1)
        ax[0].set_xticks(range(self.n))
        ax[0].set_yticks([])
        ax[0].grid(axis='x', linestyle='--', alpha=0.5)

        # Sparse Array Visualization
        ax[1].set_title("Sparse Array")
        for i in range(self.n):
            color = "lightcoral" if self.sparse[i] != -1 else "white"
            ax[1].add_patch(plt.Rectangle((i, 0), 1, 1, edgecolor="black", facecolor=color))
            val = self.sparse[i]
            ax[1].text(i + 0.5, 0.5, str(val), ha='center', va='center', fontsize=12)
        ax[1].set_xlim(0, self.n)
        ax[1].set_ylim(0, 1)
        ax[1].set_xticks(range(self.n))
        ax[1].set_yticks([])
        ax[1].grid(axis='x', linestyle='--', alpha=0.5)

        title = f"State after {operation}" if operation else "Sparse Set State"
        if subtitle:
            title += f" ({subtitle})"
        fig.suptitle(title, fontsize=16)

        plt.tight_layout()
        plt.show()
