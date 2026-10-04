# Redfall ADS Sensitivity Fix

A small utility that patches `Redfall.exe`(version 1.451.8.0) to apply a custom aim-down-sights (ADS) sensitivity multiplier.

## How It Works

Several instructions are involved in setting the ADS sensitivity multiplier:

- `Redfall.exe+10D3295` - `mov dword ptr [rcx+0x48], 0x3F000000`
- `Redfall.exe+D3F9B2` - `mov eax, dword ptr [rcx+0x128]`
- `Redfall.exe+D3F9BB` - `mov eax, dword ptr [rcx+0x128]`

This fix targets the last one, `Redfall.exe+D3F9BB`, and replaces the load with a constant float of your choice.

Example (multiplier `0.7`):
```
mov eax, dword ptr [rcx+0x128]   ->   mov eax, 0x3F333333 ; nop
8B 81 28 01 00 00                ->   B8 33 33 33 3F 90
```

## How to Use

1. Download the utility from the [Releases tab](https://github.com/K4t3N0k/Redfall-Ads-Sensitivity-Fix/releases/)
2. Make sure the game is closed
3. Place `ads_fix.exe` in the game directory, right next to `Redfall.exe`.
   *(Default path: `...\Steam\steamapps\common\Redfall\Redfall\Binaries\Win64\`)*
4. Run `ads_fix.exe`
5. Select your desired ADS sensitivity multiplier (I recommend `0.7`)
6. Click **Apply**
7. Close
8. Launch the game
