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

# Data
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
