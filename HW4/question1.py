p = 1048579

#2^(2^20+2) = 2^(2^20) + 2^2
import math
mods = {0:2}
for i in range(1,21):
    mod = (mods[i-1]*mods[i-1])%p
    mods[i] = mod
    print(f'2^(2^{i}) mod {p} = (2^(2^{i-1}) mod {p} * 2^(2^{i-1}) mod {p}) mod {p} = {mod}')

print(f'2^(2^20+2) mod {p} = (2^(2^20) mod {p} * 2^(2) mod {p}) mod {p} = {(mods[20]*mods[1]) % p}')