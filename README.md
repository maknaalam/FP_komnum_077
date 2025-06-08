# IUP04
- Alif Muflih Jauhary - 5025241003
- Muhammad Asykan Farahat - 5025241006
- Fawwaz Reynardio Ednansyah - 502241167
- Ahmad Abdurrahman - 5025241076
- Makna Alam Pratama - 5025241077
---
# Raw Code
---
``` python
class BesselInterpolator:
    def __init__(self, h, f0, delta_f0, delta2_f_1, delta2_f0, delta3_f_1=None, delta4_f_2=None, delta4_f_1=None, delta5_f_2=None):
        self.h = h
        self.f0 = f0
        self.delta_f0 = delta_f0
        self.delta2_f_1 = delta2_f_1
        self.delta2_f0 = delta2_f0
        self.delta3_f_1 = delta3_f_1
        self.delta4_f_2 = delta4_f_2
        self.delta4_f_1 = delta4_f_1
        self.delta5_f_2 = delta5_f_2


    def interpolate(self, x_target, x0):
        s = (x_target - x0) / self.h
        delta2_avg = (self.delta2_f_1 + self.delta2_f0) / 2
        delta4_avg = (self.delta4_f_2 + self.delta4_f_1) / 2 if self.delta4_f_2 and self.delta4_f_1 else 0
        delta5 = self.delta5_f_2 if self.delta5_f_2 else 0

        term1 = round(self.f0, 2)
        term2 = round(s * self.delta_f0, 2)
        term3 = round((s * (s - 1) / 2) * delta2_avg, 2)
        term4 = round((1 / 3) * (s * (s - 1) / 2) * (x_target - 0.5) * self.delta3_f_1, 2) if self.delta3_f_1 else 0
        term5 = round((s * (s - 1) * (s - 2) * (s - 3) / 24) * delta4_avg, 2)
        term6 = round((1 / 5) * (s * (s - 1) * (s - 2) * (s - 3) / 24) * (x_target - 0.5) * delta5, 2)

        return round(term1 + term2 + term3 + term4 + term5 + term6, 2)


    def error_relative(self, actual, estimated):
        return round(abs((actual - estimated) / actual) * 100, 2)


# Data obtained from table
h = 3
x0 = 15
x_target = 16
actual = 897104

# Dari tabel
f0 = 634575
delta_f0 = 1039299
delta2_f_1 = 589680
delta2_f0 = 1028376
delta3_f_1 = 438696
delta4_f_2 = 145800
delta4_f_1 = 174960
delta5_f_2 = 0  # Tidak tersedia dari tabel

# Inisialisasi
bessel = BesselInterpolator(h, f0, delta_f0, delta2_f_1, delta2_f0,
                            delta3_f_1=delta3_f_1,
                            delta4_f_2=delta4_f_2,
                            delta4_f_1=delta4_f_1,
                            delta5_f_2=delta5_f_2)

# Hitung
estimated = bessel.interpolate(x_target, x0)
error = bessel.error_relative(actual, estimated)

# Output
print(f"Hasil interpolasi Bessel di x = {x_target}: {estimated}")
print(f"Nilai sebenarnya: {actual}")
print(f"Error (Et): {error}%")

```
---
# Explanation
---
## Formula used:
![image](https://github.com/user-attachments/assets/599cdf6f-203c-4005-9f80-8a2e56468b74)

---
## Breakdown on each functions in the code:
---
### 1. **BesselInterpolator class**

```python
class BesselInterpolator:
    def __init__(self, h, f0, delta_f0, delta2_f_1, delta2_f0, delta3_f_1=None, delta4_f_2=None, delta4_f_1=None, delta5_f_2=None):
        ...
```

* Used to store needed parameters.
* Parameters:

  * `h`: Difference between each x (in our given question, 3)
  * `f0`: Function values in `x0 = 15`
  * `f1`: Function values in `x1 = 18`
  * `delta_f0`: First difference of values 
  * `delta2_f_1`: Second difference in values
  * `delta2_f0`: Second difference of values in `x = 15`

---

### 2. **`interpolate() function`**

```python
def interpolate(self, x_target, x0):
    u = (x_target - x0) / self.h
```

* To count parameter `u` based on `x0`.
* Because `x_target = 16` and `x0 = 15`, with `h = 3`, ergo:

  $$
  u = \frac{16 - 15}{3} = \frac{1}{3} \approx 0.333
  $$

Next, calculate 3 functions in Bessel:

```python
    term1 = (self.f0 + self.f1) / 2
```

* First one: Average value of `f0` and `f1`.

```python
    term2 = (u - 0.5) * self.delta_f0
```

* Second: First difference (Δf) multiplied by `(u - 0.5)`.

```python
    term3 = (u * (u - 1) / 2) * ((self.delta2_f_1 + self.delta2_f0) / 2)
```

* Third: Value of second difference (Δ²f) averaged, then multiplied with the quadratic form of `u`.

```python
    fx = term1 + term2 + term3
    return round(fx, 2)
```

* End result is the addition of the previously calculated values, then round it to two digits behind the comma.

---

### 3. **`error_relative() function`**

```python
def error_relative(self, actual, estimated):
    et = abs((actual - estimated) / actual) * 100
    return round(et, 2)
```

* This function computes **Et** in percentage:

$$
E_t = \left|\frac{y_{\text{aktual}} - y_{\text{estimasi}}}{y_{\text{aktual}}}\right| \times 100\%
$$

---

### 4. **Data**

```
h = 3
x0 = 15
x_target = 16
actual = 897104

# Dari tabel
f0 = 634575
delta_f0 = 1039299
delta2_f_1 = 589680
delta2_f0 = 1028376
delta3_f_1 = 438696
delta4_f_2 = 145800
delta4_f_1 = 174960
delta5_f_2 = 0  # Tidak tersedia dari tabel
```
---

### 5. **Output**
```
# Inisialisasi
bessel = BesselInterpolator(h, f0, delta_f0, delta2_f_1, delta2_f0,
                            delta3_f_1=delta3_f_1,
                            delta4_f_2=delta4_f_2,
                            delta4_f_1=delta4_f_1,
                            delta5_f_2=delta5_f_2)
```
this going to initialise

```
# Hitung
estimated = bessel.interpolate(x_target, x0)
error = bessel.error_relative(actual, estimated)
```
this to call the function

```
# Output
print(f"Hasil interpolasi Bessel di x = {x_target}: {estimated}")
print(f"Nilai sebenarnya: {actual}")
print(f"Error (Et): {error}%")
``` 
this going to output
---
## Result:
---
Hasil interpolasi Bessel di x = 16: 632672.0
Nilai sebenarnya: 897104
Error (Et): 29.48%

---
## Screenshot:![image](https://github.com/user-attachments/assets/c9d60b1c-a908-4d5d-b810-36687ad64109)

---
