#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import product


def is_associative(matrix, n):
    """Functie pentru testat associativitatea unui tabel."""
    # Genereaza toate listele de 3 elemente: [0, 0, 0], [0, 0, 1]...,[2, 2, 2]
    for indexes in product(range(n), repeat=3):
        i, j, k = indexes
        # (a * b) * c = a * (b * c)
        if matrix[matrix[i][j]][k] != matrix[i][matrix[j][k]]:
            return False
    # Toate operatiile din tabel au fost verificate
    return True


def generate_operations(n):
    """Generate all n by n operation tables."""
    for matrix in product(product(range(n), repeat=n), repeat=n):
        yield matrix

        
def get_associative_operations(n):
    """Get all associative n by n operation tables."""
    for matrix in generate_operations(n):
        if is_associative(matrix, n):
            yield matrix


# In[ ]:


def count_associative_operation_tables(n):
    """Count how many associative operation tables there are for sets <=n."""
    for i in range(n):
        associative_operations = len([x for x in get_associative_operations(i)])
        print(f'There are {associative_operations} associative operations for sets with {i} elements!')
        
count_associative_operation_tables(4)


# In[ ]:


def display_associative_operation_tables(n):
    """Display associative n by n operation tables."""
    for table in get_associative_operations(n):
        for row in table:
            print(row)
        print()
    
display_associative_operation_tables(4)


# In[ ]:




