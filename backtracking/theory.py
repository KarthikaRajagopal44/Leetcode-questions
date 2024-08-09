# Backtracking:
#  Pure Algorithmic Steps
# ------------------------------------------------------------------------------------------------------------------------
# Start with an Empty Solution:

# Begin with an empty solution or an initial state.
# Check if the Current Solution is Complete:

# At each step, check if the current solution meets the problem's requirements.
# If the solution is complete, record or return it as a valid solution.
# Iterate Over All Possible Choices:

# For the current step, consider all possible choices or options that can be made.
# For example, in generating permutations, you would consider each element that can be added to the current sequence.
# Make a Choice:

# Choose one of the possible options and add it to the current solution.
# This is like "moving forward" in the search space.
# Recursively Explore Further:

# Recursively continue by repeating steps 2-5 with the updated solution.
# This explores deeper into the decision tree, considering subsequent choices.
# Backtrack (Undo the Last Choice):

# If adding the current choice does not lead to a valid solution, or after exploring all options with the current choice, "backtrack" by undoing the last step.
# This involves removing the last choice from the solution and trying the next possible option.
# Repeat Until All Options are Explored:

# Continue this process until all possible configurations have been explored.
# Depending on the problem, you may want to find one solution, all solutions, or the best solution.
# End the Process:

# Once all possibilities have been explored, the algorithm terminates.
# The output could be a set of solutions, the best solution, or just a confirmation that a solution exists.
# Example: Generating All Subsets of a Set
# Consider a simple example where we want to generate all subsets of a set {1, 2, 3} using backtracking.

# Start: Begin with an empty subset [].
# Check: If the subset is complete (when you've considered all elements), record it.
# Choices: For each element, decide whether to include it in the current subset or not.
# Recursively Explore:
# Include the element, e.g., 1.
# Explore subsets starting with [1].
# Include the next element, e.g., [1, 2].
# Continue this until you've considered all elements.
# Backtrack: If you've considered all elements after adding 1, backtrack to remove 1 and try the next possibility, e.g., starting with [2].
# Repeat: Continue this process until you've explored all possible subsets.
# End: Once all subsets are generated, stop.