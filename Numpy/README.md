# [Numpy( Numerical Python ) :](./main.ipynb)
- Numpy is built on C language.
- Fundamental package for scientific computing in python .
- python library that provide multidimensional array objects 

## Advantages of using Numpy arrays over lists : 
- consumes less memory 
- fast as compared to python list
- convenient to use .

List : [1,2,3,4]
ARRAY : [1 2 3 4]

## Difference Between NumPy Arrays and Python Lists

| **Feature**                   | **NumPy Arrays**                                                                                        | **Python Lists**                                                                                      |
|-------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Data Type**                 | Homogeneous: All elements must be of the same data type.                                                | Heterogeneous: Elements can be of different data types.                                               |
| **Performance**               | Faster for numerical operations due to optimized C code.                                                | Slower for numerical operations because of Python’s dynamic typing.                                   |
| **Memory Efficiency**         | More memory-efficient for large datasets.                                                               | Less memory-efficient, especially with large datasets.                                                |
| **Element-wise Operations**   | Supports efficient element-wise operations.(Mathematical operations) `vectorisation`                                                          | Requires explicit loops or list comprehensions for element-wise operations.                           |
| **Dimensionality**            | Supports multi-dimensional arrays (e.g., 2D, 3D arrays).                                                | Primarily one-dimensional; nested lists needed for multi-dimensional data.                            |
| **Functionality**             | Rich set of functions for mathematical, logical, and statistical operations.                            | Basic functionality; requires additional coding or libraries for complex operations.                  |
| **Memory Allocation**         | Allocates memory once at array creation, leading to more predictable memory use.                        | Dynamic memory allocation, which can lead to fragmentation and less efficient memory use.             |
| **Mutability**                | Mutable: You can change elements in place, but the type and size are fixed.                             | Mutable: Elements and the list's size can change, and types can be mixed.                             |

# [Creation of array in Numpy :](array.ipynb)


## Dimensions and shapes in array :
### Dimension :
- In NumPy, the term `"dimension"` refers to the number of axes of an array. 
- For example, a one-dimensional array has one axis, while a two-dimensional array has two axes.
- The number of dimensions of an array can be determined using the `.ndim` attribute.
### Shape : 
- The shape of an array is the number of elements in each dimension or axes .
- The shape is represented as a tuple, where each element of the tuple corresponds to the size of the respective axis.
- `.shape` attribute.


# [Data types in Numpy & Typecasting ](./dataTypes.ipynb)
# [Operations in array](./Operations.ipynb)


# [Broadcasting in NumPy :](./Broadcasting.ipynb)
If we try to perform arithmetic operations on numpy array than if dimensions are different in them than it throws broadcasting error . 
- > But if there is one dimension (i.e. 1 )common seeing from r.h.s in any of two operands than it can perform arithmetic operations . 
- > Condition : r.h.s dimension should be one of anyone operand & l.h.s dimension should be same  




