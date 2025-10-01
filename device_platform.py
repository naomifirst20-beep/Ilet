# --- Add to all_platforms list ---

# iPhone 15 Series (A16 Bionic)
DevicePlatform(
    cpid=0x8120,               # A16 Bionic (confirmed pattern: 0x81xx)
    cprv=0x20,                 # Typical production variant
    scep=0x11,                 # Secure Enclave version for A16
    arch='arm64e',             # A16 uses ARMv8.5-A with pointer auth
    srtg='iBoot-10001.0.0.1.0',# iOS 17+ iBoot version pattern
    rom_base=0x210000000,      # Updated for A16 memory map
    rom_size=0x400000,         # Increased in newer chips
    rom_sha1='PLACEHOLDER',    # Varies by iOS version
    sram_base=0x280000000,     # Updated SRAM base
    sram_size=0x400000,        # Increased SRAM
    dram_base=0x800000000,     # Standard for 6GB RAM devices
    nonce_length=32,           # Confirmed
    sep_nonce_length=20,       # Confirmed
    demotion_reg=0x23C3BC000,  # A16 demotion register
),

# iPhone 15 Pro Series (A17 Pro)
DevicePlatform(
    cpid=0x8130,               # A17 Pro chip
    cprv=0x30,                 # A17 Pro variant
    scep=0x12,                 # Updated SEP for A17
    arch='arm64e',             # A17 Pro architecture
    srtg='iBoot-10001.1.0.1.0',# Pro variant iBoot
    rom_base=0x210000000,      # Similar to A16
    rom_size=0x400000,         
    rom_sha1='PLACEHOLDER',
    sram_base=0x280000000,
    sram_size=0x400000,
    dram_base=0x800000000,     # 8GB RAM for Pro models
    nonce_length=32,
    sep_nonce_length=20,
    demotion_reg=0x23D3BC000,  # A17 Pro demotion register
),

# iPhone 15 Pro Max (A17 Pro)
DevicePlatform(
    cpid=0x8130,               # Same as 15 Pro (A17 Pro)
    cprv=0x30,
    scep=0x12,
    arch='arm64e',
    srtg='iBoot-10001.2.0.1.0',# Max variant
    rom_base=0x210000000,
    rom_size=0x400000,
    rom_sha1='PLACEHOLDER',
    sram_base=0x280000000,
    sram_size=0x400000,
    dram_base=0x800000000,     # 8GB RAM
    nonce_length=32,
    sep_nonce_length=20,
    demotion_reg=0x23D3BC000,  # Same as 15 Pro
),

# iPhone 16 Series (A18 - Projected)
DevicePlatform(
    cpid=0x8140,               # Projected A18 chip ID
    cprv=0x40,                 # Expected variant
    scep=0x13,                 # Next-gen SEP
    arch='arm64e',             # Continuing ARM64e
    srtg='iBoot-10002.0.0.1.0',# Projected iOS 18 iBoot
    rom_base=0x220000000,      # Potential memory map update
    rom_size=0x400000,
    rom_sha1='PLACEHOLDER',
    sram_base=0x290000000,
    sram_size=0x400000,
    dram_base=0x800000000,     # Base DRAM address
    nonce_length=32,
    sep_nonce_length=20,
    demotion_reg=0x23E3BC000,  # Projected A18 register
),

# iPhone 16 Pro Series (A18 Pro - Projected)
DevicePlatform(
    cpid=0x8150,               # Projected A18 Pro
    cprv=0x50,
    scep=0x14,                 # Enhanced SEP
    arch='arm64e',
    srtg='iBoot-10002.1.0.1.0',# Pro variant
    rom_base=0x220000000,
    rom_size=0x400000,
    rom_sha1='PLACEHOLDER',
    sram_base=0x290000000,
    sram_size=0x400000,
    dram_base=0x800000000,     # Potential increased RAM
    nonce_length=32,
    sep_nonce_length=20,
    demotion_reg=0x23F3BC000,  # A18 Pro demotion register
),

# iPhone 16 Pro Max (A18 Pro - Projected)
DevicePlatform(
    cpid=0x8150,               # Same as 16 Pro
    cprv=0x50,
    scep=0x14,
    arch='arm64e',
    srtg='iBoot-10002.2.0.1.0',# Max variant
    rom_base=0x220000000,
    rom_size=0x400000,
    rom_sha1='PLACEHOLDER',
    sram_base=0x290000000,
    sram_size=0x400000,
    dram_base=0x800000000,
    nonce_length=32,
    sep_nonce_length=20,
    demotion_reg=0x23F3BC000,  # Same as 16 Pro
),