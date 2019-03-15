#!/usr/bin/env python
# coding: utf-8

# In[122]:


import copy

def get_matrix(n):
    """
    Get an empty matrix.
    """
    matrix = []
    for i in range(n):
        matrix.append([None]*n)
    return matrix

def generate_skeleton(n):
    """
    Generate all n by n abelian group operation table skeletons.
    
    A skeleton is basically an empty matrix with a set identity element.
    """
    for e in range(n):
        matrix = get_matrix(n)
        for i in range(n):
            matrix[e][i] = i
            matrix[i][e] = i
        yield matrix

def fill_abelian_group_table(table, line, column):
    """
    Core functionality to fill table such that it remains an abelian group.
    """
    n = len(table)
    
    # Increment the line if we reached the last column
    if column == n:
        line += 1
        # Set column to line so that we only parse half of the operation table matrix
        column = line
    
    # If the last line and column have been reached we have a valid table!
    if line == n:
        yield table
        return
    
    # Continue to next column if the current one is already set
    if table[line][column] is not None:
        yield from fill_abelian_group_table(table, line, column + 1)

    for i in range(n):
        # Set current position and it's symmetric to main diagonal to any element that
        # is not present in current row OR in symmetric row
        if i not in table[line] and i not in table[column]:
            table_copy = copy.deepcopy(table)
            
            table_copy[line][column] = i
            table_copy[column][line] = i
            
            yield from fill_abelian_group_table(table_copy, line, column + 1)
        
        
def pretty_print_abelian_group_tables(n):
    """
    Utility to display table
    """
    skeleton_tables = generate_skeleton(n)

    for skeleton in skeleton_tables:
        filled_tables_generator = fill_abelian_group_table(skeleton, 0, 0)
        for table in filled_tables_generator:
            for row in range(n):
                print('\t'.join([str(x) for x in table[row]]))
            print('- ' * n * 4)
    


# In[123]:


pretty_print_abelian_group_tables(2)


# In[124]:


pretty_print_abelian_group_tables(3)


# In[125]:


pretty_print_abelian_group_tables(4)


# In[126]:


pretty_print_abelian_group_tables(5)


# In[127]:


pretty_print_abelian_group_tables(6)


# In[ ]:


pretty_print_abelian_group_tables(7)


# In[ ]:


pretty_print_abelian_group_tables(8)


# In[ ]:




