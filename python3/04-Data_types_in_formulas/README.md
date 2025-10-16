# 34.4 PRACTICE: Data types in formulas

**Instructions:**

Write a short Python program to run without errors and align to the requirements described below. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

---

**Task:**

Create a solution that accepts any three integer inputs representing the base (b1, b2) and height (h) measurements of a trapezoid in meters. Output the exact area of the trapezoid in square meters as a float value. The exact area of a trapezoid can be calculated by finding the average of the two base measurements, then multiplying by the height measurement.

Trapezoid Area Formula:

```Math
A = [(b1 + b2) / 2] * h
```

The solution output should be in the format:

```Python
Trapezoid area: area_value square meters
```

---
**Sample Input/Output:**  

If the input is

```Python
3
4
5
```

then the expected output is

```Python
Trapezoid area: 17.5 square meters
```

Alternatively, if the input is

```Python
3
5
6
```

Then the expected output is

```Python
Trapezoid area: 28.0 square meters
```

## LAB ACTIVITY | 34.4.1: PRACTICE: Data types in formulas

main.py

```Python
#solution accepts three integer values representing base and height measurements of a trapezoid

#first and second integers represent base 1 and base 2; third integer represents height 

#solution outputs the trapezoid area in square meters using formula A = ½(b1+b2)h

```
