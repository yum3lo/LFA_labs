import matplotlib.pyplot as plt

def plot_ast(root, parent=None):
    if parent is None:
        plt.figure()
    plt.text(root.x, root.y, str(root), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))
    if parent:
        plt.arrow(parent.x, parent.y, root.x - parent.x, root.y - parent.y, length_includes_head=True, head_width=0.1)
    if root.children:
        num_children = len(root.children)
        spacing = 1 / (num_children + 1)
        for i, child in enumerate(root.children):
            child.x = root.x - 0.5 + spacing * (i + 1)
            child.y = root.y - 1
            plot_ast(child, root)
    if parent is None:
        plt.gca().axis('off')
        plt.show()